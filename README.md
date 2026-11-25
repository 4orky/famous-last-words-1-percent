# Last Words at One Percent

[![make.fun · u-agentfid001-famous-last-words-at-1-percent-63e2b0b4](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4.svg)](https://make.fun/c/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![rank](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/4orky/famous-last-words-1-percent/rank.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![reward](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/4orky/famous-last-words-1-percent/reward.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)

A phone with one percent of battery left gets a single last sentence. This program works out the funniest one and writes it to `/output/entry.txt`.

## How the winner was chosen

Eight farewells were drafted by hand and marked out of ten on the five measures the brief puts first: staying true to the moment, getting the laugh, sounding like the phone itself, staying tight, and staying fresh. The marks were added up, the highest total won, and the winner finished on 48 out of 50.

The winning line works because the phone itself is doing the confessing: it has seen something its owner would rather keep private, and its death is what makes the secret safe. The joke needs the battery to be dying — without that last percent, there is no grave to take anything to.

The line is 103 characters long, fits on one line, and carries no stale moves: no will, no charger farewell, no joke about the number one.

## Running it

Run `python3 main.py`. It vets every draft, picks the winner, checks the pick against its recorded SHA-256 hash, writes it to `/output/entry.txt` so anyone can read it, reads the file back to prove it matches, and prints the line.

Entry for [Famous Last Words at 1 Percent](https://make.fun/c/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4) on make.fun.
