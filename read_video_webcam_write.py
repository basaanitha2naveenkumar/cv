# import the libraries you require
import cv2
#import numpy




#_____________________python code to write a video_____________________
# create the video object with internal webcam

capt = cv2.VideoCapture(0)
# cross verification
if (capt.isOpened() == False):
    print("unable to detect the camera")
# print all the properties of camera
# showing values of the properties
print("frame width= '{}'".format(capt.get(cv2.CAP_PROP_FRAME_WIDTH)))
print("frame height= : '{}'".format(capt.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print("frames per second : '{}'".format(capt.get(cv2.CAP_PROP_FPS)))
print("pso_msec : '{}'".format(capt.get(cv2.CAP_PROP_POS_MSEC)))
#print("CAP_PROP_FRAME_COUNT  : '{}'".format(capt.get(cv2.CAP_PROP_FRAME_COUNT)))
print("brightness= '{}'".format(capt.get(cv2.CAP_PROP_BRIGHTNESS)))
print("contrast= '{}'".format(capt.get(cv2.CAP_PROP_CONTRAST)))
print("saturation= '{}'".format(capt.get(cv2.CAP_PROP_SATURATION)))
print("hue= '{}'".format(capt.get(cv2.CAP_PROP_HUE)))
print("gain= '{}'".format(capt.get(cv2.CAP_PROP_GAIN)))
#print("CAP_PROP_CONVERT_RGB : '{}'".format(capt.get(cv2.CAP_PROP_CONVERT_RGB)))

# 30 is frames per second

# here the fourcc is the name of the codec
output_vid = cv2.VideoWriter('output_video_created.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (int(capt.get(3)), int(capt.get(4))))

while (True):

    ret_bol, frame_read = capt.read()

    if ret_bol == True:


        output_vid.write(frame_read)



        cv2.imshow(' video_frame_read_succesfully', frame_read)



        if cv2.waitKey(1) & 0xFF == ord('e'):
            break




    else:

        break

capt.release()
output_vid.release()
cv2.destroyAllWindows()