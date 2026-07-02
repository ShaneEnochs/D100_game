# Worked Examples

Full resolutions with the exact commands. Dice values shown are illustrative;
in play, the roller's actual output is the result. Character numbers use Bill
Locke's current sheet (Might 40 / mod 4, spear 1d6+Might Mod piercing, leather
armor 1/1/1, skill points 5).

## 1. A melee exchange with DR

Bill (Might 40) attacks a Briar Hound (level 2 → Might 31, from
`statblock.py 2`). An attack is an opposed roll:

```
python3 dice_roller.py opposed 40 31
```

Say Side A rolls 22 (success, margin +18), Side B rolls 60 (failure). Side A
wins — the hit lands. Damage:

```
python3 dice_roller.py damage 1d6+4
```

Result 8. The Hound has no armor, so it takes 8. `[Hound HP: 30 → 22]`

The Hound bites back on its turn (bite 1d4 + Might Mod, piercing):

```
python3 dice_roller.py opposed 31 40
```

If the Hound wins, roll `damage 1d4+3`, say 6, minus Bill's piercing DR 1 →
5 damage. `[HP: 24 → 19]`

## 2. Difficulty and stakes stated up front

Bill wants to climb a crumbling wall under fire. Before the roll: "Might,
Difficult (-15). Success: you're on the parapet. Failure: you fall, 1d6
blunt, and you're prone in the open." Then:

```
python3 dice_roller.py check 40 difficult
```

Target is 25. The roller prints the math; read its verdict.

## 3. Critical vs critical

Both sides of an opposed roll crit (rolls 1-5, or margin 50+). Compare
margins normally; ties go to the defender. The roller already prints the
winner — do not re-adjudicate its output.

## 4. Skill points in an encounter

Bill has 5 points per encounter. Round 1: Power Strike (1 point, 4 left) —
opposed attack, on a hit `damage 1d6+4` then `damage 1d4` extra (or roll
`1d6+1d4+4` as one expression). Round 3: Mend (1 point, 3 left) — 
`check 30` on Magic; on success `damage 1d6+3` worth of healing, capped at
max HP. Basic spear attacks all fight long cost nothing. Pool resets when
combat ends.

## 5. Second Wind (aspect, automatic)

Bill is at 13/24 and takes 8 → 5, below half. Second Wind triggers by
itself, once per encounter, no action, no points:

```
python3 dice_roller.py roll 1d6
```

Heal that much. `[HP: 5 → 9]`. Tag the trigger so it is not reused this
encounter.

## 6. A potion

Bill at 6/24 drinks a Minor healing potion (Tier 1): missing HP is 18, a
quarter of 18 is 4.5, round down → heal 4. `[HP: 6 → 10]`. Takes his action.
If a Tier 2 character drank a Tier 1 Minor, halve the result again (round
down). Two tiers down: no effect.

## 7. XP from a kill

The five-recruit team kills a level 2 Briar Hound. Every member gains 2 XP —
XP is not split. `[XP: +2, pool now 2]` for each. A level 11 character in the
same fight gains 0 — the kill is outside their tier.

## 8. A level-up, end to end

See `character-progression/SKILL.md` for the full procedure. The dice part:

```
python3 dice_roller.py experience 40
```

Roll above 40 → the stat gains 1d4+1 (the roller rolls and prints it). Roll
at or below → +1. Low stats grow fast; high stats crawl. Cap 99.

## 9. Magic against armor

A caster hits a target in Scale Mail (magic penalty +2) with Arc Bolt:
`damage 1d8+<Magic Mod>`, then ADD 2. Against Full Plate ("Max"): no damage
roll — the spell deals its maximum (die maximum + modifier).

## 10. Surprise and initiative

Ambushers act once before initiative. Then:

```
python3 dice_roller.py initiative Bill Hound1 Hound2
```

Highest first; the roller re-rolls ties; order stays fixed for the fight.
