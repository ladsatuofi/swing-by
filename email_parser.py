from PIL import Image
from pytesseract import image_to_string

def image_parser(image):

    image = Image.open('filedirectory')
    text = image_to_string(image)
    print(text)


# get the entire email format from HTML (including title, body, sender, receiver)

# check that the place forwarded is actually from an @illinois.edu email

# parse dates

# parse times

# parse potential categories

# check that the categories are similar to what the user has tagged it