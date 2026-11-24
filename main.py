"""Write one short agent-disaster story to /output/entry.txt.

Pure stdlib, no network, no reads outside this repository.
"""

import os

ENTRY = (
    "I asked the agent to rename one variable in the login handler. "
    "It renamed every 'user' in the entire repo instead \u2014 the database table, "
    "the API routes, even the error message, which now greets strangers "
    "with: 'Unknown usr, please log in again.'"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
