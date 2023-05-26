import cv2

# img = cv2.imread("../catsample.png")
# img = cv2.imread("../ok/dog/dogsample.png")
# img = cv2.imread("../dogsample2.png")
# img = cv2.imread("../dogsample3.png")
# img = cv2.imread("../dogsample4.png")
# img = cv2.imread("../dogsample5.png")
# img = cv2.imread("./ok/dog/1.jpg")
# img = cv2.imread("./ok/dog/2.jpg")
img = cv2.imread("./ok/dog/3.jpg")
# img = cv2.imread("./ok/dog/5.jpg")
# img = cv2.imread("./ok/dog/6.jpg")
# img = cv2.imread("./ok/dog/20.jpg")
# img = cv2.imread("../.png")

grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# custom_cascade = cv2.CascadeClassifier('./cascade/cascade.xml')
custom_cascade = cv2.CascadeClassifier('../haarcascade_eye.xml')
# custom_cascade = cv2.CascadeClassifier(
#     '../haarcascade_eye_tree_eyeglasses.xml')

custom_rect = custom_cascade.detectMultiScale(
    grayimg, scaleFactor=1.07, minNeighbors=2, minSize=(1, 1))

print("custom_rect↓")
print(custom_rect)

if len(custom_rect) > 0:
    print("恐らくここに来たということは正解という事")
    for rect in custom_rect:
        cv2.rectangle(img, tuple(rect[0:2]), tuple(
            rect[0:2]+rect[2:4]), (0, 255, 255), thickness=3)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
