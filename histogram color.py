
import cv2
import matplotlib.pyplot as plt

def analyze_histogram(image_path):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Image not found!")
        return

    colors = ('b', 'g', 'r')
    names = ('Blue', 'Green', 'Red')

    plt.figure(figsize=(8, 5))

    for i, color in enumerate(colors):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=color, label=names[i])

    plt.title("Color Histogram")
    plt.xlabel("Color Intensity Level (0-255)")
    plt.ylabel("Number of Pixels")
    plt.xlim([0, 256])
    plt.legend()
    plt.grid()
    plt.show()

analyze_histogram("/Users/eswar/Desktop/image.jpg")
