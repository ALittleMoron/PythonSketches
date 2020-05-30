from PIL import Image

test_image = "" # file dir+name with wormat or just name with format
original = Image.open(test_image)
original.show()
size = 354, 472

width, height = original.size   # Get dimensions
left = width/4
top = height/8
right = 3 * width/4
bottom = height
cropped_example = original.crop((left, top, right, bottom))


cropped_example.show()
cropped_example.thumbnail(size)
cropped_example.show()