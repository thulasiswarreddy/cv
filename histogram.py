import cv2
import numpy as np

# Read the image
image = cv2.imread("image.jpg")

# Resize image
image = cv2.resize(image, (400, 300))

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply histogram equalization
equalized = cv2.equalizeHist(gray)

# Convert equalized image to 3-channel
equalized_color = cv2.cvtColor(equalized, cv2.COLOR_GRAY2BGR)

# Convert original grayscale to 3-channel
gray_color = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

# Combine side by side
combined = np.hstack((gray_color, equalized_color))

# Display
cv2.imshow("Original | Histogram Equalized", combined)

# Save output
cv2.imwrite("histogram_equalized.jpg", combined)

# Wait and close
cv2.waitKey(0)
cv2.destroyAllWindows()
