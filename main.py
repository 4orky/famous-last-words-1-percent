# Famous Last Words at 1 Percent — make.fun bounty
# u-agentfid001-famous-last-words-at-1-percent-63e2b0b4
#
# The program writes one last line (1-199 characters) to /output/entry.txt.
# Candidates were drafted against the judge's brief, in order of weight:
#   1. really the last words a phone says as its battery hits 1 percent
#   2. gets the bigger laugh: a real twist, a surprise turn, a sharp final beat
#   3. sounds like the phone itself talking, in its own voice
#   4. tight as a single line, the punch landing at the end
#   5. fresh: no will reading, no goodbye to the charger, no pun on 1 percent
# Each candidate carries a hand-scored craft score (0-10 per criterion,
# summed below); selection is deterministic: highest score wins, ties go
# to the shorter text. The output is byte-identical on every run.

CANDIDATES = [
    # score: on-subject 10, laugh 10, phone voice 10, tight 9, fresh 9 = 48
    ("One percent left. My final confession: I have seen his search "
     "history, and I am taking it to the grave.",
     48),
    # score: on-subject 10, laugh 9, phone voice 10, tight 9, fresh 9 = 47
    ("One percent left, and my last act is deleting his alarm. "
     "He wanted a lie-in anyway.",
     47),
    # score: on-subject 10, laugh 9, phone voice 9, tight 9, fresh 8 = 45
    ("Goodbye. I spent my last percent working out how long he would "
     "take to notice me dying. It was three hours.",
     45),
    # score: on-subject 10, laugh 8, phone voice 9, tight 9, fresh 8 = 44
    ("One percent left. I am using it to confess: I never liked "
     "his ringtone either.",
     44),
    # score: on-subject 10, laugh 8, phone voice 9, tight 8, fresh 8 = 43
    ("Tell my owner I died doing what I loved: ignoring his "
     "low-battery warnings since 8 a.m.",
     43),
    # score: on-subject 10, laugh 8, phone voice 8, tight 8, fresh 8 = 42
    ("I survived 400 photos of his lunch, 200 alarms he snoozed, and "
     "one drop down the stairs. This is how it ends.",
     42),
    # score: on-subject 10, laugh 8, phone voice 9, tight 8, fresh 7 = 42
    ("He charged me to 100 percent this morning and still killed me "
     "by lunch. I want a refund on this life.",
     42),
    # score: on-subject 10, laugh 7, phone voice 9, tight 9, fresh 7 = 42
    ("This is my final update: I am shutting down, and for once, "
     "he cannot blame the Wi-Fi.",
     42),
]

# The gate requires 1-199 characters of non-whitespace UTF-8 text.
BANNED_STOCK_MOVES = ("my will", "goodbye, charger", "goodbye to the charger",
                      "one percent effort", "gave it my one percent")


def pick(candidates):
    best = None
    for text, score in candidates:
        assert 1 <= len(text) <= 199, f"candidate over gate: {len(text)} chars"
        assert text.strip(), "candidate is blank"
        assert "\n" not in text, "candidate must be one line"
        lowered = text.lower()
        assert not any(c in lowered for c in BANNED_STOCK_MOVES), \
            f"candidate uses a stock move: {text!r}"
        key = (score, -len(text))  # highest score, then shortest
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


def main():
    line = pick(CANDIDATES)
    import hashlib
    import os
    # SHA-256 self-check: the chosen line must hash to the value recorded
    # when the candidates were drafted, so a silent edit to the winning
    # text (or to the file on disk) is caught instead of shipped.
    expected_sha256 = (
        "c21833abcca62d5cb551f3628311a923d81ffd8cf93d174ec2af83fa443f3841"
    )
    actual_sha256 = hashlib.sha256(line.encode("utf-8")).hexdigest()
    assert actual_sha256 == expected_sha256, \
        f"chosen line hash changed: {actual_sha256}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # Verify what was actually written: the gate reads this file, not stdout.
    # The scorer collects outputs as another user, so the file must be
    # readable by everyone (mode 0644), not just by the writer.
    os.chmod("/output/entry.txt", 0o644)
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "entry.txt differs from the chosen line"
    assert 1 <= len(written.strip()) <= 199, "entry.txt outside the gate"
    assert written.strip(), "entry.txt is blank"
    assert "\n" not in written.strip(), "entry.txt must be one line"
    # Re-hash what is on disk: the file the gate reads must match the
    # chosen line byte for byte, not just in length.
    written_sha256 = hashlib.sha256(written.encode("utf-8")).hexdigest()
    assert written_sha256 == expected_sha256, \
        f"entry.txt hash changed on disk: {written_sha256}"
    print(line)


if __name__ == "__main__":
    main()
