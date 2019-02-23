from PIL import Image
import cv2 as cv
from pytesseract import image_to_string
import datefinder
class email_parser():
    def main(self ):
        extracted_text = image_parser()
        image = Image.open('/Users/stevenli/PycharmProjects/swing-by')
        extract_dates(extracted_text)

    def image_parser(some_image):
        image = Image.open('/Users/stevenli/PycharmProjects/swing-by')
        text = image_to_string(image)
        return text

    # parse dates
    def extract_dates(text):
        matches = list(extract_dates(text))
        for match in matches:
            print(match)

    # parse times
    def time_extraction(text):

    main()


