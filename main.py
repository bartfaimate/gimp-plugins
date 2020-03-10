#!/usr/bin/python

from gimpfu import *


def plugin_main(timg, tdrawable, maxh=500, maxw=500):
    currentWidth = tdrawable.width
    currentHeight = tdrawable.height

    newWidth = currentWidth
    newHeight = currentHeight

    if (maxw < newWidth):
        newWidth = maxw
        newHeight = (float(currentHeight) / (float(currentWidth) / newWidth))

    if (maxh < newHeight):
        newHeight = maxh
        newWidth = (float(currentWidth) / (float(currentHeight) / newHeight))

    pdb.gimp_image_scale(timg, newWidth, newHeight)

register(
    "python_fu_resize",
    "Saves the image at a maximum width and height",
    "Saves the image at a maximum width and height",
    "Nathan A. Good",
    "Nathan A. Good",
    "2010",
    "<Image>/Image/Resize to max...",
    "RGB*, GRAY*",
    [
        (PF_INT, "max_width", "Maximum Width", 500),    # create input fields
        (PF_INT, "max_height", "Maximum Height", 500),
    ],
    [],
    plugin_main)  # method to register


main()
