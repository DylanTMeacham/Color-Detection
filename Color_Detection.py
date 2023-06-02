import cv2
import numpy as np

def _in_Color_Detection():

    cap = cv2.VideoCapture(0)

    while True:
    
        _, frame = cap.read()
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        #Set to red - Cone - hsv
        lower_Cone_values1 = np.array([150, 100, 100])
        upper_Cone_values1 = np.array([255, 255, 255])

        #Set to green/light blue - Cube - hsv
        lower_Cube_values = np.array([70, 100, 100])
        upper_Cube_values = np.array([150, 255, 255])
        
        #Defines Variables for each objects mask
        cone_mask = cv2.inRange(hsv, lower_Cone_values1, upper_Cone_values1)
        cube_mask = cv2.inRange(hsv, lower_Cube_values, upper_Cube_values)
        
        #Defines variables for each object result
        cone_res = cv2.bitwise_and(frame, frame, mask = cone_mask)
        cube_res = cv2.bitwise_and(frame, frame, mask = cube_mask)

        contours, _ = cv2.findContours(cone_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours1, _ = cv2.findContours(cube_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            
            #Calculate area and remove unnecessary 
            area = cv2.contourArea(cnt)
            
            #Draws a rectangle where frame detects color if the are of the color is less than 100
            #if area < 100:
                #cv2.drawContours(frame,[cnt], -1, (0, 0, 255), 2)
                #x, y, w, h = cv2.boundingRect(cnt)
                #cv2.rectangle(cone_res, (x, y), (x +w, y + h), (0, 0, 255), 3)
        
        for cnt1 in contours1:

            area1 = cv2.contourArea(cnt1)
            
            #if area1 < 100:
                #cv2.drawContours(frame,[cnt1], -1, (0, 0, 255), 2)
                #x, y, w, h = cv2.boundingRect(cnt1)
                #cv2.rectangle(cube_mask, (x, y), (x +w, y + h), (0, 0, 255), 3)
        
        cv2.imshow('Frame', frame)
        #cv2.imshow('Cone Mask', cone_mask)
        cv2.imshow(' Cone Result', cone_res)
        #cv2.imshow('Cube Mask', cube_mask)
        cv2.imshow('Cube Results', cube_res)

        key = cv2.waitKey(1)
        
        #Terminate if the escape key is pressed
        if key == 27:
            break

    cv2.destroyAllWindows()
    cap.release()
    
def Color_Detection():
    try:
        while True:
            _in_Color_Detection()
    except StopIteration:
        pass
    
if __name__ == "__main__":
    Color_Detection()
