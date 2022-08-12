import cv2

def rescale_img(img_arr,scale_factor=0.5):
    width=int(img_arr.shape[1]*scale_factor)
    height=int(img_arr.shape[0]*scale_factor)
    # Linear interpolation----smooth but computationally expensive
    #return cv2.resize(img_arr,(width,height),interpolation=cv2.INTER_LINEAR)
    return cv2.resize(img_arr,(width,height),interpolation=cv2.INTER_AREA)

def chanage_resolution_live_feed(width_frame,height_frame,capture_obj,brightness_frame=10):
    capture_obj.set(3,width_frame)
    capture_obj.set(4,height_frame)
    capture_obj.set(10,brightness_frame)
    return capture_obj

# same as first function rescale_img with default interpolation
def resize_change_res(image_arr,width,height):
    resized = cv2.resize(image_arr, (width,height))
    return resized
