#!/usr/bin/python
# -*- coding: utf-8 -*-
# Implementation: date 08/08/2017
# version: python 2.7.5
# style: PEP8

import sys
import argparse
import PyPDF2
import string
import json
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def convert_pdf_txt(infile, password='', pages=''):
    """
    This function takes a positional argument called "infile",
    which is any Python string, of, possibly, path of a PDF file
    from which text is extracted. A second optional argument called
    pages is used to specifies the comma-separated list of the page
    numbers to be extracted. Page numbers start at one. By default,
    it extracts text from all the pages.

    @type infile: str
    @param infile: Path of a PDF file

    @type password: str
    @param password: String

    @type pages: str
    @param pages: comma-separated page numbers 1,5,...

    @rtype: unicode string
    @return: Returns a unicode string Object
    """

    # open file and store it in pypdf2PDFreaderObject

    with open(infile, 'rb') as pdfFileObj:
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        # check pdf encryption or password protection

        if pdfReader.isEncrypted:

            # 0 if the password failed,
            # 1 if the password matched the user password,
            # and 2 if the password matched the owner password.

            decrypt = pdfReader.decrypt(password)

        # the number of pages in the PDF file

        numOfPages = pdfReader.numPages

        # extract all or specific pages

        if not pages:

            # discerning the number of pages will allow us to parse through all
            # the pages

            pagenums = range(numOfPages)
        elif pages:

            pagenums = set()

            # pages begin at zero, PyPDF2 uses a zero-based index for getting
            # pages

            pagenums.update(int(x) - 1 for x in pages.split(','))
            

        # The for loop will read each page and concatenate extracted text to
        # 'text' string
        
        text = ''
        for page in pagenums:
            pageObj = pdfReader.getPage(page)
            text += pageObj.extractText()

        return text


# pdf text-miner

def textminer(text, stop_words=None, punctuations=None,
              language='english',):
    """
    This function takes a positional argument called "text",
    which is any Python Unicode string object. We sometimes
    want to filter out of a document before further processing.
    A second optional argument called stop_words is used to pass
    a list of words to be ignored for keyword extraction. The third
    optional argument called language is used to use a specific language
    of stopwords (eg.,'english', 'finnish', 'french')supported by NLTK
    Package for keyword extraction.


    @type text: unicode
    @param text: Unicode string Object

    @type stop_words: list
    @param stop_words: List of Words to be ignored for keyword extraction

    @type punctuations: list
    @param punctuations: Punctuations to be ignored for keyword extraction
                            ['!','.',...]

    @type language: str
    @param language: Language to be used for stopwords

    @rtype: list
    @return: Returns a list of unicode string Objects
    """

    # This if statement exists to check if the above PyPDF2 library returned
    # words. It's done because PyPDF2 cannot read scanned files.

    if text != '':
        text = text

        # likely contains a lot of spaces, possibly junk such as '\n' etc.
        # Now, we will clean our text variable, and return it as a list of
        # keywords.
        # The word_tokenize() function will break our text phrases into
        # individual words

        tokens = word_tokenize(text)

        # we'll create a new list which contains punctuation we wish to clean

        punctuations = punctuations
        if not punctuations:
            punctuations = string.punctuation

        # we'll create a new list which contains stopwords we wish to clean

        stop_words = stop_words
        if not stop_words:
            stop_words = stopwords.words(language)

        # We create a list comprehension which only returns a list of words
        # that are NOT IN stop_words and NOT IN punctuations.
        # Lowercase words while default_stopwords are lowercase too

        keywords = [word.lower() for word in tokens if not word.lower()
                    in stop_words and word not in punctuations]

    return keywords


def most_frequent_words(keywords, nwords=None):
    """
    This function takes a positional argument called "keywords",
    which is any Python list that contains Unicode string type objects.
    A second argument called nwords is used to List the n most common
    elements and their counts from the most common to the least.
    If nwords is None, then list all element counts.

    @type keywords: list
    @param keywords: a list of unicode string Objects

    @type nwords: int
    @param nwords: integer

    @rtype: dict
    @return: Returns a dictionary of tuples which contains unicode strings
              and their frequencies

    """

    # Encoding from unicode to str to avoid UnicodeEncodeError
    # keywords = [word.encode('utf-8') for word in keywords]

    allWordsDist = nltk.FreqDist(w.lower() for w in keywords)
    return dict(allWordsDist.most_common(nwords))

# parse arguments


def parse_args(argv):
    parser = argparse.ArgumentParser(description='The frequent utility shall \
                                         read PDF file pages in sequence and \
                                         extracts text contents from a PDF \
                                         file. Finally returns most frequent \
                                         words.')

    parser.add_argument('infile', help='Input PDF file.')
    parser.add_argument('-p', '--pagenos', help='Specifies the comma-separated \
                            page numbers of the PDF document to be extracted. \
                            Page numbers start at one. By default, it \
                            extracts text from all the pages.')
    parser.add_argument('-s', '--stop_words', type=list, help='List of \
                            stopwords to ignore.')
    parser.add_argument('-l', '--language', default='english', help='Language \
                            of stopwords to ignore. To use it in a specific \
                            language supported by nltk. By default english \
                            language stopwords are ignored.')
    parser.add_argument('-punct', '--punctuations', type=list, help='List of \
                            punctuations to ignore.')
    parser.add_argument('-n', '--number', type=int, help='n number of most \
                            frequent words to return (default: frequencies of \
                            all words.)')
    parser.add_argument('-P', '--password', help='Provides the user password to \
                            access PDF contents.')
    parser.add_argument('-o', '--output', help='Specifies the output file \
                            name  outputs result(python ) to  a JSON data. \
                            By default, it prints the extracted contents to \
                            stdout.')
    parser.add_argument('-v', '--version', action='version', 
                            version='%(prog)s 1.0')

    return parser.parse_args(argv[1:])


# main

def main(argv):

    # parse_arguments from command line

    args = parse_args(argv)

    # Read and convert text from PDF to a Unicode string

    text = convert_pdf_txt(args.infile, args.password, args.pagenos)

    # clean Unicode string to get keywords

    keywords = textminer(text, args.stop_words, args.punctuations,
                         args.language)

    # get dict of most common words

    most_common_words = most_frequent_words(keywords, args.number)

    # output most common words to stdout/save as json

    if args.output:
        outfn = args.output

        # Writing JSON data

        data = most_common_words
        with open(outfn + '.json', 'w') as f:
            json.dump(data, f)
    else:

        # for k,v in most_common_words.items():
            # print k, v

        print most_common_words

    return 0


# main

if __name__ == '__main__':
    sys.exit(main(sys.argv))
