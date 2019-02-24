from PIL import Image
import cv2 as cv
from pytesseract import image_to_string
import datefinder
import location_extractor as loc


# parse dates
def date_extraction(copy_of_text):
    matches = datefinder.find_dates(copy_of_text)
    #throw out extraneous dates (non 2019)
    #throw out dates lasting over a week
    for match in matches:
        print(match)


def location_extraction(text):
    matches = loc.extract_locations_from_text(text)
    #search for most viable location
    for match in matches:
        print(match)