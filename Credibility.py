import cv2 as cv
def image_verification(image):

    # read in the image
    image = cv.imread('filename.jpg')
    gray_image = gray_image = cv.cvtColor(image, cv.COLOR_RGB2GRAY)

    # applying Gaussian blur to the image to remove noise
    gray_image = cv.cvtColor(gray_image, cv.COLOR_RGB2GRAY)
    blur = cv.GaussianBlur(gray_image, (5, 5), 0)

    # display the image that has had noise removed
    cv.imshow('result', blur)
    cv.waitkey(0)

