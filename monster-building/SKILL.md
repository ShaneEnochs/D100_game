---
name: monster-building
description: Build correct monster stat blocks for the RPG project and run creatures in encounters. Use this skill the moment any creature without an existing block is about to appear in play, when statting bestiary creatures at a chosen level, when designing encounter opposition, or when checking monster math. Also use it before every first encounter with a named module creature (the Shade Courier, Bett Sorrel, portal spawns).
---

# Monster Building

Rule from `gm_guide.md`: build the block BEFORE resolving anything or rolling
initiative. Never improvise stats mid-fight.

## The procedure

1. **Pick the level.** Bestiary entries carry a typical range (1-3 or 3-5);
   the GM assigns the actual level using the party's level and the fiction. A
   3-5 creature met by level 1 hunters is meant to be more trouble than the
   block suggests — that is the design, not an error.
2. **Get the base block:**
   ```
   python3 .claude/skills/monster-building/scripts/statblock.py <level>
   ```
   This prints the canonical Might/Magic/mods/HP from the published tables.
   Do not compute these by hand and do not use the formula text in
   rpg_core_system.md directly — the tables deviate from their own formulas
   in six known places, and the tables are what governs. `--verify` proves
   the tool still matches the file.
3. **Monsters have two stats only** — Might and Magic. Every roll a monster
   makes uses one of them.
4. **Give it 1-4 unique abilities or aspects.** This is the whole identity of
   the creature; the base block is shared by everything at its level. Follow
   the conventions in `references/ability_design.md` (grammar, damage bands,
   the on-death/rider/sense taxonomy drawn from the existing forty entries).
5. **Write the attack line:** dice + the relevant mod + a damage type
   (blade/piercing/blunt, or magic). Bestiary norm at levels 1-3 is
   1d4 + Might Mod; heavier 3-5 predators run 1d6 to 1d8. Magic attackers
   use Magic Mod.
6. **Write the block down** — name, level, stats, mods, HP, DR if any,
   attack line, abilities — then roll initiative and begin.

## Running monsters

- Attacks are opposed rolls through the roller, like everything else.
- Monster DR comes only from abilities (Bone Shell, etc.); subtract by
  damage type where the ability says so.
- Ability usage follows each ability's own text; there is no monster skill
  point pool unless a ruling creates one (see the rules-resolution ledger).
- Infernals drop mana stones on death; grade tracks tier (Tier 1 → E/F).
  Exact drops are ruling space — log what you rule.
- XP on kill = the creature's level, to every party member, tier-gated.

## Levels above 5, and above 50

- Levels 6-50 have published base stats; `statblock.py` serves them. What
  does NOT exist yet is a bestiary of named creatures above level 5 — that
  is design work owned by the `content-authoring` and
  `campaign-advancement` skills (Act 3 needs level 6-8 blocks; Act 4 needs
  a Tier 2 bestiary).
- Past level 50 there is no table at all. Stats cap at 99 by level 48-50;
  the stated rule is that further bumps convert into new abilities,
  resistances, or immunities. Extending there is new design, not table
  lookup.

## If the tables ever change

`statblock.py --verify` fails when `rpg_core_system.md`'s tables and the
tool's embedded copy diverge. That failure means someone edited one without
the other. Reconcile deliberately: find the ruling that authorized the
change, update both, and update the known-deviations list in the script and
in `rules-resolution/references/rulings_and_precedence.md`.
