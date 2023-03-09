import cv2 as cv
import os

# argument 0 is given to use the default camera of the laptop
camera = cv.VideoCapture(0)
# Now check if the camera object is created successfully
if not camera.isOpened():
    print("The Camera is not Opened....Exiting")
    exit()


# creating a list of lables "You could add as many you want"
Labels = ["ACT Nachos"]
# Now create folders for each label to store images
#for label in Labels:
 #   if not os.path.exists("C:\\Users\\gteja\\OneDrive\\Desktop\\New folder"):
  #      os.mkdir(label)

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
        # convert the image into gray format for fast caculation
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # display window with gray image
        cv.imshow("Video Window", gray)
        # resizing the image to store it
        gray = cv.resize(gray, (28, 28))
        # Store the image to specific label folder
        cv.imwrite('C:\\Users\\gteja\\OneDrive\\Desktop\\New folder' + folder+'\\img'+str(count)+'.png', gray)
        count = count+1
        # to quite the display window press 'q'
        if cv.waitKey(1) == ord('q'):
            break
# When everything done, release the capture
camera.release()
cv.destroyAllWindows()
