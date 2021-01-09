import cv2

# Opens the Video file
# cap=cv2.VideoCapture(r"D:\mscs\thesis\dataset\Sugarcane.MOV")
cap=cv2.VideoCapture(r"C:\Users\HP\Downloads\Video\_Getintopc.com_uTorrent_3.5.5.mp4")
i = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    cap.set(cv2.CAP_PROP_POS_MSEC, (i * 100))
    if ret == False:
        break
    cv2.imwrite(''+str(i)+ '.jpg', frame)
    i += 1

cap.release()
cv2.destroyAllWindows()