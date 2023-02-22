import cv2

# Load the image
img = cv2.imread('path/to/image.jpg')

# Define the coordinates of the region of interest (ROI)
x, y, w, h = 100, 100, 200, 200

# Crop the image
crop_img = img[y:y+h, x:x+w]

# Display the original and cropped image
cv2.imshow('Original Image', img)
cv2.imshow('Cropped Image', crop_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
