# Skill Library — RPG Campaign Project

This library exists so that any future session — a junior engineer, a smaller
model, anyone — can run, debug, extend, and validate this project at the
standard it was built to. The project files hold the rules and the state; the
skills hold the procedures, the verified tooling, and the tribal knowledge
that is written down nowhere else.

Built and verified against the project files as of 2026-07-02 (session 1
complete, character Bill Locke at level 1).

## Route by task

| You are asked to... | Use |
|---|---|
| Run a play session, open or close one, GM anything | `running-sessions` |
| Resolve a rule question, adjudicate an edge case, settle a conflict between files | `rules-resolution` |
| Level a character up, buy a skill/aspect, apply death, heal, spend XP | `character-progression` |
| Stat a monster, run an encounter against a new creature | `monster-building` |
| Edit, validate, or rebuild the JSON state files; write session notes; deliver files | `state-management` |
| Write new creatures, items, skills, quests, prices, or lore | `content-authoring` |
| Modify, debug, or extend `dice_roller.py` | `dice-roller-engineering` |
| Advance the campaign between acts, build what Act 3/4 needs, pace the plot | `campaign-advancement` |

## The precedence ladder

When sources disagree, resolve in this order (gm_guide.md Part 8, extended):

1. **Live state files** — `character_sheet.json`, `campaign_state.json`. The truth about current numbers and situation.
2. **Logged rulings** — `campaign_state.rulings` and the Rulings sections of session notes. Table law until promoted into a rules file.
3. **Specialized rules files** — `equipment.md`, `skills_and_aspects.md`, `price_list.md`, `bestiary_levels_1_5.md`. These refine and supersede the core system wherever they overlap. The known overlaps are catalogued in `rules-resolution/references/rulings_and_precedence.md` — read that file before declaring any two files "in conflict."
4. **`rpg_core_system.md`** — the base rules.
5. **`gm_guide.md`** — procedure and conduct. It does not carry numbers.
6. **Session notes, `world_fort_easy_dawn.md`, the campaign module** — narrative record and lore. Never override a number.

## The standard

A session or task is done when all of these hold:

- Every mechanical roll went through `python3 dice_roller.py`. No ad-hoc scripts, no narrated results. This rule has a history; see `rules-resolution`.
- Every number that moved was tagged in-line at the moment it moved: `[HP: 23 → 18]`.
- New rulings were logged in `campaign_state.rulings` and the session notes.
- `validate_state.py` passes on both JSON files before delivery.
- `statblock.py --verify` passes if the monster tables were touched.
- Changed files were copied to the outputs directory and presented for download. Work the player cannot download did not happen.
- No rule was edited silently. A rule change is a ruling first, a file edit second, and both leave a written trail.

## Maintenance of this library

When a project file changes in a way that invalidates a number or claim in a
skill, update the skill in the same piece of work and note the date. The
scripts embed rule tables deliberately (so they can detect drift); if the
tables in `rpg_core_system.md` are ever intentionally changed, update
`statblock.py` and `validate_state.py` to match, and log the ruling that
authorized the change.
