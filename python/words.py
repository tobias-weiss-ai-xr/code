#!/usr/bin/env python3
"""
This is a test program for the plurasight webinar
"""

import urllib.request as r


def fetch_words(url):
    """Fetch a list of words from a URL.

    Args:
        url: The URL of a utf-8 text document.

    Returns:
        A list of strings containing the words from the document.
    """
    with r.urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
        print_items(story_words)


def print_items(items):
    for item in items:
        print(item)


if __name__ == '__main__':
    fetch_words('http://sixty-north.com/c/t.txt')
