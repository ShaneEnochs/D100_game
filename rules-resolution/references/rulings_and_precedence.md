# Rulings and Precedence Ledger

Every known place where two project files overlap or where the text needed a
ruling, with the governing answer. Verified against the files as of
2026-07-02. Updated with balance rebalance rulings 2026-07-03. When a new
overlap or ruling appears, add it here in the same format: what the texts
say, which governs, why.

## File overlaps — settled

### 1. Power Strike damage: +1d4, not +1d6

`rpg_core_system.md` lists Power Strike under "Example Skills" with +1d6.
`skills_and_aspects.md` (the operative catalog) and the live character sheet
both say +1d4. **The catalog governs.** The core system's skill list is
explicitly labeled examples; the catalog is the purchasable inventory. The
same logic applies to Arc Bolt, Analyze Weakness, and Commanding Voice — use
the catalog's wording, costs, and numbers, never the core file's example
versions.

### 2. Armor model: three physical DR types + magic penalty

`rpg_core_system.md` says armor has "a physical DR and a magic DR rating."
`equipment.md` replaces this with the operative model: separate DR for blade,
piercing, and blunt, plus a **magic penalty** that ADDS damage when the wearer
is hit by magic ("Max" = the spell's maximum possible damage, no roll).
**equipment.md governs.** The character sheet's armor object
(blade_dr/piercing_dr/blunt_dr/magic_penalty) confirms it. There is no
"magic DR" on armor in this game.

### 3. Skill economy: skill points, not per-skill cooldowns

`rpg_core_system.md` describes per-skill cooldowns (no cooldown / X rounds /
once per encounter). `skills_and_aspects.md` replaces this with the operative
economy: a per-encounter pool of skill points (1 + Intellect Mod + Tier),
costs of 1/2/3 points, basic attacks free, pool resets at combat end.
**The catalog governs.** What survives from the cooldown text: 3-point skills
are once per encounter, and aspects with encounter limits (Second Wind) keep
them. If a future ability needs an X-round cooldown, that is new design —
log it as a ruling first.

### 4. Ability XP costs: the catalog's table extends the core's

The core system prices abilities at the XP threshold of their required level
and lists thresholds in 5-level steps. `skills_and_aspects.md` adds the
level 3 (60 XP) and level 8 (360 XP) rows the Tier 1 catalog uses, and now
extends through all five tiers with four bands per tier (0/3/5/8, 10/13/15/18,
20/23/25/28, 30/33/35/38, 40/43/45/48). No conflict — same rule, finer table.
Cost of any ability = XP threshold of its required level, from the core XP
table.

### 5. Monster tables vs their own formulas

The published stat tables in `rpg_core_system.md` are canonical — but they do
not perfectly match the generative rules printed beside them. Verified by
script (`monster-building/scripts/statblock.py --verify`):

- Five HP rows sit exactly +10 above the accumulation formula: levels **3,
  10, 31, 38, 47**.
- The Might column from level **22** onward runs 1 point below strict bump
  alternation (one Might bump missing at 22), converging again at the 99 cap.

**The tables govern play.** Do not silently regenerate them from the formula,
and do not trust the formula alone when extending past the tables. Any
deliberate correction is a rules change: log the ruling, edit the file, and
update `statblock.py`'s embedded table and known-deviations list together.

### 6. Weapon attack stats

`equipment.md` governs: physical weapons and bows use Might; **crossbows and
clockwork devices use Intellect and deal flat dice with no modifier**;
**magi-tech weapons use Magic and deal flat dice with no modifier** (closed
from TBD as of 2026-07-03, costs 1 E-stone of fuel per encounter of use).
The core system's blanket "all physical weapon attacks use Might" predates
the mechanical-weapon and magi-tech categories.

### 7. Skill point formula

`rpg_core_system.md` said `2 + Intellect Mod`.
`skills_and_aspects.md` now says `1 + Intellect Mod + Tier`.
At Tier 1 the results are identical (Bill Locke: 1 + 3 + 1 = 5). The catalog
governs; the core system has not been updated with the new formula text (it
delegates to the catalog). `validate_state.py` must use the new formula.

## Rulings made in play — binding

From session 1 (recorded in `session_1_notes.md`):

1. **Training spars award no XP.**
2. **HP resets between training encounters.** (Real injuries outside training
   heal by the normal rules: full rest, healing skills, potions.)
3. Communication: banned-phrase additions were folded into `gm_guide.md`
   Part 4. Part 4 is the living list — follow the file, not memory.

## Rulings from the skills rebalance (2026-07-03) — binding

These were logged in `campaign_state.rulings` and promoted into the rules
files in the same change.

**R1 — Reactions.** Any skill tagged *Reaction* (Parry, Mana Shield, Ward
Other, Riposte, and future reaction skills) is declared in response to an
incoming attack. One reaction per round. Reactions do not cost your action.
You cannot use a reaction in a round in which you took the Dodge action.
Added to `rpg_core_system.md` under Combat > Reactions.

**R2 — Action denial cap.** Any effect that costs a creature its action
(stun, knockdown recovery, lost action) allows a resist check — Might for
physical effects, Magic for magical or mental ones — unless the ability text
says otherwise. A creature can lose at most one action per round to such
effects, no matter how many land. Added to `rpg_core_system.md` under
Combat > Action Denial and to `ability_design.md`.

**R3 — Out-of-combat skill use.** Outside combat, using a skill spends
points from your next encounter's pool. The pool refills on a full rest.
Added to `skills_and_aspects.md` under Skill Points.

**R4 — Swap timing.** Skills and aspects can be swapped only during a full
rest with System access. Updated in `rpg_core_system.md` and
`skills_and_aspects.md`.

**R5 — "Ally" includes you.** Any skill targeting "an ally" or "allies" can
target the user, unless the skill's own text excludes it (Heal Other, Ward
Other, Perfect Timing). Added to `skills_and_aspects.md` under Ally
Targeting.

**R6 — Social skills vs creature types.** Social combat skills work on any
creature capable of fear or morale, beasts included. Constructs, undead,
mindless creatures, and creatures tagged Feral are immune. Added as a header
line in the Social Skills section of `skills_and_aspects.md`.

**R7 — Critical hit effect.** A critical hit on an attack deals maximum
damage dice (no roll). Add modifiers normally. Added to `rpg_core_system.md`
under Critical Successes.

**R8 — Skill point formula.** `1 + Intellect Mod + Tier` replaces
`2 + Intellect Mod`. At Tier 1 this produces the same values; at higher
tiers the pool grows to support larger slot counts and longer fights. Updated
in `skills_and_aspects.md`. `validate_state.py` formula must be updated.

**Dodge action.** Attackers roll at Difficult (-15). Costs your action.
Excludes reactions for that round per R1. Updated in `rpg_core_system.md`.
Moved from the open list.

**Second Wind repricing.** Level_req changed from 0 to 3 (60 XP). Bill
Locke's copy was acquired at creation under old pricing — no retroactive
charge. Updated on the character sheet with a note field.

## Open points — rule at the table, log the ruling

- **Mana stone drops.** Infernals drop mana stones; drop rate and grade per
  creature are not codified. Practice so far: grade tracks the creature's
  tier (Tier 1 infernals drop E/F-grade). Rule per encounter, log patterns,
  promote a table when one emerges.
- **Monster skill points.** Monsters have abilities but no printed skill
  point economy. Practice: monster abilities are usable per their own text
  (most read as at-will or once-per-encounter); do not give monsters a point
  pool unless a ruling creates one.

## The precedence ladder (restated)

1. Live state files → 2. Logged rulings → 3. Specialized rules files
(equipment, skills_and_aspects, price_list, bestiary) → 4. rpg_core_system.md
→ 5. gm_guide.md (procedure) → 6. Notes, world file, module (narrative; never
a number).
