# coding: utf-8

import argparse
import os
import re
from collections import defaultdict
from heapq import nlargest
from string import punctuation

import cv2 as cv
import pytesseract as ocr
import requests
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize, word_tokenize
from symspellpy.symspellpy import SymSpell

import email_parser as ep

# make runnable from command line
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--parse", help="retrieve dates from image")
args = vars(ap.parse_args())

# read in the image
image = cv.imread('clear.png')

# applying Gaussian blur to the image to remove noise
gray_image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)
blur = cv.GaussianBlur(gray_image, (5, 5), 0)
res = cv.resize(blur, None, fx=3, fy=3, interpolation=cv.INTER_CUBIC)

# display the image that has had noise removed
text = ocr.image_to_string(res)

# extract info from ocr
date_time = ep.date_extraction(text)
if not date_time[0] < date_time[1] and not date_time[0] > date_time[1]:
    date_time = date_time[0]
location = ep.location_extraction(text)


def remove_non_ascii(s): return "".join(i for i in s if ord(i) < 128)


def insert_periods(text):
    return re.sub(r"(?<=\w)([A-Z])", r". \1", text)


def sanitize_input(data):
    """
    Currently just a whitespace remover. More thought will have to be given with how
    to handle sanitzation and encoding in a way that most text files can be successfully
    parsed
    """
    replace = {
        ord('\f'): ' ',
        ord('\t'): ' ',
        ord('\n'): ' ',
        ord('\r'): None
    }
    return str(data).translate(replace)


def tokenize_content(content):
    """
    Accept the content and produce a list of tokenized sentences,
    a list of tokenized words, and then a list of the tokenized words
    with stop words built from NLTK corpus and Python string class filtred out.
    """
    stop_words = set(stopwords.words('english') + list(punctuation))
    words = word_tokenize(content.lower())

    return [
        sent_tokenize(content),
        [word for word in words if word not in stop_words]
    ]


def score_tokens(filtered_words, sentence_tokens):
    """
    Builds a frequency map based on the filtered list of words and
    uses this to produce a map of each sentence and its total score
    """
    word_freq = FreqDist(filtered_words)

    ranking = defaultdict(int)

    for i, sentence in enumerate(sentence_tokens):
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                ranking[i] += word_freq[word]

    return ranking


def summarize(ranks, sentences, length):
    """
    Utilizes a ranking map produced by score_token to extract
    the highest ranking sentences in order after converting from
    array to string.
    """
    if int(length) > len(sentences):
        print("Error, more sentences requested than available. Use --l (--length) flag to adjust.")
        exit()

    indexes = nlargest(length, ranks, key=ranks.get)
    final_sentences = [sentences[j] for j in sorted(indexes)]
    return ' '.join(final_sentences)


def get_title(filtered_words):
    word_freq = FreqDist(filtered_words)
    return word_freq.max()


def spell_check(text):
    # maximum edit distance per dictionary precalculation
    max_edit_distance_dictionary = 2
    prefix_length = 7
    # create object
    sym_spell = SymSpell(max_edit_distance_dictionary, prefix_length)
    # load dictionary
    dictionary_path = os.path.join(os.path.dirname(__file__),
                                   "frequency_dictionary_en_82_765.txt")
    term_index = 0  # column of the term in the dictionary text file
    count_index = 1  # column of the term frequency in the dictionary text file
    if not sym_spell.load_dictionary(dictionary_path, term_index, count_index):
        print("Dictionary file not found")
        return
    # lookup suggestions for multi-word input strings (supports compound
    # splitting & merging)
    input_term = text
    # max edit distance per lookup (per single word, not per whole input string)
    max_edit_distance_lookup = 2
    suggestions = sym_spell.lookup_compound(input_term,
                                            max_edit_distance_lookup)
    for suggestion in suggestions:
        return suggestion.term


text = remove_non_ascii(text)

# text = spell_check(text)
# text = insert_periods(text)
text = sanitize_input(text)
sentence_tokens, word_tokens = tokenize_content(text)
sentence_ranks = score_tokens(word_tokens, sentence_tokens)
summary = summarize(sentence_ranks, sentence_tokens, len(sentence_tokens) // 3)
title = get_title(word_tokens)
r = requests.post("https://swing-by-server.localtunnel.me/v1/events", json = {"time": date_time[0].isoformat(),
                                                                              "timeStr": date_time[0].__format__('%c'),
                                                                              'location': location[0],
                                                                              'description': summary,
                                                                              'name': title,
                                                                              'duration': (date_time[1] - date_time[0]).total_seconds() // 3600
                                                                              })
# print(r.status_code)
# print(requests.get("https://swing-by-server.localtunnel.me/v1/events").content)
