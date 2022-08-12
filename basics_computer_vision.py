#_____________________computer vision basics__________________
#!pip install pandas
#! pip install opencv-python numpy pillow
#_________________import the libraries required over here
import cv2
import numpy as nmpy
import PIL
import os

# rename a file using python


#___________uncomment the below two lines of code if need to rename__________

#os.rename("ladybug-7284337_960_720.jpg","lady_bug.jpg")
#print("renamed the file")

print("succesfully imported the libraries with no errors")

# start the codes overs here

# storing a image array into some variable
read_arr=cv2.imread("lady_bug.jpg")
cv2.imshow("bug",cv2.imread("lady_bug.jpg"))

# wait until a key is pressed to exit
cv2.waitKey(0)



#__________________re_writig the video code______________

capt=cv2.VideoCapture("/media/hari/My Passport1/test/cv/pexels-olya-kobruseva-6800632.mp4")
while (capt.isOpened()):
    succesfully_read,frame_data=capt.read()
    resize_frame=rescale_img(frame_data,0.7)
    # if needed you can add a if statement like if succesfully_read and else break
    cv2.imshow("video_frames_read",frame_data)
    cv2.imshow("video_resized_data",resize_frame)
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

