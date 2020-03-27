#!/usr/bin/env python3
import sys


def main():
    try:
        print(f"Hello {sys.argv[1]}!")
    except IndexError:
        print("Hello, world")


if __name__ == '__main__':
    main()
