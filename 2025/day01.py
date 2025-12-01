from common.helper import get_input


def task01():
    return "test"


def task02(): ...


def main():
    data = get_input(day=1, year=2025)
    return data


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--task", type=str, default="all", help="1 | 2")
    args = parser.parse_args()

    if args.task == "1":
        print(task01())
    elif args.task == "2":
        print(task02())
