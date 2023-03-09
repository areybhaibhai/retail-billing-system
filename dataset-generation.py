import cv2 as cv

# argument 0 is given to use the default camera of the laptop
camera = cv.VideoCapture(0)
# Now check if the camera object is created successfully
if not camera.isOpened():
    print("The Camera is not Opened....Exiting")
    exit()
# creating a list of lables "You could add as many you want"
Labels = ["colgate"]

for folder in Labels:
    # using count variable to name the images in the dataset.
    count = 0
    # Taking input to start the capturing
    print("Press 's' to start data collection for"+folder)
    userinput = input()
    if userinput != 's':
        print("Wrong Input..........")
        exit()
    # clicking 200 images per label, you could change as you want.
    while count < 20:
        # read returns two values one is the exit code and other is the frame
        status, frame = camera.read()
        # check if we get the frame or not
        if not status:
            print("Frame is not been captured..Exiting...")
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        #display window with gray image
        cv.imshow("Video Window",hsv)
        #resizing the image to store it
        hsv = cv.resize(hsv, (28,28))
        # Store the image to specific label folder
        cv.imwrite('C:/Users/Harsha/OneDrive/Documents/Projects/Retail Billing System/dataset/' +
                   folder+'/img/img'+str(count)+'.png',hsv)
        count = count+1
        # to quite the display window press 'q'
        if cv.waitKey(1) == ord('q'):
            break
# When everything done, release the capture
camera.release()
cv.destroyAllWindows()