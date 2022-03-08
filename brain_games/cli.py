# -*- coding: utf-8 -*-

"""Prompt library usage example."""

import prompt


def run():
    """Interact with user."""
    print('Welcome to the Brain Games!\n')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
