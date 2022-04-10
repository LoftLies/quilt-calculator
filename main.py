# Adapted from tutorial of John Hammond, https://youtu.be/CSU0Ar-koR4
from PIL import Image
from collections import Counter
import prettytable

def CountColors(imagePath):

    # Open the image and convert to RGB mode
    with Image.open(imagePath) as img:
        img = img.convert("RGB")

    # Read the width and height from the image into variables x and y
    size = w, h = img.size

    # Load the image data
    data = img.load()

    # Create a list of colors, add color of each pixel in the image data to the list
    colors = []
    for x in range(w):
        for y in range(h):
            color = data[x, y]

            # Format the separate RGB values into one hexadecimal value
            # ['0xff', '0xff', '0xff'] --> remove '0x', add leading 0's if necessary, join together
            hex_color = '#'+''.join([hex(c)[2:].rjust(2,'0') for c in color])
            colors.append(hex_color)

    pt = prettytable.PrettyTable(["Color", "Count"])

    for color, count in Counter(colors).items():
        pt.add_row([color, count])

    print(pt)
    
    colors = list(dict.fromkeys(colors))
    colorsfound = len(colors)

    return colorsfound
