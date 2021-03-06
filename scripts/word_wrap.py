#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python script to wrap long lines in a text corpus

import textwrap

char_limit = 90
encoding = 'utf-8'
file_in = '/home/babraham/tigrinya_ocr/raw_data/corpus.txt'
file_out = 'wrapped_corpus.txt'

def main():
    wrapper = textwrap.TextWrapper()
    wrapper.width = char_limit
    # all whitespace chars are converted to space: '\t\n\v\f\r'
    wrapper.expand_tabs = True
    wrapper.replace_whitespace = True
    wrapper.break_long_words = False

    # read corpus
    with open(file_in) as f:
        text = f.read()

    text = text.decode(encoding)
    lines = text.splitlines()
    lines = [wrapper.fill(line) for line in lines]
    text = '\n'.join(lines)
    text = text.encode(encoding)
    
    with open(file_out, 'w+') as f:
        f.write(text)


if __name__ == "__main__":
    main()

