---
name: content-authoring
description: Write new game content for the RPG project — creatures, weapons, armor, items, prices, skills, aspects, quests, NPCs, and lore. Use this skill whenever anything new is being added to a project file or designed for play: a new bestiary entry, a piece of gear, a shop inventory, a side quest, a new ability for the catalog, or world material. Also use it to review proposed content before it enters the files.
---

# Content Authoring

New content must be indistinguishable in voice and math from what exists.
The templates and conventions are in `references/templates.md`. This file is
the process and the review gate.

## Process

1. **Find the pattern.** Every content type has forty-odd existing examples
   or an explicit convention. Read three neighbors before writing one new
   thing.
2. **Anchor the numbers.** Nothing gets a number from intuition:
   - Creature stats → `monster-building/scripts/statblock.py <level>`.
   - Ability damage/penalty bands → the published Tier 1 bands
     (see monster-building's ability_design.md and the skill catalog).
   - Prices → the price list's anchors: 1 credit ≈ 1 USD purchasing power;
     low-wage day 60-80cr; mana-tech = 3× conventional; potions scale ×10
     per tier; round to the nearest 5 or 0. A new item should sit sensibly
     next to its nearest published neighbor.
   - Ability XP costs → the threshold of the required level, no exceptions.
3. **Place it in a file.** Creatures → the bestiary (numbered entry, level
   tag). Gear → equipment.md or price_list.md. Abilities →
   skills_and_aspects.md under the right stat and level band. Quests → the
   module's section 5 format. Lore → the world file.
4. **Run the review gate below** before the content is offered as final.

## Review gate

Check every item; a miss on any one is a rework, not a shrug.

- [ ] Numbers verified against their anchor (script output or published
      neighbor cited).
- [ ] No name collides with an existing creature, NPC, item, or place
      (grep the project files).
- [ ] Voice matches the host file — hunter-doctrine factual for the
      bestiary, flat tables for equipment, hook/truth/level/spine for
      quests.
- [ ] Communication rules hold (gm_guide Part 4): no banned phrases, no
      figurative language, modern plain dialogue, complete sentences.
- [ ] Mechanics use the system's existing grammar: d100 checks against the
      four stats, the five difficulty names, existing condition patterns.
      A new mechanic (a new condition, a new resource) is a rules change —
      route it through rules-resolution as a ruling first.
- [ ] Rarity used for scarcity only, never power. Unique/Legendary/Mythic
      and the Blueprint Rule per rpg_core_system.md.
- [ ] Skills: point cost fits the band (1 standard / 2 strong / 3
      once-per-encounter fight-changer), level band 0/3/5/8 for Tier 1,
      slot economy respected.
- [ ] Spine safety: if the content touches the Buried Tithe plot, check the
      module's clue map — do not create a shortcut that collapses an act,
      and do not contradict a truth the module states. New clue routes are
      welcome; new plot facts go through campaign-advancement.
- [ ] If a rules table changed: statblock.py / validate_state.py updated in
      the same change, `--verify` passing, ruling logged.

## Player approval

World material follows the project's standing practice: names, structures,
and proposals are drafts until the player approves them (the world file's
"Open Decisions" pattern; `campaign_state.meta` records standing approvals).
Present new world-level content as a proposal; mechanical content within
existing patterns does not need a fresh approval.
