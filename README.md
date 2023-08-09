# TemplateCheckingUsingOpenCV
python code to check if a particular pattern is present in the image or not

Library Used: OpenCV

Concept: 
Template Matching is a method for searching and finding the location of a template image in a larger image. OpenCV comes with a function cv.matchTemplate() for this purpose. It simply slides the template image over the input image (as in 2D convolution) and compares the template and patch of input image under the template image. 

Methods:
There are different methods that can use for template Matching like 
#TM_CCOEFF
#TM_CCOEFF_NORMED
#TM_CCORR
#TM_CCORR_NORMED
#TM_SQDIFF
#TM_SQDIFF_NORMED

Project:
Using Open CV's template matching algorithm to identify logo in the car images.

Challenges:
1. for efficient template matching the template size and the focussed area size in the test image should exactly match as it undergoes a 2d Convulation process.
2. the template should be very similar to the logo. I faced a challenge in using the logo at the back for the car front.

How to run the code:
Please clone the repo. You can download the libraries from requirements.txt and then ls to "finalCode" folder to execute the main script.
ls is necessary because the code finds the test images folder by "os" library. thus your cwd needs to be finalCode.

Thankyou! Happy Learning
