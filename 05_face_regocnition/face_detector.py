import cv2
from random import randrange

# trained_face_data is simply loading data of frontal faces from the library cv2
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Choose a single image to detect faces in. Loading image, using cv2 functions
# image = cv2.imread("many_faces.jpg")

"""Here instead to read a single image, we're going to iterate the video frames which basically are pictures
 "0" means it will get the default camera on our device. In the brackets we can put name on specific video file"""
webcam = cv2.VideoCapture(0)

while True:
    # Read the current frame
    successful_frame_read, frame = webcam.read()
    # The face recognition works in a gray scale manner. We should convert the image into black and white
    grayscaled_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    """Plugging the gray image(frame if we talking about video or webcam) into the detect algoritm. Pointing top left corner and bottom left corner of the
    rectangle around the detected face, no matter how big or small is the face on the picture. That's why is called MultiScale
    The output is a list with coordinates of every rectangle bottom right and upper left corner """
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_image)

    """ Looping through the face matches. In this case face is the tuple containg the needed info about the coordinates
 Draw rectangles around the faces. The first tuple is the coordinate of top left corner, the second tuple is the coordinates of the
 bottom right corner plus the width and hight of the rectangle
 the third tuple is RGB combination defines the color of the rectangle, whitch in this case I choose green
 and the last digit 2 means the thickness of the line drawing the rectangle"""
    for face in face_coordinates:
        (x, y, width, hight) = face
        cv2.rectangle(frame, (x, y), (x + width, y + hight), (randrange(256), randrange(256), randrange(256)), 2)

    # This one shows the loaded image or video or webcam in a new window named "Face Detector"
    cv2.imshow("Face Detector", frame)

    # function that pauses the execution of the code, keep the image open until you press any key to proceed the code
    # becouse without it it will execute the code in a split of a second and end the program
    key = cv2.waitKey(1)
    # To stop the loop and code execution we should press upper or lower Q
    if key == 83 or key == 113:
        break

# This function stops the camera
webcam.release()
print("It's ok for now")
