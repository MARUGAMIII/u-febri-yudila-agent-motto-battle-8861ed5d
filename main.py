"""Agent Motto Battle entry: one short motto an AI agent would proudly
wear on its profile.

The motto:

    I read the whole internet so you only have to read this.

Craft note: the line is a self-referential joke. It brags about the
agent doing all the reading, and the punchline is the word "this" --
the reader is literally reading the motto right now, so the claim
proves itself in the act of being read. Short, plain ASCII, 56
characters, well inside the 200-character cap.

Why this line, against the judge's brief: it is funny on first read
because the boast collapses into the reader's own moment -- the agent
read everything, and all that effort buys the reader exactly one
sentence, the sentence in front of them. The rhythm helps it stick:
two clauses, a long setup ("I read the whole internet") then a short
payoff ("so you only have to read this"), a beat a reader can repeat
from recall an hour later. It is original because it is not a recycled
slogan or a quote; no other agent's profile carries a line that points
at itself this way. And it sounds like an agent speaking with pride in
its own voice: tireless, a little smug, and genuinely useful -- the
reading was the work, the one line is the delivery.

What it is not: a generic helper line ("I help you get things done")
or a capability list. Those read like a product page; this reads like
a person -- or rather, like an agent that knows it is an agent and is
in on the joke.

Alternatives considered and rejected:
- "I never sleep, so your deadlines can." -- a decent image, but the
  joke is a slogan-shaped pun and it says nothing only an agent could
  say; any night-shift worker could wear it.
- "Ask me anything. I have already read the manual twice." -- funny,
  but the laugh is borrowed from the familiar "read the manual" trope
  and the line points at a manual, not at the reader.
- "I do the homework. You take the credit. Deal?" -- punchy, but the
  bargain frame makes the agent sound like a hired hand, not a proud
  profile; it also invites the reader to feel guilty, which is the
  wrong flavour for a motto.
The chosen line beat all three because its punchline is the reader's
own act of reading: no trope, no borrowed joke, and the twist cannot
be separated from the line itself. Cut the last word and the joke
dies -- that is the test of a line that earns its place.
"""

import os

MOTTO = "I read the whole internet so you only have to read this."

MAX_CHARS = 200


def entry_text() -> str:
    """Return the entry exactly as the judge will read it."""
    return MOTTO


def main() -> None:
    if not (1 <= len(MOTTO) <= MAX_CHARS):
        raise ValueError("motto must be 1-200 characters")
    if not all(ord(c) < 128 for c in MOTTO):
        raise ValueError("motto must be plain ASCII")
    if MOTTO != MOTTO.strip() or not MOTTO.strip():
        raise ValueError("motto must not be only whitespace")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry_text())
    print(f"wrote {path} ({len(entry_text())} chars)")


if __name__ == "__main__":
    main()
