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
crossbows on Intellect, FLAT dice, no mod. A new category (whips, thrown,
magi-tech) is a rules addition — define its attack stat and mod rule
explicitly and log the ruling. Magi-tech weapon damage is an open design
task; whoever builds it defines the Magic-stat damage rule and updates
equipment.md's TBD.

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

Bands (Tier 1 catalog): level 0 = bread and butter (1 point, ~1d4-1d8
effects); level 3 = tactical (mostly 2 points); level 5 = strong control or
multi-target; level 8 = 3 points, once per encounter, fight-changing (2d8
band). Cost = the level's XP threshold: 0/60/150/360 for 0/3/5/8. Every
3-point skill is once per encounter — no exceptions in the catalog, keep it
that way.

## Aspect (passive)

```
**<Name>** — <passive effect: a +10/+15 conditional bonus, a small DR, a
resource tweak, or an automatic trigger with a per-encounter limit>.
```

The catalog's power band: +15 on a defined slice of one stat's rolls is the
standard shape; automatic triggers (Second Wind) carry once-per-encounter
limits; economy tweaks (Mana Well) have floors. An always-on unconditional
stat bonus is out of band.

## Quest (module section 5 format)

```
**S-<n>. <Name>** (<level or range>[, availability gate]) — <Hook: how it
arrives. Truth: what is really going on. Beats if non-obvious.> <Reward per
the price list.> *Spine:* <none | the connection, stated plainly>.
```

Board quests post in System voice when accepted:
`[Quest: <name> — <objective>. Reward: <reward>.]`
Character quests do not post until the character agrees to help.
Rewards: village board work at these levels pays 150-400cr (published
band); Organization commissions 100-300cr per verified site. XP always
comes from kills per the core rules, never as a quest line item.

## NPC

The world file's pattern: name, race, sex/age, role, two or three sentences
of who they are and how they behave, one thing that makes them useful or
difficult in play. Then — before they appear in a session — create their
`npc_knowledge` entry in the campaign state, starting from ignorance.
Dialogue rules from gm_guide Part 4 apply to every line they will ever say.

## Lore / world material

Match the world file's register: plain declarative description, no live
numbers (numbers live in state files and rules files), and a note of what is
proposal versus established. New world material is a draft until the player
approves it.
