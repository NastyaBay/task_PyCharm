from PIL import Image
import numpy as np


def count_gray(pixels, pixels_x, pixels_y, size):
    gray = np.sum((pixels[pixels_x: pixels_x + size, pixels_y: pixels_y + size]) / 3)
    return int(gray // (size * size))


def replace_pixels(pixels, pixels_x, pixels_y, size, step):
    gray = count_gray(pixels, pixels_x, pixels_y, size)
    pixels[pixels_x: pixels_x + size, pixels_y: pixels_y + size] = int(gray // step) * step


def convert_gray_img(pixels, size, grey_step):
    step = 255 // (grey_step - 1)
    height = len(pixels)
    width = len(pixels[1])
    pixels_x = 0
    while pixels_x < height:
        pixels_y = 0
        while pixels_y < width:
            replace_pixels(pixels, pixels_x, pixels_y, size, step)
            pixels_y = pixels_y + size
        pixels_x = pixels_x + size
    return pixels


img = Image.open(input('Имя входного файла:'))
pixels_img = np.array(img)
size_pixel = int(input('Размер пикселя(блока):'))
step_gray = int(input('Количество градаций:'))
res_file = input('Имя для сохранения файла:')
res = Image.fromarray(convert_gray_img(pixels_img, size_pixel, step_gray))
res.save(res_file)
