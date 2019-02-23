from PIL import Image
import cv2 as cv
from pytesseract import image_to_string
import datefinder

def image_parser(self):

    image = Image.open('/Users/stevenli/PycharmProjects/swing-by')
    text = image_to_string(image)

    # parse dates
    def date_extraction(copy_of_text):
        copy_of_text = text
        matches = date_extraction(copy_of_text)
        for match in matches:
            print(match)

    # parse times
    def time_extraction(copy_of_text):
        copy_of_text = text

    # parse potential categories
    def keyword_tokens:

    # check that the categories are similar to what the user has tagged it
    def keyword_match_relevance:
