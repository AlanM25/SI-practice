import cv2 

image = cv2.imread('flecha.jpg')
height, width = image.shape[:2]
cv2.imshow('Original image', image)

for i in range(360, 0, -1):
 
    center = (width/2, height/2)

    # using cv2.getRotationMatrix2D() to get the rotation matrix
    rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=90, scale=1)
    
    # rotate the image using cv2.warpAffine
    rotated_image = cv2.warpAffine(src=image, M=rotate_matrix, dsize=(width, height))
    
    # save the rotated image to disk
    cv2.imwrite('rotated_image.jpg', rotated_image)
    
    # Create a video capture object, in this case we are reading the video from a file
    vid_capture = cv2.VideoCapture('rotated_image.jpg')

    # Obtain frame size information using get() method
    frame_width = int(vid_capture.get(3))
    frame_height = int(vid_capture.get(4))
    frame_size = (frame_width,frame_height)
    fps = 20

    # Initialize video writer object
    output = cv2.VideoWriter('Prueba1.mp4', cv2.VideoWriter_fourcc('M','J','P','G'), 20, frame_size)
    
    while(vid_capture.isOpened()):
        # vid_capture.read() methods returns a tuple, first element is a bool 
        # and the second is frame
        ret, frame = vid_capture.read()
        if ret == True:
            output.write(frame)
            cv2.imshow('Frame',frame)
            # 20 is in milliseconds, try to increase the value, say 50 and observe
            key = cv2.waitKey(20)
        
        if key == ord('q'):
            cv2.imwrite('ultimoframe.jpg', frame)
            break
        else:
            break
 
# Release the video capture object
#vid_capture.release()
output.release()
cv2.destroyAllWindows()