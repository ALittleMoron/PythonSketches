from PIL import Image
import math, re, os, os.path

# TODO: make parsing of directory+path or directory for validation

def img_resize(f_size:str="", path:str="")->Image:
    """resize inputed img in directory and return it
    
    key arguments:
    f_size -- to what size you need to resize the image. Like "200x200"
    """
    if not f_size and not path:
        raise Exception("No argument in img_resize function")
    if type(f_size) is not str or type(path) is not str:
        raise Exception("function need string arguments")

    full_path_pattern = re.compile(r'^([CD]:.)(\.\w{1,5})$')
    cur_path_pattern = re.compile(r'^([a-zA-Z]+)(\.\w{1,5})$')

    if full_path_pattern.fullmatch(path) is not None:
        if not os.path.exists(path):
            raise Exception("Path not exist")
        with Image.open(path) as img:
            sz = img.size
            img.load()
            img.thumbnail(sz)
            return img

    elif cur_path_pattern.fullmatch(path) is not None:
        if not os.path.isfile(path):
            raise Exception("cringe error. how you input not file with file extention?")
        with Image.open(path) as img:
            sz = img.size
            img.load()
            img.thumbnail(sz)
            return img

    else:
        raise Exception("Not a directory or file.")

if __name__ == "__main__":
    a = img_resize("500x200", path = "abs.jpg")
    a.show()
