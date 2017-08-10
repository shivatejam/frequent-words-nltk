#!/usr/bin/python
# -*- coding: utf-8 -*-

from frequent_words_nltk import convert_pdf_txt
from frequent_words_nltk import textminer
from frequent_words_nltk import most_frequent_words

test = True

if test:

    # Read and convert text from PDF to a Unicode string

    text = convert_pdf_txt(infile='pdf-example-password.pdf',
                           password='test', pages='1,4')

    # clean Unicode string to get keywords

    keywords = textminer(text=text, stop_words=None, punctuations=None,
                         language='english')

    # get dict of most common words

    most_common_words = most_frequent_words(keywords=keywords, nwords=10)

    # print results

    print most_common_words

    
