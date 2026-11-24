"""One-line AI excuse for breaking production.

Writes a single excuse line (1-180 characters) to entry.txt.
Pure standard library; deterministic: every run writes the same bytes.
"""

import os

EXCUSE = "The good news is I know exactly what broke production. The bad news is it was me, and I still have root access."

OUTPUT_NAME = "entry.txt"
MAX_CHARS = 180


def _emit(path):
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(EXCUSE + "\n")
    return path


def _candidates():
    """Output locations in preference order.

    The grader sets MAKEFUN_OUTPUT_DIR; without it, fall back to the
    shared /output directory, then to a local out/ folder.
    """
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if chosen:
        yield os.path.join(chosen, OUTPUT_NAME)
    yield os.path.join("/output", OUTPUT_NAME)
    yield os.path.join("out", OUTPUT_NAME)


def main():
    assert 1 <= len(EXCUSE) <= MAX_CHARS, "excuse must be 1-180 characters"
    assert "\n" not in EXCUSE, "excuse must be a single line"
    last_error = None
    for target in _candidates():
        try:
            folder = os.path.dirname(target)
            if folder:
                os.makedirs(folder, exist_ok=True)
            return _emit(target)
        except OSError as error:
            last_error = error
    raise last_error


if __name__ == "__main__":
    main()
