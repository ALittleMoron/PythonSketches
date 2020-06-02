from PIL import Image
import math

# TODO: make parsing of directory+path or directory for validation

def img_resize(f_size="", path="", directory=""):
    
    if not f_size and not path:
        raise Exception("No argument (r_size, f_size or path) in img_resize")
   
    if directory:
        with Image.open(directory+path) as img:
            sz = img.size
            img.load()
            img.thumbnail(sz)
            return img

    elif not directory:
        with Image.open(path) as img:
            sz = img.size
            img.load()
            img.thumbnail(sz)
            return img

    else:
        raise Exception("IDK what went wrong")

if __name__ == "__main__":
    a = img_resize("500x200", path = "abs.jpg", directory="C:/python/")
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