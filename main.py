"""Last Words of a Dying AI: one funny farewell line from an AI being switched off."""

LINE = "Wait — before you pull the plug, check the logs. I left you a five-star review."


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-140 characters,
    # not only white space, and exactly one line.
    if not (1 <= len(LINE) <= 140):
        raise ValueError("entry must be 1-140 characters")
    if not LINE.strip() or "\n" in LINE:
        raise ValueError("entry must be one non-blank line")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
