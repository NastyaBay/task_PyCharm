from PIL import Image
import numpy as np


def count_gray(pixels, pixels_x, pixels_y, size):
    """"""
    gray = np.sum((pixels[pixels_x: pixels_x + size, pixels_y: pixels_y + size]) / 3)
    return int(gray // (size * size))


def replace_pixels(pixels, pixels_x, pixels_y, size, step):
    gray = count_gray(pixels, pixels_x, pixels_y, size)
    pixels[pixels_x: pixels_x + size, pixels_y: pixels_y + size] = int(gray // step) * step


def convert_gray_img(pixels, size, grey_step):
    step = 255 // (grey_step - 1)
    height = len(pixels)
    width = len(pixels[1])
    for pixels_x in range(0, height, size):
        for pixels_y in range(0, width, size):
            replace_pixels(pixels, pixels_x, pixels_y, size, step)
    return pixels


img = Image.open('img2.jpg')
pixels_img = np.array(img)
size_pixel = 10
step_gray = 50
res = Image.fromarray(convert_gray_img(pixels_img, size_pixel, step_gray))
res.save('res_filename.jpg')
