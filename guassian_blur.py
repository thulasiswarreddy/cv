import cv2
import numpy as np

# Read the image
image = cv2.imread("image.jpg")

# Apply Gaussian Blur
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

# Put both images side by side
combined = np.hstack((image, blurred_image))

# Display both images
cv2.imshow("Original Image | Gaussian Blurred Image", combined)

# Save the side-by-side output
cv2.imwrite("output_side_by_side.jpg", combined)

# Wait for a key press
cv2.waitKey(0)

# Close the window
cv2.destroyAllWindows()
