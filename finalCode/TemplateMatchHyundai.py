import cv2
import numpy as np
import os

def matchLoop(img,template,parameter):
    # img = cv2.resize(cv2.imread('assets/soccer_practice.jpg', 0), (0, 0), fx=0.8, fy=0.8)
    # template = cv2.resize(cv2.imread('assets/shoe.PNG', 0), (0, 0), fx=0.8, fy=0.8)
    template=cv2.imread(template,0)
    h, w = template.shape[::1]
    parameter = "front" if parameter else "back"
    methodString = ["TM_CCOEFF", "TM_CCOEFF_NORMED", "TM_SQDIFF", "TM_SQDIFF_NORMED"]
    methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

    for index,method in enumerate(methods): # find match from all the 4 methods
        img2 = img.copy()  #create a copy to make rectangles
        result = cv2.matchTemplate(img2, template, method)  # match templates
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)  # in case of multiple find consider only min and max_loc
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:  # in min sq diff, we select edge points with min_loc as we aim to minimise the difference 
            location = min_loc
        else:
            location = max_loc
        
        bottom_right = (location[0] + w, location[1] + h)     # bottom right coordinates for the rectangle
        cv2.rectangle(img2, location, bottom_right, (255,255,0),2)
        windowName=parameter+methodString[index]
        cv2.imshow(windowName, img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


currentWorkingDirectory = os.getcwd()
imagePath=os.path.join(currentWorkingDirectory,'assets/testImages') 
templatePath=os.path.join(currentWorkingDirectory,'assets/templateImages') 
print(imagePath,templatePath)
templates=os.listdir(templatePath)
print(templates)
for image in os.listdir(imagePath):
    # print("inside for loop",image)
    if "." in image and image.split(".")[-1]=="jpg":
        imgPath=os.path.join(imagePath,image)
        img_rgb=cv2.imread(imgPath)
        img_g=cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)
        for template in templates:
             parameter = True if "front" in template else False
             matchLoop(img_g,os.path.join(templatePath,template),parameter)


'''
Template Matching through CV2

all methods through which we can match templates: 
# methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

best performing methods after testing:
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
'''