---
name: state-management
description: Read, edit, validate, and deliver the RPG project's live state — character_sheet.json, campaign_state.json, and session notes files. Use this skill whenever a session closes, whenever either JSON file needs editing, whenever session notes get written, whenever files must be delivered to the player, and whenever state and notes disagree and need reconciling.
---

# State Management

The two JSON files are the truth of the campaign. Everything here protects
that truth: schemas, the close-of-session sequence, validation, delivery.
Field-by-field schemas live in `references/schemas.md` — read it before the
first edit of either file.

## Ground rules

- The project directory is read-only in a session. Edit working copies, then
  deliver them to the outputs directory for the player to upload back. The
  project updates when the player uploads — not before.
- State files outrank everything: save points, session notes, and memory of
  play all yield to them. If they are wrong, fix them openly and tell the
  player.
- Never hand-edit a derived field to "make it look right." Modifiers, tier,
  `xp_next_level`, and skill points are all derivable; if one is off, find
  which underlying number moved and reconcile from there.

## Close-of-session — the full sequence (gm_guide Part 7)

1. **Rewrite the character sheet** from the last save point plus every
   `[tag]` logged after it. Update every field that moved and every derived
   field it drags along (stat → modifier → skill points; level → tier →
   slots → xp_next_level).
2. **Rewrite the campaign state**: advance quests (completed ones leave the
   active list — they live in the notes now), update `npc_knowledge` for
   every NPC encountered (knowledge deltas from play), append new rulings to
   `rulings`, write a clean `resume_point`, bump `session_count` and
   `current_to` to the session just played.
3. **Write the session notes file** (`session_<n>_notes.md`) with the exact
   published structure: header (name, session, date, open/close locations,
   one-line start and end states) · What Happened (numbered beats) · NPC
   Knowledge Deltas (per NPC: now knows / still does not know / attitude) ·
   Sheet Changes · Rulings · Next-Session Prompt (where, condition, pending,
   active quests, options, one line of in-fiction orientation). Session 1's
   file is the model — match it.
4. **Validate:**
   ```
   python3 .claude/skills/state-management/scripts/validate_state.py <character.json> <campaign.json>
   ```
   Then read the notes' end state against the sheet yourself — the script
   checks internal consistency, only a human read catches a beat the tags
   missed. Fix every error before step 5.
5. **Deliver.** Copy every changed file to the outputs directory and present
   them: character sheet, campaign state, and the new notes file, always.
   Tell the player to upload them back into the project. The session is not
   closed until the player has downloadable files.

## What the validator checks (and what it cannot)

Checks: JSON parses; required keys; stats 1-99; modifiers = stat÷10 rounded
down; level/tier agreement; `xp_next_level` against the XP formula; HP sanity
(and the exact level-1 max); skill points = 2 + Intellect Mod; slot ceilings
by tier; ability shapes and level requirements; session numbering; NPC
knowledge entry shapes; quest lists; rulings list.

Cannot check: whether the content is TRUE to play — an NPC entry that omits
something the player said, a quest step that did not advance. That is the
step-4 human read of the notes.

## Reconciliation (start-of-session step 5, or any drift)

When notes and state disagree: state wins. Announce the discrepancy to the
player, correct whichever file is wrong (usually the notes' end-state line
or a missed tag), and log what was reconciled. Do not play on top of a known
mismatch.
