import cv2

vid = cv2.VideoCapture(0)
  
while(True):
      
    frame = vid.read()[1]
    #frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #frame=cv2.threshold(src =frame, thresh = 0, maxval = 255, type = cv2.THRESH_OTSU+cv2.THRESH_BINARY)[1]
    #frame=cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                          #cv2.THRESH_BINARY, 199, 5)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
