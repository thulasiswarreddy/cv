from PIL import Image

img = Image.open("image.jpg")

gray_img = img.convert("L")

img.show()
gray_img.show()

gray_img.save("gray_image.jpg")

print("Image converted to grayscale successfully!")
