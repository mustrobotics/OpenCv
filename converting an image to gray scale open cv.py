import cv2

# load the image
img =cv2.imread("//home/tootsie/Downloads//WhatsApp Image 2023-02-07 at 9.55.23 AM.jpeg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#DISPLAY THE ORIGINAL AND GRAY SCALE IMAGES
cv2.imshow ('original Image', img)
cv2.imshow('Grayscale Image',gray_img)

cv2.waitKey(0)
cv2.destroyAllWindows()