---
name: campaign-advancement
description: Steer and extend the Buried Tithe campaign — act transitions, plot pacing, clue management, the war layer, escalation clocks, and the between-act build work (level 6-8 blocks, the Tier 2 bestiary, Fort Greywatch). Use this skill when deciding whether an act has ended, when the plot needs to advance or slow, when a player goes off-thread, when preparing upcoming acts, and when adding anything to the campaign's plot or world at spine level.
---

# Campaign Advancement

`campaign_module_buried_tithe_v2.md` is the full truth of the plot,
GM-facing, hidden from the character. This skill is how to drive it and what
must be built before the module can deliver its later acts. The concrete
build backlog is in `references/build_tasks.md`.

## How the module advances

- **Acts end on discoveries, never dates.** Act 1 ends when "the ground is
  wrong" is discovered; Act 2 on the operation's shape; Act 3 on the Anchor
  Valley battle. Check the module's per-act "discovery" line before
  declaring a transition, then update `campaign_state.act` and `phase` at
  the close.
- **Every load-bearing discovery has multiple routes** (module section 6,
  the clue map). Track which routes have fired — record them in the campaign
  state (a `clue_routes` note under world_flags or rulings works; establish
  the field once and keep using it). **If the player misses three
  consecutive routes to the same discovery, the next one arrives by NPC
  initiative.** The world is full of people who also have eyes.
- **Ignoring the thread is allowed.** Each act's "if ignored" line says what
  happens; the escalation clock (third portal → cache spiral completes →
  pad-house raid → activation) runs one step per long off-thread stretch,
  and each step is loud and offers a fresh on-ramp. Failure at the Act 3
  climax transforms the campaign into a siege arc; it never ends the game.
- **Kade is smart, not psychic.** Track his knowledge like any NPC's —
  arrests, disappearances, patrols in his ground, loud questions in
  Millbrook are what he observes. He accelerates when told to, not before.
- **Do not protect the plot from the player.** A detection or approach
  method the module did not anticipate works if it should work. Caches are
  objects in the ground; the valley is a place on the map.

## Pacing levers

- **Three pillars — plot, exploration, war — share sessions.** When one has
  dominated two sessions, lead the next with a different one. A good
  session touches at least two.
- **The lieutenants are valves:** Voss gates pad access, Fenwick field
  range, Valin magical analysis, Grint equipment. Close a gate for a
  legitimate training reason to slow; open one to speed.
- **Level pacing:** 1-4 fast, 5-8 slower. Act 1 ends ~3, Act 2 ~5-6, the
  Act 3 climax at 7-8, Act 4 spans 8-12. Board quests and gazetteer sites
  throttle in both directions.
- **The war stays personal:** at least one war-layer element per act
  (dispatch progression steps in order, the Sixth, casualty names, Wren,
  Kel). The front's decline and the plot are one operation seen from two
  ends — keep both moving together.
- **Promotion is narrative.** Rank advances on demonstrated leadership and
  trust, never on stats alone.

## Extending at spine level

New plot facts, new Tithe activity, new named opposition, or changes to
what an act contains go through this skill deliberately: check the clue map
for shortcuts, check `world_flags` for contradictions, write the change
into the module file (or a module addendum file) so the next session
inherits it, and keep the character-hidden/GM-facing boundary clean. World
material still follows the player-approval pattern from content-authoring.

## Between-act preparation

The module flags its own build tasks; they are collected, with
specifications and anchors, in `references/build_tasks.md`. Treat that file
as the backlog: before Act 3's climax and before Act 4 there is mandatory
construction work, and starting those acts without it means improvising
set-piece opposition mid-fight — the exact failure the GM guide forbids.
