from PIL import Image

img = Image.open("GLaDOS.jpg")

flipped = img.transpose(Image.ROTATE_180)

flipped.show()