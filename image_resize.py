from PIL import Image
import math

def img_resize(f_size="", path="", directory=""):
    if not f_size and not path:
        raise Exception("No argument (r_size, f_size or path) in img_resize")
    
    if directory:
        with Image.open(directory+path) as img:
            size = f_size.split('x')
            size = tuple([int(i) for i in size])
            img.thumbnail(size)
            return img

    elif not directory:
        with Image.open(path) as img:
            size = f_size.split('x')
            size = tuple([int(i) for i in size])
            img.thumbnail(size)
            return img

    else:
        raise Exception("IDK what went wrong")


a = img_resize("600x800", path = "car.png", directory="C:/Users/dimal/Desktop/")
a.show()
# test_image = "" # file dir+name with wormat or just name with format
# original = Image.open(test_image)
# original.show()
# size = 354, 472

# width, height = original.size   # Get dimensions
# left = width/4
# top = height/8
# right = 3 * width/4
# bottom = height
# cropped_example = original.crop((left, top, right, bottom))


# cropped_example.show()
# cropped_example.thumbnail(size)
# cropped_example.show()