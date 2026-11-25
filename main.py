#!/usr/bin/env python3
"""Write the judge-laugh one-liner to /output/entry.txt.

Entry (115 chars, limit 200): "My agent watered the dead plant,
then opened a Jira ticket - 'plants: blocked on sunlight' - and
assigned it to me."

One concrete mechanism (the agent files a Jira ticket for a dead
houseplant), one concrete consequence (the ticket lands on the human,
not the plant), one escalating twist: the blocker is "sunlight",
the one thing the agent was supposed to provide by watering it in
the first place. The agent does process, not gardening - and the
human gets the ticket. Funny because it is exactly how a ticket
queue absorbs a real problem and returns it, assigned, to you.
The two em dashes frame the ticket title the way Jira frames a
summary: the joke reads like a real ticket, because it is one.
"""
import os

ENTRY = "My agent watered the dead plant, then opened a Jira ticket \u2014 'plants: blocked on sunlight' \u2014 and assigned it to me."


def main() -> None:
    # Gate: the sealed scorer only accepts 1-200 chars of non-blank UTF-8.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, limit 200"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
