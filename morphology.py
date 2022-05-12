from PIL import Image
import numpy as np


class StructureElement:
    def __init__(self, data, size):
        self.data = data
        self.size = size


def erode(pixels, elm, img_size):
    pixels_new = pixels.copy()
    width, height = img_size

    for m in range(0, height):
        for n in range(0, width):
            condition = True
            for i, j in elm.data:
                x = m+i
                y = n+j
                if not (x < 0 or y < 0 or x >= height or y >= width):
                    if pixels[x][y] != True:
                        condition = False
                        break
                    
            if condition:
                pixels_new[m][n] = True # pixels[m][n] 
            else:
                pixels_new[m][n] = False # !!! False
    
    return pixels_new


def dilate(pixels, elm, img_size):
    pixels_new = pixels.copy()
    width, height = img_size

    for m in range(0, height):
        for n in range(0, width):

            if pixels[m][n] == True:
                for i, j in elm.data:
                    x = m+i
                    y = n+j
                    if not (x < 0 or y < 0 or x >= height or y >= width):
                        pixels_new[x][y] = True
    
    return pixels_new


elm1 = StructureElement(
    [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1), ( 0, 0), ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1),
    ],
    (3, 3)
)

elm2 = StructureElement(
    [
        (0, 0), (0, 1),
        (1, 0), (1, 1),
    ],
    (2, 2)
)

img = Image.open("img2.bmp").convert("1")
pixels = np.asarray(img)
print(img.size)

pixels_eroded = erode(pixels, elm1, img.size)
Image.fromarray(pixels_eroded).save("eroded.bmp", mode="1")

# print(pixels[237][:20])
# print(pixels_eroded[237][:20])

pixels_dilated = dilate(pixels, elm1, img.size)
Image.fromarray(pixels_dilated).save("dilated.bmp", mode="1")

# 0 - Black     1 - White
# test = np.zeros(100).reshape((10, 10)).astype(bool)
# print(test)
# Image.fromarray(test).save("test.bmp", mode="1")