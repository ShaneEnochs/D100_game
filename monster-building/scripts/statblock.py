#!/usr/bin/env python3
"""
statblock.py — canonical monster base stats for the RPG Core System.

The published tables in rpg_core_system.md are the rules of record. This tool
embeds them verbatim so a session never has to re-derive them, and it carries
the generative formulas as a cross-check so table edits and extensions can be
verified instead of eyeballed.

Usage:
    python3 statblock.py <level>            Print the base block for one level (1-50).
    python3 statblock.py --range <a> <b>    Print blocks for a level range.
    python3 statblock.py --verify           Cross-check tables against the formulas.
                                            Exits 0 if only the KNOWN deviations exist,
                                            1 if any new deviation appears.

Known facts (verified 2026-07-02, do not "fix" without a logged ruling):
  * Five HP rows sit exactly +10 above the accumulation formula:
    levels 3, 10, 31, 38, 47. The table wins — players have seen it.
  * The Might column from level 22 onward runs 1 point below strict
    bump alternation (one Might bump is missing at level 22). The table wins.
  * HP formula: raw = 20 + MightMod at L1; each level adds MightMod + Level;
    displayed HP = raw rounded to the nearest 10, half rounded up.
  * Stat bumps per level equal the tier number, alternating per
    rpg_core_system.md "Monster Stat Growth". Stats cap at 99; capped bumps
    convert into extra abilities/resistances (GM's design call).
"""

import sys

# (Might, Magic, MightMod, MagicMod, HP) — verbatim from rpg_core_system.md
TABLE = {
    1: (31, 30, 3, 3, 20),   2: (31, 31, 3, 3, 30),   3: (32, 31, 3, 3, 40),
    4: (32, 32, 3, 3, 40),   5: (33, 32, 3, 3, 50),   6: (33, 33, 3, 3, 60),
    7: (34, 33, 3, 3, 70),   8: (34, 34, 3, 3, 80),   9: (35, 34, 3, 3, 90),
    10: (35, 35, 3, 3, 110),
    11: (36, 36, 3, 3, 120), 12: (37, 37, 3, 3, 130), 13: (38, 38, 3, 3, 150),
    14: (39, 39, 3, 3, 170), 15: (40, 40, 4, 4, 190), 16: (41, 41, 4, 4, 210),
    17: (42, 42, 4, 4, 230), 18: (43, 43, 4, 4, 250), 19: (44, 44, 4, 4, 270),
    20: (45, 45, 4, 4, 300),
    21: (47, 46, 4, 4, 320), 22: (47, 48, 4, 4, 350), 23: (49, 49, 4, 4, 370),
    24: (50, 51, 5, 5, 400), 25: (52, 52, 5, 5, 430), 26: (53, 54, 5, 5, 460),
    27: (55, 55, 5, 5, 500), 28: (56, 57, 5, 5, 530), 29: (58, 58, 5, 5, 560),
    30: (59, 60, 5, 6, 600),
    31: (61, 62, 6, 6, 640), 32: (63, 64, 6, 6, 670), 33: (65, 66, 6, 6, 710),
    34: (67, 68, 6, 6, 750), 35: (69, 70, 6, 7, 790), 36: (71, 72, 7, 7, 840),
    37: (73, 74, 7, 7, 880), 38: (75, 76, 7, 7, 930), 39: (77, 78, 7, 7, 970),
    40: (79, 80, 7, 8, 1020),
    41: (82, 82, 8, 8, 1070), 42: (84, 85, 8, 8, 1120), 43: (87, 87, 8, 8, 1170),
    44: (89, 90, 8, 9, 1220), 45: (92, 92, 9, 9, 1270), 46: (94, 95, 9, 9, 1330),
    47: (97, 97, 9, 9, 1390), 48: (99, 99, 9, 9, 1440), 49: (99, 99, 9, 9, 1500),
    50: (99, 99, 9, 9, 1560),
}

# Table rows known to sit above the HP accumulation formula, each by +10.
KNOWN_HP_DEVIATIONS = {3, 10, 31, 38, 47}
# The Might column runs 1 below strict alternation from this level on
# (converges again once both stats cap at 99 near level 48).
MIGHT_OFFSET_START = 22


def tier_of(level):
    return (level - 1) // 10 + 1


def abilities_range():
    return "1-4 unique abilities or aspects (per rpg_core_system.md)"


def round10_half_up(x):
    return int((x + 5) // 10 * 10)


def formula_hp():
    """HP per level from the stated accumulation formula, using the table's
    published MightMod per level. Returns {level: (raw, rounded)}."""
    out = {}
    raw = 20 + TABLE[1][2]
    for level in range(1, 51):
        if level > 1:
            raw += TABLE[level][2] + level
        out[level] = (raw, round10_half_up(raw))
    return out


def formula_stats():
    """Might/Magic per level from strict bump alternation. Returns {level: (m, g)}."""
    out = {}
    might, magic = 30, 30
    for level in range(1, 51):
        tier = tier_of(level)
        if tier == 1:
            if level % 2 == 1:
                might += 1
            else:
                magic += 1
        elif tier == 2:
            might += 1
            magic += 1
        elif tier == 3:
            if (level - 21) % 2 == 0:
                might += 2
                magic += 1
            else:
                might += 1
                magic += 2
        elif tier == 4:
            might += 2
            magic += 2
        else:
            if (level - 41) % 2 == 0:
                might += 3
                magic += 2
            else:
                might += 2
                magic += 3
        might, magic = min(might, 99), min(magic, 99)
        out[level] = (might, magic)
    return out


def print_block(level):
    m, g, mm, gm, hp = TABLE[level]
    print(f"Level {level}  (Tier {tier_of(level)})")
    print(f"  Might {m} (mod {mm})   Magic {g} (mod {gm})   HP {hp}")
    print(f"  Give it {abilities_range()} and an attack line")
    print(f"  (dice + the relevant mod + a damage type). Write the full block")
    print(f"  down BEFORE rolling initiative — gm_guide.md, 'Building a new monster'.")
    if level in KNOWN_HP_DEVIATIONS:
        print(f"  Note: this HP row is one of the five that sit +10 above the")
        print(f"  formula. It is canonical anyway. See --verify.")


def verify():
    ok = True
    hp = formula_hp()
    stats = formula_stats()

    print("=== HP: table vs accumulation formula ===")
    unexpected = []
    for level in range(1, 51):
        got = hp[level][1]
        want = TABLE[level][4]
        if got != want:
            known = level in KNOWN_HP_DEVIATIONS and want - got == 10
            tag = "known (+10)" if known else "NEW DEVIATION"
            if not known:
                unexpected.append(level)
            print(f"  L{level}: formula {got}, table {want}  <- {tag}")
    if not unexpected:
        print("  All other rows match. Known deviations accounted for:",
              sorted(KNOWN_HP_DEVIATIONS))
    else:
        ok = False

    print("\n=== Stats: table vs strict bump alternation ===")
    stat_bad = []
    for level in range(1, 51):
        fm, fg = stats[level]
        tm, tg = TABLE[level][0], TABLE[level][1]
        if fg != tg:
            stat_bad.append((level, "Magic", fg, tg))
        if fm != tm:
            expected_offset = level >= MIGHT_OFFSET_START and fm - tm == 1
            if not expected_offset:
                stat_bad.append((level, "Might", fm, tm))
    if stat_bad:
        ok = False
        for level, col, f, t in stat_bad:
            print(f"  L{level} {col}: formula {f}, table {t}  <- NEW DEVIATION")
    else:
        print(f"  Magic column matches everywhere. Might column runs exactly 1")
        print(f"  below alternation from L{MIGHT_OFFSET_START} until the 99 cap")
        print(f"  (the single missing bump at L{MIGHT_OFFSET_START}). This is the")
        print(f"  known state of the table.")

    print("\n" + ("VERIFY PASS — table matches its known state."
                  if ok else
                  "VERIFY FAIL — the table has drifted from its known state. "
                  "Someone edited rpg_core_system.md or this file. Reconcile "
                  "before using either."))
    return 0 if ok else 1


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 0
    if args[0] == "--verify":
        return verify()
    if args[0] == "--range" and len(args) == 3:
        a, b = int(args[1]), int(args[2])
        for level in range(a, b + 1):
            if level in TABLE:
                print_block(level)
                print()
        return 0
    try:
        level = int(args[0])
    except ValueError:
        print(f"Not a level: {args[0]}")
        return 1
    if level not in TABLE:
        print("Level must be 1-50. Beyond 50 there is no published table; that "
              "is new design work — see the campaign-advancement skill.")
        return 1
    print_block(level)
    return 0


if __name__ == "__main__":
    sys.exit(main())
