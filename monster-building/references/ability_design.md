# Ability Design Conventions

Derived from the forty published entries in `bestiary_levels_1_5.md`. New
creatures should read like they came from the same field guide.

## The grammar

Abilities are one to three sentences, mechanical, and use the system's own
check language. Patterns that appear across the published entries:

- Saves: "must pass a Might check (Easy) or take 1d4 poison damage" /
  "or become poisoned: -10 on all rolls until they rest."
- Riders: "the target takes 1d4 additional damage at the start of its next
  turn."
- Action taxes: "must spend their action to get up" / "loses its next
  action."
- Flat DR: "1 DR against all physical damage types."
- Conditional healing: "If it does not move on its turn, it heals 2 HP."
- Senses: "Cannot be snuck up on while touching the ground."
- Surprise: "If it attacks from underground, it gets a surprise round."
- Target priority: "Prioritizes targets below half HP."

Keep numbers in these bands at Tier 1: rider/secondary damage 1 to 1d4,
ability DR 1-2, roll penalties -10 to -15, durations 1-2 rounds or
"until they rest." Bigger numbers are a Tier 2 design decision.

## Ability count carries the threat

The base block is identical for every creature at a level. Differentiate by
count and kind:

- 1-2 abilities → nuisance or swarm member (Sludge Rat, Bone Beetle).
- 3 abilities → a proper predator (typical of the 3-5 tag).
- 4 abilities → a leader creature or a set-piece threat.

Pick abilities that express the creature's fiction: an ambusher gets a
surprise mechanic and a sense; a fortress creature gets DR and a rooted
heal; an infernal gets something that touches the portal/mana layer.

## Infernal tags

Mark extra-planar creatures *(Infernal)*. Infernals connect to the invasion
mechanics: they drop mana stones, they come through portals, and portal
creatures may carry reinforcement mechanics (the Rift Whelp's Portal Tether
pattern — an open portal replaces losses, so objective play beats
attrition). Any new portal creature should say what the open portal does
for it.

## Full entry format (for the bestiary file)

Match the published section order exactly:

```
## <n>. <Name> [*(Infernal)* if applicable]

**Typically level <a>-<b>**

**Classification:** <Beast/Flora/Construct/Undead/Infernal> — <subtype>

**Habitat:** <where it lives, plainly>

**Behavior:** <2-3 paragraphs: how it acts, why, what a nest/group looks like>

**Identifying signs:** <what a hunter sees before contact>

**Tactical notes:** <field advice a lieutenant would give recruits>

- **Attack:** <name> — <dice> + <Might|Magic> Mod (<damage type>)
- **<Ability>** — <mechanical text>
- **<Ability>** — <mechanical text>
```

Voice check: the guide is written as hunter doctrine — factual, practical,
no jokes, no archaisms. Every Behavior section should teach the counter-play
that Tactical notes then states outright.

## Encounter-facing block (for play, per gm_guide)

Before initiative, write down the working block:

```
<Name> — Level <n> (Tier <t>)
Might <x> (mod <a>) / Magic <y> (mod <b>) / HP <z>
DR: <from abilities, by type, or none>
Attack: <dice + mod, type>
Abilities: <the 1-4, one line each>
```

Numbers come from `scripts/statblock.py <level>`, never from memory.
