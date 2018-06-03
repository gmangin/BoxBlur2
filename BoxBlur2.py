#!/bin/python3

def summatrix(image, i, j):
    count = 0
    for x in range(3):
        for y in range(3):
            count += image[i + x][j + y]   
    return count//9

def forj(image, i, index, newimage):
    j = 0
    while j < len(image[i]):
        if j == len(image[i]) - 1:
            newimage[index].append(summatrix(image, i, j - 2))
        elif j == len(image[i]) - 2:
            newimage[index].append(summatrix(image, i, j - 1))
        elif j % 3 == 0:
            newimage[index].append(summatrix(image, i, j))
        j += 3
    return newimage

def boxBlur(image):
    newimage = []
    i = 0
    while i < len(image):
        if i == len(image) - 1:
            newimage.append([])
            forj(image, i - 2, i // 3, newimage)
        elif i == len(image) - 2:
            newimage.append([])
            forj(image, i - 1, i // 3, newimage)
        elif i % 3 == 0:
            newimage.append([])
            forj(image, i, i // 3, newimage)
        i += 3
    return newimage
