import argparse


def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers(dest="command")

    # "Add" subcommands
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--title", required=True)

    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    main()
