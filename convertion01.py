
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("/Users/eswar/Desktop/image.jpg")

if img is None:
    print("Image not found!")
else:
    h, w = img.shape[:2]

    bigger = cv2.resize(img, (w * 2, h * 2))
    smaller = cv2.resize(img, (max(1, w // 2), max(1, h // 2)))

    print("Original size:", w, "x", h)
    print("Bigger size:", bigger.shape[1], "x", bigger.shape[0])
    print("Smaller size:", smaller.shape[1], "x", smaller.shape[0])

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1, 3, 2)
    plt.imshow(cv2.cvtColor(bigger, cv2.COLOR_BGR2RGB))
    plt.title("Bigger (2x)")
    plt.axis("off")

    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(smaller, cv2.COLOR_BGR2RGB))
    plt.title("Smaller (0.5x)")
    plt.axis("off")

    plt.tight_layout()
    plt.show()
