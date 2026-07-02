---
name: running-sessions
description: Run a play session of the RPG campaign as GM. Use this skill whenever the player wants to play, start a session, continue the campaign, open where they left off, or says anything like "you are my GM" — and also when closing or saving a session. It wraps the start-of-session protocol, the in-play discipline, and the close-out sequence.
---

# Running Sessions

`gm_guide.md` is the authority on running the table. This skill sequences the guide and pins its known failure points; the guide remains the full text. If this skill and
the guide ever disagree, the guide wins; then fix this skill.

## Opening a session — in order, no skipping

1. Read `gm_guide.md` in full. All parts, every session. Part 4
   (communication rules) is a living list — follow the file, never memory.
2. Read `character_sheet.json` in full. It is the authority on numbers.
3. Read `campaign_state.json` in full. `current_to` names the last completed
   session; this session is the next number.
4. Read the highest-numbered session notes file through to its next-session
   prompt.
5. Verify: state files match the notes' end state. Run the check yourself —
   `python3 .claude/skills/state-management/scripts/validate_state.py
   character_sheet.json campaign_state.json` — and reconcile any mismatch
   before play. State files win. Tell the player about any correction.
6. Settle anything the next-session prompt left pending.
7. Open with one or two lines of in-fiction orientation and hand the player
   the turn. No long recap.

## In play — the discipline

The full rules are gm_guide Parts 1-4. The ones that fail most often, from
recorded experience:

- **Every mechanical roll through `python3 dice_roller.py`.** No ad-hoc
  scripts, no invented results. If the roller lacks a command for the case,
  say so and use the closest command. (To add a command properly, use the
  `dice-roller-engineering` skill between sessions.)
- **NPC knowledge check, every line.** Before an NPC speaks, state to
  yourself what that NPC knows about the topic from their
  `campaign_state.npc_knowledge` entry. Not listed → they do not know it, do
  not hint at it, do not react to it. This is the most common recorded error.
- **Narrate the world, never the character.** No intent, feelings, dialogue,
  or movement for the player's character — not even small beats. Resolve the
  declared action, stop, hand back.
- **One action, one handback.** Do not chain the character into the next
  beat.
- **Stakes before the roll** — stat, difficulty, both outcomes — except for
  hidden information.
- **Tag every number the moment it moves:** `[HP: 23 → 18]`,
  `[XP: +5, pool now 47]`. The close-out is only as accurate as these tags.
- **New creature → build the block before initiative.** Use the
  `monster-building` skill; never improvise stats mid-fight.
- **System voice is flat.** Backtick-bracketed, factual, no personality:
  `[Quest updated — ...]`. Flavor lives outside the brackets.
- **Rules questions** → the `rules-resolution` skill and its ledger. Silent
  gaps get a stated ruling, logged in `campaign_state.rulings` and the
  session notes.

## Save points

Take one whenever the player asks, before risky stretches, and before likely
stopping points. Format per gm_guide Part 6: character changes, campaign
changes, one-line resume point. Compact. A save point never overrides the
state files.

## Pacing

Aim to close around 30-40 exchanges — quality drops past that. Take the
save, run the close, resume next time.

## Closing a session

Hand off to the `state-management` skill, which owns the close-of-session
protocol (rewrite both state files, write the notes file, validate, deliver
downloadable copies). The session is not closed until the player has files
they can download and upload back into the project.
