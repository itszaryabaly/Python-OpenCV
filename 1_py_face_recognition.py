import cv2
print("Module Imported Successfuly!")


img = cv2.imread("img/devil.jpg")


cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

