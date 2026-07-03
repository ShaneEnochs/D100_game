# Content Templates and Number Anchors

## Bestiary entry

Use the full format in `monster-building/references/ability_design.md` (that
file owns creature design). Number the entry after the last one in the file
and keep the level tag honest to the abilities you gave it.

## Weapon

```
| <Name> | <Blade/Blunt/Piercing> | <dice> + Might Mod | <price> credits |
```

Bands from equipment.md: simple melee 1d4-1d6, no requirement, 15-80cr;
martial melee 1d8-2d6, requires 40 Might, 500-800cr; bows 1d6-1d8 on Might;
crossbows on Intellect, FLAT dice, no mod; magi-tech on Magic, FLAT dice,
no mod, 1 E-stone fuel per encounter. A new category (whips, thrown) is a
rules addition — define its attack stat and mod rule explicitly and log the
ruling.

Tier 2+ weapon dice anchors (see equipment.md "Tier Weapon and Armor
Anchors"): T2 ~2d6-2d8, T3 ~3d6-3d8, T4 ~4d8-4d10, T5 ~6d8-6d10. Prices
follow the ×10-per-tier curve.

## Armor

```
| <Name> | <blade> | <piercing> | <blunt> | <magic penalty> | <price> |
```

The published progression: DR totals rise with weight class, magic penalty
rises with metal coverage (None → +1 → +2 → +3 → Max), requirements None /
40 Might / 60 Might. Keep new armor on that curve; a heavy armor without a
magic penalty breaks the tradeoff the table is built on.

## General item pricing

Anchors from price_list.md: 1 credit ≈ 1 USD; basic meal 5-10; bunk 20-30 a
night; low-wage day 60-80; skilled tradesperson 150-250 a day; mana-tech =
3× the conventional version; round to nearest 5 or 0. Sanity test: state the
item's nearest published neighbor and why the new price sits where it does.

## Skill (active ability)

```
**<Name>** — <1|2|3> point[s][, once per encounter]. <Stat> <attack|check>.
<Effect in one or two sentences using existing grammar.>
```

### Tier band structure

Four bands per tier. XP costs come from the core formula. Point costs stay
1/2/3 at every tier; every 3-point skill is once per encounter, at every
tier, no exceptions.

| Tier | Bands (required level) | XP costs |
|---|---|---|
| 1 | 0 / 3 / 5 / 8 | 0 / 60 / 150 / 360 |
| 2 | 10 / 13 / 15 / 18 | 550 / 838 / 1,070 / 1,478 |
| 3 | 20 / 23 / 25 / 28 | 1,790 / 2,186 / 2,480 / 2,966 |
| 4 | 30 / 33 / 35 / 38 | 3,320 / 3,704 / 3,980 / 4,424 |
| 5 | 40 / 43 / 45 / 48 | 4,740 / 4,992 / 5,170 / 5,452 |

Old skills stay usable and cheap — a Tier 3 character spamming Power Strike
is paying 1 point for +1d4, which is its own obsolescence curve. No sunset
rules needed.

### Damage and effect bands per tier

These assume the published HP tables. If a future HP rebalance is adopted,
revisit Tier 3+ bands.

| Tier | 1-pt attack rider / spell | 2-pt band | 3-pt capstone | Heals | Roll penalties/bonuses | Ability DR |
|---|---|---|---|---|---|---|
| 1 | +1d4 / 1d8+Mod | +1d8, multi 1d6 | 2d8 | 1d6–2d8 | ±10 to ±15 | 1–3 |
| 2 | +2d6 / 2d8+Mod | +2d8, multi 2d6 | 4d8 | 2d6–4d6 | ±10 to ±15 | 2–4 |
| 3 | +3d6 / 3d8+Mod | +3d8, multi 2d8 | 6d8 | 3d6–6d6 | ±15 | 3–5 |
| 4 | +4d8 / 4d10+Mod | +4d10, multi 3d8 | 8d10 | 4d8–6d8 | ±15 | 4–6 |
| 5 | +6d8 / 6d10+Mod | +6d10, multi 4d10 | 10d10 | 6d8–8d8 | ±15 to ±20 | 5–8 |

## Aspect (passive)

```
**<Name>** *(Level <n> — <cost> XP)* — <passive effect: a +10/+15
conditional bonus, a small DR, a resource tweak, or an automatic trigger
with a per-encounter limit>.
```

The catalog's power band: +15 on a defined slice of one stat's rolls is the
standard shape; automatic triggers (Second Wind) carry once-per-encounter
limits; economy tweaks (Mana Well) have floors. An always-on unconditional
stat bonus is out of band.

Aspect level requirements (so aspects participate in the XP economy):

| Tier | Typical level bands | XP cost range |
|---|---|---|
| 1 | 0, 3, 5, 8 | 0–360 |
| 2 | 10, 13, 15, 18 | 550–1,478 |
| 3 | 20, 23, 25 | 1,790–2,480 |
| 4 | 33, 35 | 3,704–3,980 |
| 5 | 45, 48 | 5,170–5,452 |

## Quest (module section 5 format)

```
**S-<n>. <Name>** (<level or range>[, availability gate]) — <Hook: how it
arrives. Truth: what is really going on. Beats if non-obvious.> <Reward per
the price list.> *Spine:* <none | the connection, stated plainly>.
```

Board quests post in System voice when accepted:
`[Quest: <Name> — <objective>. Reward: <reward>.]`
Character quests do not post until the character agrees to help.
