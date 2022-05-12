from PIL import Image
import numpy as np


def filter(pixels, filter, img_size, filter_size):
    pixels_copy = pixels.copy()
    width, height = img_size
    w = sum([sum(e) for e in filter])
    r = filter_size // 2

    for m in range(0, height):
        for n in range(0, width):
            s = 0
            for i in range(-r, r+1):
                for j in range(-r, r+1):
                    s += f(pixels_copy, m+i, n+j) * filter[i+r][j+r]
            
            res = s / w

            if res < 0:
                pixels[m][n] = 0
            elif res > 255:
                pixels[m][n] = 255
            else:
                pixels[m][n] = res
            
def f(pixels, x, y):
    return 0 if x < 0 or y < 0 or x >= len(pixels) or y >= len(pixels[0]) else pixels[x][y]

def w(filter, x, y):
    pass


filter1 = np.array([
    [-1, -1, -1],
    [-1,  9, -1],
    [-1, -1, -1],
])

filter2 = np.array([
    [ 0,  -1,  0],
    [-1,  20, -1],
    [ 0,  -1,  0],
])

# LoG (Laplassian of Gauss)
filter3 = np.array([
    [ 0,  0, -1,  0,  0],
    [ 0, -1, -2, -1,  0],
    [-1, -2, 16, -2, -1],
    [ 0, -1, -2, -1,  0],
    [ 0,  0, -1,  0,  0],
])


img = Image.open("img.bmp").convert("L")
pixels_test = img.load()

width, height = img.size
print(img.size)
pixels = np.asarray(img)


print(pixels[0][:10])
print(pixels[1][:10])

filter(pixels, filter1, (width, height), len(filter1))

print(pixels[0][:10])
print(pixels[1][:10])

Image.fromarray(pixels, mode="L").save("filtered.bmp")
