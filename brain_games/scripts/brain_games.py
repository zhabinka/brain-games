#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The "Brain Games" script."""

import sys

from brain_games import cli


def main():
    """Run the script."""
    cli.run()


if __name__ == '__main__':
    sys.exit(main() or 0)
