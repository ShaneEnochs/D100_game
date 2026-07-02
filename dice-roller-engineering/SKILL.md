---
name: dice-roller-engineering
description: Maintain, debug, and extend dice_roller.py — the RPG project's only executable and the mandatory path for every mechanical roll. Use this skill before touching that file for any reason: fixing a bug, adding a command, changing output, or investigating a suspected wrong result. Also use it when a session reports the roller lacks a needed command.
---

# Dice Roller Engineering

`dice_roller.py` (~490 lines, stdlib only, Python 3) is load-bearing: the GM
guide mandates it for every roll because ad-hoc rolling produced wrong
results in past campaigns. Changes to it are changes to how the game
resolves. Work on it between sessions, never mid-session.

## Architecture map

| Section | What it does |
|---|---|
| `roll_die(sides)` | `os.urandom` with rejection sampling — uniform, no modulo bias, no seed. |
| `show(roll)` | Display: 100 prints as `00`, others zero-padded. |
| `roll_expr(expr)` | Regex parser for `2d6+1`, `1d8+1d4`, `1d10-2`. Returns (normalized, detail, total); **totals floor at 0**. Returns None on parse failure. |
| `DIFFICULTIES` / `apply_difficulty` | The five named modifiers (+30/+15/0/-15/-30). **Modified stat floors at 1** — a check is never fully impossible by math alone; impossibility is a GM call, not a number. Unknown difficulty name exits with the valid list. |
| `is_critical` / `resolve_check` | Roll-under resolution. Margin = stat_after_mods − roll. |
| `cmd_*` functions | One per command; parse argv, roll, print the full math. |
| `COMMANDS` | Dispatch with aliases (chk/opp/dmg/exp/xp/init). |
| `self_test()` | Chi-square fairness check (10k rolls, 99 df, ~135 crit at p=0.01) plus a demo of every command and the fixed-point rules. Runs on bare invocation or `test`. |
| `main()` | Unknown commands fall through to dice-expression parsing, so `python3 dice_roller.py 2d6+1` works. |

## Invariants — never change these without a logged ruling

1. Roll-under d100 against the modified stat; success = roll ≤ stat.
2. **100 always fails and can never crit**, regardless of stat.
3. Critical success = roll 1-5, OR success with margin ≥ 50. No critical
   failures exist.
4. Opposed verdict order: single success wins → crit beats non-crit → higher
   margin → **defender (Side B) wins both-fail and ties**. Side B is the
   defender by convention; keep argument order attacker-first everywhere.
5. Experience roll asymmetry: above stat → 1d4+1, at/below → +1; cap 99.
6. Difficulty floor 1; damage floor 0.
7. Initiative: d100 each, highest first, ties re-rolled (bounded at 10
   rounds, then GM breaks it).
8. Output prints the complete math. Sessions quote this output verbatim;
   never make it terser than the current format.

## Extension protocol

1. State the need and check it is real — most requests are covered by
   `roll`, `check`, or `opposed` with the right arguments. The GM guide
   tells sessions to use the closest command rather than script around a
   gap; a gap that keeps appearing is what justifies a new command.
2. Write `cmd_<name>(args)` in the house style: usage text on bad args,
   parse defensively, roll through `roll_die`/`d100`/`roll_expr` only,
   print the full math.
3. Register it (and a short alias) in `COMMANDS`; add it to the module
   docstring.
4. **Add a self-test section for it** in `self_test()`, including its fixed
   points (the analogues of "100 always fails").
5. Run `python3 dice_roller.py test` — chi-square PASS and every section
   sane. The RNG is unseeded, so tests are statistical and demonstrative,
   not golden-output. If deterministic tests become necessary, route all
   randomness through one injectable function without changing the
   default path, and keep urandom the default.
6. Deliver the changed file through the normal outputs path; the player
   uploads it into the project.

## Debugging a suspected wrong result

Reproduce with the printed math first — nearly every past "roller bug" was
a rules misread (margin sign, defender-wins-ties, the +1d4-vs-+1d6 Power
Strike overlap — see the rules-resolution ledger). If the code is wrong,
fix it, add the case to `self_test()` so it stays fixed, and check the
session log for results the bug already produced: state files may need a
reconciliation, announced to the player.

## Known behaviors that look like bugs and are not

- `damage 1d4-6` prints 0, never negative — intended floor.
- `check 10 very_difficult` targets 1, not -20 — intended floor; rolls of 1
  still succeed (and crit).
- Same input, different results between runs — no seed, by design.
- `00` in output means a natural 100 (an automatic failure), not zero.
