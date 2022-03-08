#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""A "Prime game" runner."""

import sys

from brain_games import engine, games


def main():
    """Run a game."""
    engine.run(games.prime)


if __name__ == '__main__':
    sys.exit(main() or 0)
