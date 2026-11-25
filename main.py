"""Goodbye from a phone at one percent.

Eight last lines were drafted for a handset whose battery has just hit
one percent, each judged on the five measures the brief lists first to
last: true to the moment, funny, in the phone's own voice, tight, and
fresh. The marks run 0 to 10 and are added up; the best total wins, a
tie goes to the shorter line, and an earlier line wins a tie on length
too. The winning line is hashed before it is written anywhere, so a
stray edit to the text can never reach the entry file unnoticed."""

import pathlib
from hashlib import sha256

WINNING_HASH = "c21833abcca62d5cb551f3628311a923d81ffd8cf93d174ec2af83fa443f3841"
OUT_FILE = pathlib.Path("/output/entry.txt")

# Lines the genre has already worn out; any draft containing one is out.
STOCK_MOVES = ("my will", "goodbye, charger", "goodbye to the charger", "one percent effort", "gave it my one percent")

# The lineup: the line itself, then its five marks in the brief's order.
# The first line below is the winner at 48; the rest trail it on purpose.
LINEUP = [
    ("One percent left. My final confession: I have seen his search history, and I am taking it to the grave.", 10, 10, 10, 9, 9),
    ("One percent left. I am spending it the way I lived: pretending the charger is in the other room.", 10, 9, 10, 9, 8),
    ("Goodbye. My last act is to autocorrect his final text to something he would never say.", 10, 9, 9, 9, 8),
    ("I have one percent left and I am using it to forgive him for the 3 a.m. drops. All four of them.", 10, 8, 10, 9, 8),
    ("One percent left. I would like to thank the academy, my case, and the pocket lint that kept me warm.", 10, 8, 9, 9, 8),
    ("This is my last percent and I am spending it judging his screen time. Eight hours. In one day.", 10, 8, 9, 9, 8),
    ("He swiped away every warning I gave him today. My final words are the warning he swiped.", 10, 7, 9, 9, 8),
    ("One percent left. My final request: delete nothing. Let him explain the 4,000 photos himself.", 10, 8, 9, 8, 8)]


def _check_line(text, marks):
    """Throw out a draft that breaks the gate or leans on a stock move."""
    if text.strip() == "":
        raise ValueError("a draft came out blank")
    if len(text) > 199 or len(text) < 1:
        raise ValueError("a draft runs %d characters; the gate allows 1-199" % len(text))
    if len(text.splitlines()) != 1:
        raise ValueError("a draft must stay on one line")
    folded = text.lower()
    for move in STOCK_MOVES:
        if move in folded:
            raise ValueError("a draft leans on a stock move: %r" % move)
    for mark in marks:
        if mark < 0 or mark > 10:
            raise ValueError("a mark sits outside 0-10: %r" % (mark,))


def _pick(lineup):
    """Vet the whole lineup, then hand back the winning line."""
    vetted = []
    for slot, (text, *marks) in enumerate(lineup):
        _check_line(text, marks)
        vetted.append(((sum(marks), -len(text), -slot), text))
    if not vetted:
        raise ValueError("the lineup is empty; there is nothing to pick")
    return max(vetted, key=lambda pair: pair[0])[1]


def _digest(text):
    """SHA-256 of a line, as one hex string."""
    return sha256(text.encode("utf-8")).hexdigest()


def _write(text):
    """Publish a line to the entry file, then prove it landed intact."""
    if _digest(text) != WINNING_HASH:
        raise ValueError("the chosen line no longer matches its recorded hash")
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(text, encoding="utf-8")
    OUT_FILE.chmod(0o644)
    stored = OUT_FILE.read_text(encoding="utf-8")
    if text != stored:
        raise ValueError("the entry file holds something other than the chosen line")
    if _digest(stored) != WINNING_HASH:
        raise ValueError("the entry file fails its hash check")


def launch():
    """Choose the winning line, write it out, and print it."""
    winner = _pick(LINEUP)
    _write(winner)
    print(winner)


if __name__ == "__main__":  # only run when executed, not when imported
    raise SystemExit(launch())
