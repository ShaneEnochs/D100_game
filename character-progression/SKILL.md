---
name: character-progression
description: Handle everything that changes a character's numbers over time in the RPG project — leveling up, spending XP, buying or swapping skills and aspects, HP growth, tier changes, death penalties, and healing. Use this skill whenever a character levels, buys an ability, dies, or whenever XP, HP maximums, stat growth, or slot counts need to change on the character sheet.
---

# Character Progression

XP is one currency for two purchases: levels and abilities. Both deduct from
the pool; excess carries over. All thresholds and costs live in
`rpg_core_system.md` and `skills_and_aspects.md` — this skill is the
procedure and the traps.

## Leveling up — the procedure

Level-ups are manual; the player chooses when, any time the pool covers the
threshold.

1. **Confirm the threshold.** `xp_next_level` on the sheet must equal the XP
   table row for the current level (formula: previous threshold + current
   level × tier multiplier; multipliers 10/8/6/4/2 for tiers 1-5). The state
   validator checks this — if the sheet disagrees with the formula, fix the
   sheet first.
2. **Deduct.** `[XP: -<threshold>, pool now <n>]`. Level +1.
3. **Player picks one stat.** Then roll — through the roller, always:
   ```
   python3 dice_roller.py experience <current value of that stat>
   ```
   Above the stat → +1d4+1 (roller rolls it). At or below → +1. Cap 99. The
   asymmetry is deliberate: low stats grow fast, high stats crawl.
4. **Update the modifier** for that stat if it crossed a ÷10 boundary
   (mods round down). If Intellect's mod changed, recompute
   `skill_points_per_encounter = 2 + Intellect Mod`.
5. **HP: max += current Might Mod.** Locked in at this moment — **not
   retroactive**. A later Might increase improves future level-ups only.
   Never recompute past HP gains from the current modifier; that is why max
   HP cannot be derived from the sheet's stats alone above level 1.
6. **Tier boundary?** Levels 11/21/31/41 raise the tier and the slot
   ceilings (skills 2/3/4/5/6, aspects 1/2/3/4/5 by tier). Update `tier`.
7. **Set the new `xp_next_level`** from the table/formula.
8. Post the System line: `[Level <n> reached. <stat> <old> → <new>.]` and
   tag every changed number.

## Buying skills and aspects

- Cost = the XP threshold of the ability's required level (level 0 free,
  3 → 60, 5 → 150, 8 → 360, 10 → 550; higher levels per the core table).
- The catalog is `skills_and_aspects.md`. Check any stat requirements.
- **Slots are the constraint.** Equipping past the tier ceiling requires a
  swap, and a swapped-out ability is LOST — reacquiring it later costs full
  price again. Say this to the player before confirming a swap.
- Deduct XP, tag it, add the ability to the sheet with its full fields
  (`name`, `cost`, `stat`, `effect`, `level_req`), post the System line:
  `[Skill learned — <name>. <cost> XP spent, pool now <n>.]`
- Racial traits never occupy an aspect slot.

## Death

Respawn at a respawn point. Lose half the XP pool, **rounded down**. Keep
the level, all loot, and all purchased skills and aspects. Tag it:
`[Death. XP pool 47 → 23.]` Nothing else on the sheet changes from dying.

## Healing (out of level-up context)

- Full rest → full heal.
- Healing skills → their text, costs skill points and the action.
- Potions → fraction of MISSING HP, rounded down (Minor 1/4, Healing 1/2,
  Greater all); one tier below the drinker halves the effect, two or more
  tiers below does nothing. Takes the action; anyone can drink one.
- Active ruling: HP resets between TRAINING encounters (session-1 ruling).
  Real field damage heals only by the means above.

## After any change

Run the validator before considering the work done:

```
python3 .claude/skills/state-management/scripts/validate_state.py character_sheet.json campaign_state.json
```

It checks modifiers, thresholds, tier, slots, skill point math, and ability
level requirements against the rules. A sheet that fails validation does not
get delivered.
