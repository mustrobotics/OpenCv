import cv2

# Load the image
img = cv2.imread('path/to/image.jpg')

# Flip the image horizontally
flipped_img = cv2.flip(img, 1)

# Flip the image vertically
# flipped_img = cv2.flip(img, 0)

# Flip the image horizontally and vertically
# flipped_img = cv2.flip(img, -1)

# Display the original and flipped image
cv2.imshow('Original Image', img)
cv2.imshow('Flipped Image', flipped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
