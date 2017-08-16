frequent-words-nltk
=========

A Python implementation to identify most frequent words in a text extracted from a PDF document. Use power of Natural language processing tool kit (NLTK) to clean the text before identification of frequent words.

Setup
--------------

 * Download the source code.
 * Unpack it.
 * cd frequent-words-nltk-master
 * Run `frequent_words_nltk.py`:
 
 .. code:: bash

   $ python frequent_words_nltk.py 

 * Do the following test:
 
 .. code:: bash

    $ ./frequent_words_nltk.py -h

Directly from the repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

   $ git clone https://github.com/shivatejam/frequent-words-nltk.git
   $ python frequent-words-nltk/frequent_words_nltk.py
       
Post setup
----------

.. code:: bash

    $ pip install PyPDF2
    $ pip install nltk

If you see a stopwords error, it means that you do not have the corpus
`stopwords` downloaded from NLTK. You can download it using command below.

.. code:: bash

    $ python -c "import nltk; nltk.download('stopwords')"

Usage
-----

.. code:: python

    import frequent_words_nltk 
    
    # Read and convert text from a PDF document to a Unicode string.
    text = convert_pdf_txt(<infile>, <password>, <pages>) 
    
    # clean Unicode string to get keywords using power of NLTK.
    # Uses stopwords for english from NLTK, and all puntuation characters.
    # If you want to provide your own set of stop words, punctuations and
    # To use it in a specific language supported by nltk.
    keywords = textminer(<text>, <stop_words>, <punctuations>, <language>)  
    
    # To get python dictionary of n number of most common words
    most_common_words = most_frequent_words(<keywords>, <nwords>) 
    
Command Line Tool
~~~~~~~~~~~~~~~~~~

frequent-words-nltk comes with handy tool:

.. code:: bash

    $ python frequent_words_nltk.py --help
     
To display 10 most frequent words  

.. code:: bash

    $ python frequent_words_nltk.py pdf-example-password.pdf -P test -n 10 

To get 10 most frequent words of dictionary as JSON 
    
.. code:: bash

    $ python frequent_words_nltk.py pdf-example-password.pdf -P test -n 10 -o data
    
To Read data back

.. code:: python

     import json
     
     with open('data.json', 'r') as f:
          data = json.load(f)

Inspired by
----------

This is a python implementation of the algorithm as inspired by *"How to Extract Words from PDFs with Python(1)"*


Why I chose to implement it myself?
-----------------------------------

-  It is extremely fun to implement algorithms.
-  By making *NLTK(2)* an integral part of the implementation I get the flexibility and power to extend it in other
   creative ways, if I see fit later, without having to implement everything myself.

References
----------
#. `How to Extract Words from PDFs with Python <https://medium.com/@rqaiserr/how-to-convert-pdfs-into-searchable-key-words-with-python-85aab86c544f>`_
#. `NLTK <http://www.nltk.org/>`_

Terms and Conditions
--------------------

(This is so-called MIT/X License)

Copyright (c) 2017  Shivateja Medisetti 

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or
sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
