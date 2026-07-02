#!/usr/bin/env python3
"""
validate_state.py — checks the two live state files for internal consistency
with the rules in rpg_core_system.md and skills_and_aspects.md.

Usage:
    python3 validate_state.py <character_sheet.json> <campaign_state.json>

Run this at every session close (gm_guide.md Part 7, step 4) and any time a
file has been edited by hand. Exit code 0 = clean, 1 = errors found.
Warnings do not fail the run; errors do.

What it derives instead of trusting:
  * XP thresholds from the formula: threshold(L) = threshold(L-1) + L * tier_multiplier,
    multipliers 10/8/6/4/2 for tiers 1-5. Verified against the published table.
  * Modifiers: stat // 10.
  * Tier: (level - 1) // 10 + 1.
  * Skill points per encounter: 2 + Intellect // 10.
  * Slot ceilings by tier: skills 2/3/4/5/6, aspects 1/2/3/4/5.

What it cannot check: narrative truth (whether an NPC entry reflects what was
said in play). That stays a human/GM read of the session notes.
"""

import json
import sys

TIER_MULT = {1: 10, 2: 8, 3: 6, 4: 4, 5: 2}
SKILL_SLOTS = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6}
ASPECT_SLOTS = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

errors = []
warnings = []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def tier_of(level):
    return (level - 1) // 10 + 1


def xp_threshold(level):
    """XP required to go from `level` to `level`+1... in this system the table
    lists, per level L, the XP needed to REACH the next level while at L.
    threshold(1) = 10; threshold(L) = threshold(L-1) + (L * multiplier of L's tier).
    Spot-checked against the published table: L10=550, L11=638, L20=1790,
    L21=1916, L30=3320, L31=3444, L40=4740, L41=4822, L50=5650."""
    t = 0
    for lv in range(1, level + 1):
        t += lv * TIER_MULT[tier_of(lv)]
    return t


def load(path, label):
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        err(f"{label}: file not found at {path}")
    except json.JSONDecodeError as e:
        err(f"{label}: does not parse as JSON — {e}")
    return None


def check_character(c):
    required = ["name", "race", "class", "level", "tier", "xp_pool",
                "xp_next_level", "stats", "modifiers", "hp",
                "skill_points_per_encounter", "skills", "aspects",
                "racial_trait", "equipment", "currency"]
    missing = [k for k in required if k not in c]
    for key in missing:
        err(f"character sheet: missing required key '{key}'")
    if missing:
        return

    level = c["level"]
    if not (1 <= level <= 50):
        err(f"character sheet: level {level} outside 1-50")
        return

    # Tier
    expect_tier = tier_of(level)
    if c["tier"] != expect_tier:
        err(f"character sheet: tier {c['tier']} but level {level} is tier {expect_tier}")

    # Stats and modifiers
    for stat in ["might", "intellect", "magic", "social"]:
        v = c["stats"].get(stat)
        if v is None:
            err(f"character sheet: stats.{stat} missing")
            continue
        if not (1 <= v <= 99):
            err(f"character sheet: stats.{stat} = {v}, must be 1-99 (cap is 99)")
        mod_key = f"{stat}_mod"
        mod = c["modifiers"].get(mod_key)
        if mod is None:
            err(f"character sheet: modifiers.{mod_key} missing")
        elif mod != v // 10:
            err(f"character sheet: modifiers.{mod_key} = {mod} but {stat} {v} // 10 = {v // 10}")

    # XP threshold
    expect_next = xp_threshold(level)
    if c["xp_next_level"] != expect_next:
        err(f"character sheet: xp_next_level = {c['xp_next_level']} but the "
            f"formula gives {expect_next} for level {level}")
    if c["xp_pool"] < 0:
        err(f"character sheet: xp_pool is negative ({c['xp_pool']})")

    # HP
    hp = c["hp"]
    if hp.get("current") is None or hp.get("max") is None:
        err("character sheet: hp needs 'current' and 'max'")
    else:
        if hp["current"] > hp["max"]:
            err(f"character sheet: hp current {hp['current']} > max {hp['max']}")
        if hp["max"] < 1:
            err("character sheet: hp max below 1")
        if hp["current"] < 0:
            err("character sheet: hp current below 0")
        # Max HP cannot be reconstructed from stats alone (level-up gains lock
        # in at the Might Mod current at the time). Only the level-1 case is
        # fully determined.
        if level == 1:
            expect_max = 20 + c["stats"]["might"] // 10
            if hp["max"] != expect_max:
                err(f"character sheet: at level 1, hp max should be "
                    f"20 + Might Mod = {expect_max}, found {hp['max']}")

    # Skill points
    expect_sp = 2 + c["stats"]["intellect"] // 10
    if c["skill_points_per_encounter"] != expect_sp:
        err(f"character sheet: skill_points_per_encounter = "
            f"{c['skill_points_per_encounter']} but 2 + Intellect Mod = {expect_sp}")

    # Slots
    if len(c["skills"]) > SKILL_SLOTS[expect_tier]:
        err(f"character sheet: {len(c['skills'])} skills equipped, tier "
            f"{expect_tier} allows {SKILL_SLOTS[expect_tier]}")
    if len(c["aspects"]) > ASPECT_SLOTS[expect_tier]:
        err(f"character sheet: {len(c['aspects'])} aspects equipped, tier "
            f"{expect_tier} allows {ASPECT_SLOTS[expect_tier]}")

    # Ability shapes and level requirements
    for s in c["skills"]:
        for key in ["name", "cost", "stat", "effect", "level_req"]:
            if key not in s:
                err(f"character sheet: skill '{s.get('name', '?')}' missing '{key}'")
        if s.get("level_req", 0) > level:
            err(f"character sheet: skill '{s.get('name')}' requires level "
                f"{s['level_req']}, character is level {level}")
        if s.get("cost") not in (1, 2, 3, None):
            warn(f"character sheet: skill '{s.get('name')}' has cost "
                 f"{s.get('cost')} — catalog uses 1, 2, or 3")
    for a in c["aspects"]:
        for key in ["name", "effect", "level_req"]:
            if key not in a:
                err(f"character sheet: aspect '{a.get('name', '?')}' missing '{key}'")
        if a.get("level_req", 0) > level:
            err(f"character sheet: aspect '{a.get('name')}' requires level "
                f"{a['level_req']}, character is level {level}")

    # Currency
    cur = c["currency"]
    if cur.get("credits", 0) < 0:
        err("character sheet: negative credits")
    if not isinstance(cur.get("mana_stones", []), list):
        err("character sheet: currency.mana_stones must be a list")


def check_campaign(s):
    required = ["current_to", "session_count", "campaign", "location",
                "resume_point", "active_quests", "completed_quests",
                "npc_knowledge"]
    missing = [k for k in required if k not in s]
    for key in missing:
        err(f"campaign state: missing required key '{key}'")
    if missing:
        return

    cur = s["current_to"]
    if not (isinstance(cur, str) and cur.startswith("session-")):
        err(f"campaign state: current_to should look like 'session-N', found {cur!r}")
    else:
        try:
            n = int(cur.split("-", 1)[1])
            if n != s["session_count"]:
                err(f"campaign state: current_to says session {n} but "
                    f"session_count is {s['session_count']}")
        except ValueError:
            err(f"campaign state: cannot read a number out of current_to {cur!r}")

    if not str(s["resume_point"]).strip():
        err("campaign state: resume_point is empty — the next session cannot open")

    if not isinstance(s["active_quests"], list):
        err("campaign state: active_quests must be a list")
    if not isinstance(s["completed_quests"], list):
        err("campaign state: completed_quests must be a list")

    nk = s["npc_knowledge"]
    if not isinstance(nk, dict):
        err("campaign state: npc_knowledge must be an object keyed by NPC id")
    else:
        for npc, entry in nk.items():
            if "knows" not in entry or not isinstance(entry["knows"], list):
                err(f"campaign state: npc_knowledge.{npc} needs a 'knows' list")
            if "does_not_know" in entry and not isinstance(entry["does_not_know"], list):
                err(f"campaign state: npc_knowledge.{npc}.does_not_know must be a list")
            if not entry.get("knows"):
                warn(f"campaign state: npc_knowledge.{npc}.knows is empty — "
                     f"an NPC who knows nothing about the character may not "
                     f"need an entry yet")

    if "rulings" in s and not isinstance(s["rulings"], list):
        err("campaign state: rulings must be a list")


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        return 1

    char = load(sys.argv[1], "character sheet")
    camp = load(sys.argv[2], "campaign state")
    if char is not None:
        check_character(char)
    if camp is not None:
        check_campaign(camp)

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    if not errors:
        print(f"OK — both files pass "
              f"({len(warnings)} warning{'s' if len(warnings) != 1 else ''}).")
        return 0
    print(f"\n{len(errors)} error(s). Fix these before delivering files — "
          f"the state files are the truth of the campaign.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
