import doctest

from PIL import Image
import numpy as np


def count_gray(pixels, pixels_x, pixels_y, size):
    """
    Считает компонент серого цвета и возвращает среднюю яркость
    >>> count_gray(np.array(Image.open('img2.jpg')), 10, 10, 10)
    19
    >>> count_gray(np.array(Image.open('img2.jpg')), 5, 5, 5)
    17
    """
    gray = np.sum((pixels[pixels_x: pixels_x + size, pixels_y: pixels_y + size]) / 3)
    return int(gray // (size * size))


def replace_pixels(pixels, pixels_x, pixels_y, size, step):
    """
    Закрашивает элементы массива(изображения) в один цвет средней яркости
    """
    gray = count_gray(pixels, pixels_x, pixels_y, size)
    pixels[pixels_x: pixels_x + size, pixels_y: pixels_y + size] = int(gray // step) * step


def convert_gray_img(pixels, size, grey_step):
    """
    Возвращает новое изображение(массив) в серых оттенках
    >>> type(convert_gray_img(np.array(Image.open('img2.jpg')), 10, 5))
    <class 'numpy.ndarray'>
    """
    step = 255 // (grey_step - 1)
    height = len(pixels)
    width = len(pixels[1])
    for pixels_x in range(0, height, size):
        for pixels_y in range(0, width, size):
            replace_pixels(pixels, pixels_x, pixels_y, size, step)
    return pixels


if __name__ == '__main__':
    doctest.testmod()

img = Image.open(input('Имя входного файла:'))
pixels_img = np.array(img)
size_pixel = int(input('Размер пикселя(блока):'))
step_gray = int(input('Количество градаций:'))
res_file = input('Имя для сохранения файла:')
res = Image.fromarray(convert_gray_img(pixels_img, size_pixel, step_gray))
res.save(res_file)
