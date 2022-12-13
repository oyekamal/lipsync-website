# import statistics

# import numpy as np
from PIL import Image, ImageOps


def zoom_at(img, x, y, zoom):
    w, h = img.size
    zoom2 = zoom * 2
    img = img.crop((x - w / zoom2, y - h / zoom2, x + w / zoom2, y + h / zoom2))
    return img.resize((w, h), Image.LANCZOS)


def adding_image(
    img_bg, img_fg, location, size=30, rotation=0, mirror=False, size_cordinates=None
):
    """PIL import image required not openCV. this function is responsiable for adding image, size and rotating it"""
    if size_cordinates is not None:
        dim = size_cordinates
    else:
        width, height = img_fg.size
        scale_percent = size  # percent of original size
        width = int(width * scale_percent / 100)
        height = int(height * scale_percent / 100)
        dim = (width, height)

    if mirror:
        img_fg = ImageOps.mirror(img_fg)

    if rotation != 0:
        img_fg = img_fg.rotate(rotation)

    img_fg = img_fg.resize(dim)

    img_bg.paste(img_fg, location, mask=img_fg)

    return img_bg


def mirror_image(img):
    return ImageOps.mirror(img)


# how to use this function:
if __name__ == "__main__":
    bg = Image.open(r"./images/background/greenbg.png")

    lips = Image.open(r"./images/happy/l_h.png")

    new_image = adding_image(bg, lips, location=(200, 250))
    new_image.show()
    new_image.save("new_G.png")
