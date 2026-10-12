
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("/Users/eswar/Desktop/image.jpg")

if img is None:
    print("Image not found!")
else:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    eroded = cv2.erode(img, kernel, iterations=1)

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(eroded, cv2.COLOR_BGR2RGB))
    plt.title("Eroded Image")
    plt.axis("off")

    plt.show()
