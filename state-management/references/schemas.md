# State File Schemas

Field-by-field, with invariants. "Derived" fields must always be recomputed
when their source changes — the validator enforces the marked ones.

## character_sheet.json

| Field | Type | Rules |
|---|---|---|
| `name`, `race`, `class` | string | Race is one of the five playable races; class is flavor plus the creation-time +10 to one stat. |
| `level` | int | 1-50. |
| `tier` | int | **Derived:** (level-1)//10 + 1. |
| `xp_pool` | int | ≥ 0. Spent by level-ups and ability purchases; halved (rounded down) on death. |
| `xp_next_level` | int | **Derived** from the XP table for the current level (formula: prev + level × tier multiplier; multipliers 10/8/6/4/2). |
| `stats` | object | `might`, `intellect`, `magic`, `social`, each 1-99. Start 30 each +10 from class. |
| `modifiers` | object | **Derived:** `<stat>_mod` = stat ÷ 10 rounded down. |
| `hp.current` | int | 0 ≤ current ≤ max. |
| `hp.max` | int | Level 1: exactly 20 + Might Mod. Above level 1: historical — each level-up added the Might Mod current AT THAT MOMENT; not recomputable from today's stats. Preserve it; never rebuild it from the modifier. |
| `skill_points_per_encounter` | int | **Derived:** 2 + Intellect Mod. |
| `skills` | array | Each: `name`, `cost` (1/2/3), `stat`, `effect`, `level_req`. Count ≤ tier's skill slots (2/3/4/5/6). `level_req` ≤ level. Text comes verbatim from skills_and_aspects.md. |
| `aspects` | array | Each: `name`, `effect`, `level_req`. Count ≤ tier's aspect slots (1/2/3/4/5). |
| `racial_trait` | string | The race's passive. Occupies NO aspect slot. |
| `equipment.weapon` | object | `name`, `damage_type`, `damage` (dice + which mod), `category`. From equipment.md. |
| `equipment.armor` | object | `name`, `blade_dr`, `piercing_dr`, `blunt_dr`, `magic_penalty` ("None", "+n magic damage", or "Max"), `category`. |
| `equipment.shield` | object or null | Shield DR adds to all physical types; occupies a hand. |
| `equipment.other` | array | Free-text inventory lines. |
| `currency.credits` | int | ≥ 0. |
| `currency.mana_stones` | array | Stone entries as held (grade + count in whatever shape play established). E=10cr, each grade ×10 up to S. |
| `rank`, `detachment`, `lieutenant`, `notes` | string | Organization position and free notes. |

## campaign_state.json

| Field | Type | Rules |
|---|---|---|
| `current_to` | string | `session-<n>`, the last COMPLETED session. Must agree with `session_count`. |
| `session_count` | int | Count of completed sessions. |
| `campaign`, `act`, `phase` | string/int | Position in the module. Acts advance on discoveries (see campaign-advancement), never on dates. |
| `location`, `time` | string | Where and when the fiction stands. |
| `resume_point` | string | Non-empty. The exact opening situation for the next session — specific enough to open from with two lines. |
| `active_quests` | array | Open quests only. Completed quests LEAVE this list at close and live on in the session notes. |
| `completed_quests` | array | Optional archive of names. |
| `npc_knowledge` | object | Keyed by NPC id. Each entry: `knows` (list of plain factual sentences), `does_not_know` (list; the load-bearing negatives worth guarding). This object is the anti-leak mechanism — an NPC knows ONLY what is listed. Update after every conversation via the session's knowledge deltas. Track hostile actors here too (Kade reacts only to what he can observe). |
| `world_flags` | object | Background truths advancing off-screen (tithe activity, front status, fort awareness). The GM advances these at closes per the module's clocks. |
| `rulings` | array | Every table ruling, one string each. Promote recurring ones into the rules files between sessions; leave the entry in place with a note when promoted. |
| `meta` | object | Standing player approvals (world, pay/gear, names). Do not re-litigate approved items. |

## Session notes files (`session_<n>_notes.md`)

Not machine-validated; structure is contract. Sections, in order: Header ·
What Happened · NPC Knowledge Deltas · Sheet Changes · Rulings ·
Next-Session Prompt. `session_1_notes.md` is the canonical example. The
Next-Session Prompt must let a cold session open play in two lines — write
it for a reader with no memory of tonight.
