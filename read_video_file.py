# ____________________reading videos in opencv______________
import cv2
from vision_utils import rescale_img
capt=cv2.VideoCapture("/media/hari/My Passport1/test/cv/pexels-olya-kobruseva-6800632.mp4")
while True:
    succesfully_read,frame_data=capt.read()
    cv2.imshow("video_frames_read",frame_data)

    # rescaling the image with factor from comp utils

    cv2.imshow("rescaled",rescale_img(frame_data))
    #_____start



    #The ord() function returns the unicode of specific character returns the asciee number
    # I have added here e for the exit
    if cv2.waitKey(20) & 0xFF==ord('e'):
        break
# once the while loop failles it throws the assertion error


# Note if you get the asseertion failde error it states that the video file is unable to read in the given location
# release the capture and destroy all the videos
capt.release()
cv2.destroyAllWindows()
cv2.waitKey(0)


#__________________re_writig the video code______________

capt=cv2.VideoCapture("/media/hari/My Passport1/test/cv/pexels-olya-kobruseva-6800632.mp4")
while (capt.isOpened()):
    succesfully_read,frame_data=capt.read()
    # if needed you can add a if statement like if succesfully_read and else break
    cv2.imshow("video_frames_read",frame_data)
    #The ord() function returns the unicode of specific character returns the asciee number
    # I have added here e for the exit
    if cv2.waitKey(20) & 0xFF==ord('e'):
        break
# once the while loop failles it throws the assertion error


# Note if you get the asseertion failde error it states that the video file is unable to read in the given location
# release the capture and destroy all the videos
capt.release()
cv2.destroyAllWindows()
cv2.waitKey(0)


# python code to write a video
"""

# Create a VideoCapture object and read from input file

# If the input is the camera, pass 0 instead of the video file name

cap = cv2.VideoCapture('chaplin.mp4')

# Check if camera opened successfully

if (cap.isOpened() == False):
    print("Error opening video stream or file")

# Read until video is completed

while (cap.isOpened()):

    # Capture frame-by-frame

    ret, frame = cap.read()

    if ret == True:

        # Display the resulting frame

        cv2.imshow('Frame', frame)

        # Press Q on keyboard to  exit

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break



    # Break the loop

    else:

        break

# When everything done, release the video capture object

cap.release()

# Closes all the frames

cv2.destroyAllWindows()

"""

