import cv2

#img = cv2.imread("glad.PNG")

#cv2.imshow("Gladiatus",img)

#video = cv2.VideoCapture("montage.mp4")

#while True:
    #success, videom = video.read()
    #cv2.imshow("Video", videom)
    #if cv2.waitKey(5) & 0xFF == ord('q'):       # Bi şekilde iş yapıyo q için, delay da lazım oynatma için
        #break

kamera = cv2.VideoCapture(0)
print(kamera.isOpened())
kamera.set(3,640)
kamera.set(4,480)




