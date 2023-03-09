#Credits to creator(s) of this code implementation - https://www.analyticsvidhya.com/blog/2021/05/create-your-own-image-dataset-using-opencv-in-machine-learning/
import cv2 as cv

camera = cv.VideoCapture(0)

if not camera.isOpened():
    print("The Camera is not Opened....Exiting")
    exit()

Labels = ["colgate"]

for folder in Labels:

    count = 0

    print("Press 's' to start data collection for "+folder)
    userinput = input()
    if userinput != 's':
        print("Wrong Input..........")
        exit()

    while count < 20:

        status, frame = camera.read()

        if not status:
            print("Frame is not been captured..Exiting...")
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        cv.imshow("Video Window",hsv)

        hsv = cv.resize(hsv, (28,28))

        cv.imwrite('./dataset/' +
                   folder+'/img/img'+str(count)+'.png',hsv)
        count = count+1

        if cv.waitKey(1) == ord('q'):
            break

camera.release()
cv.destroyAllWindows()
