import cv2
import numpy as np

# Read the image
image = cv2.imread("image.jpg")

# Resize image
image = cv2.resize(image, (400, 300))

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray, 100, 200)

# Convert edges to 3-channel image
edges_color = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

# Combine original and outline side by side
combined = np.hstack((image, edges_color))

# Display output
cv2.imshow("Original Image | Canny Outline", combined)

# Save output
cv2.imwrite("canny_output.jpg", combined)

# Wait and close
cv2.waitKey(0)
cv2.destroyAllWindows()
