---
name: rules-resolution
description: Adjudicate rules for the RPG project — checks, opposed rolls, criticals, combat, damage and DR, skill points, potions, XP math, and every case where two project files appear to disagree. Use this skill whenever a rules question comes up in play or in development, whenever a mechanic needs to be resolved, whenever files seem to conflict, and before ruling on anything the rules text does not cover. Also use it when reviewing past sessions for mechanical errors.
---

# Rules Resolution

The rules live in the project files. This skill tells you how to apply them
correctly, which file wins where they overlap, and how to rule where the text
is silent. Two reference files carry the depth:

- `references/rulings_and_precedence.md` — the known overlaps between files,
  which text governs, and the rulings already made in play. **Read this before
  declaring any conflict or making any ruling.** Most "conflicts" are already
  settled there.
- `references/worked_examples.md` — full worked resolutions with the exact
  dice roller commands. Read it before running your first combat, and any time
  a resolution feels uncertain.

## The one mechanic

Everything is a d100 roll-under against one of four stats (Might, Intellect,
Magic, Social) after a difficulty modifier: Very Easy +30, Easy +15, Normal 0,
Difficult -15, Very Difficult -30. Roll at or under the modified stat to
succeed. Margin = modified stat minus roll. Critical success: roll 1-5, or
success by margin 50+. There are no critical failures, and a roll of 100
always fails and never crits.

Every roll goes through the roller:

```
python3 dice_roller.py check <stat> [difficulty]
python3 dice_roller.py opposed <stat_a> <stat_b> [diff_a] [diff_b]
python3 dice_roller.py damage <expr>
python3 dice_roller.py experience <stat>
python3 dice_roller.py initiative <name> <name> ...
python3 dice_roller.py roll <expr>
```

Do not roll by hand, do not write a one-off script, do not narrate a result
without running the command. Ad-hoc scripts produced wrong results in past
campaigns — missed criticals, wrong difficulty math. The roller has the tested
rules and prints the full resolution; its output is the result.

## Resolution quick paths

**Simple check.** State the stat, difficulty, and both outcomes before the
player commits (hidden information excepted). Run `check`.

**Opposed roll** (attacks, contests). Run `opposed`. Rules: one success wins;
both succeed → higher margin; crit beats non-crit; both fail → defender;
tie → defender. The roller applies all of this — read its verdict line.

**Attack and damage.** Attacker's stat (Might for weapons and bows, Intellect
for crossbows, Magic for spells) opposed against the defender. On a hit:
weapon/spell dice + the attacker's modifier (mods = stat ÷ 10, rounded down;
crossbows deal flat dice, no mod). Subtract the defender's DR of the matching
damage type — blade, piercing, or blunt for physical, the armor's magic
penalty ADDS damage for magical hits. Shields add their DR to all physical
types. Damage floors at 0.

**Multiple attackers on one target.** The defender rolls a separate opposed
check against each attack, on each attacker's turn.

**Skill use.** Check the skill's point cost against the user's remaining
pool (2 + Intellect Mod per encounter; basic weapon attacks are free; pool
resets when combat ends). 3-point skills are once per encounter. Then resolve
the skill's stated check and effect.

**Potions.** Heal a fraction of MISSING HP, rounded down: Minor 1/4, Healing
1/2, Greater all of it. One tier below the drinker: half effect. Two or more
tiers below: nothing.

**XP.** Kill grants XP equal to the creature's level, full value to every
party member, minimum 1, round decimals up, and only for kills within the
character's own tier — above or below tier grants zero.

## Where the text is silent

Do not freeze and do not invent a permanent rule mid-scene. Procedure:

1. Pick the most relevant stat and a difficulty that fits reality, say so
   plainly, and roll. The core system's GM guidance endorses exactly this.
2. If the call would recur (a new condition, an uncovered interaction), log it
   as a ruling: append to `campaign_state.rulings` and record it in the
   session notes' Rulings section.
3. Recurring rulings get promoted into the proper rules file between sessions
   — a deliberate edit with a trail, never a silent one. If the Rulings
   section keeps growing, the core system has a gap to patch; say so.

## Rounding conventions (memorize these)

- Stat modifiers: divide by 10, round **down**.
- XP from kills: round **up**, minimum 1.
- Death penalty: lose half the XP pool, rounded **down** (keep level, loot,
  purchased abilities; respawn at a respawn point).
- Potion healing: fraction of missing HP, rounded **down**.
- Monster HP tables: nearest 10 (already baked into the published tables).
- Prices: nearest 5 or 0.
