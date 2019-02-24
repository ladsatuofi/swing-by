from PIL import Image
import cv2 as cv
from pytesseract import image_to_string
import datefinder
import location_extractor as loc


# parse dates
def date_extraction(copy_of_text):
    matches = datefinder.find_dates(copy_of_text)
    for match in matches:
        print(match)


def location_extraction(text):
    matches = loc.extract_locations_from_text(text)
    for match in matches:
        print(match)