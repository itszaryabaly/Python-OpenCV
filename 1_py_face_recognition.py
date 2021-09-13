import cv2


# print(cv2.__version__) for checking the version of opencv module
 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# resized = cv2.resize(img,  (300,250)) for resizing the image

img =  cv2.imread("img/people.jpg") #for checiking  the image and it can be opened

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(img,scaleFactor =1.05,minNeighbors = 5)
print(type(faces))
print(faces)

for x,y,w,h in faces:
   gray_img = cv2.rectangle(gray_img,(x,y), (x+w,y+h),(0,255,0),2)

cv2.imshow("Face Detect",gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# print(img.shape)
# print(type(img))
#  print(img)