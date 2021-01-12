import cv2
from mtcnn.mtcnn import MTCNN
detector = MTCNN()

img=cv2.imread("input & output/people.jpg")
location = detector.detect_faces(img)
if len(location) > 0:
    for face in location:
        x, y, width, height = face['box']
        x2, y2 = x + width, y + height
        cv2.rectangle(img, (x, y), (x2, y2), (0, 0, 255), 4)

cv2.imwrite("input & output/Outputfile.jpg",img)
print("The Image was successfully saved")
