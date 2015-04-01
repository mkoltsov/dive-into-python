#!/usr/bin/env python3.4
"""FETCH A list of words from a URL.
"""
import sys
from urllib.request import urlopen
def fetch_words(url):
	"""FETCH A list of words from a URL.
	Args: URL
	Returns: words
	"""
	with urlopen(url) as story:
	     story_words =[]
	     for line in story:
	          line_words=line.decode('utf-8').split()
	          for word in line_words:
	               story_words.append(word)
	return story_words


def print_words(story_words):
	for word in story_words:
	    print(word)


def main(url):
	print(url)
	words = fetch_words(url)
	print_words(words)
 
if __name__ == '__main__':
	main(sys.argv[1]) # the 0arg is reserved