"""Find when a sequence of focus sessions ends, including breaks between sessions."""

import argparse


def positive(text):
    value = int(text)
    if value < 1:
        raise argparse.ArgumentTypeError("Expected an integer of at least 1")
    return value


def nonnegative(text):
    value = int(text)
    if value < 0:
        raise argparse.ArgumentTypeError("Expected an integer of at least 0")
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("start")
    parser.add_argument("sessions", type=positive)
    parser.add_argument("minutes", type=positive)
    parser.add_argument("pause", type=nonnegative)
    args = parser.parse_args()
    try:
        hour, minute = map(int, args.start.split(":"))
        if not (0 <= hour < 24 and 0 <= minute < 60):
            raise ValueError("Start time must be HH:MM on a 24-hour clock")
        elapsed = args.sessions * args.minutes + (args.sessions - 1) * args.pause
        days, clock = divmod(hour * 60 + minute + elapsed, 1440)
        print(f"Finish: {clock // 60:02}:{clock % 60:02} (day +{days})")
    except ValueError as error:
        parser.exit(1, f"{error}\n")


if __name__ == "__main__":
    main()
