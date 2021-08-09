#!/usr/bin/env python
# coding: utf-8

# # Intro
# 
# ## Tools:
#  - Git
#  - Colab
#  - Jupyter Notebook
#  - Web camera
# 
# We're going to be collecting images using our webcam, but you could just as easily do this with you phone or pre process video
# 
# we'll be using a github library called [labelimg](https://github.com/tzutalin/labelImg) to label our images
# 
# ## Best practices for labeling: 
# 1. Case sensitive - watch out! - log it in your readme
# 2. include pictures of objects at different angles and under different light conditions
# 3. start with 10-20 pictures in each class
# 4. keep your labels as tight (minimum margins) as possible
# 

# ## 1. Make sure your web camera is working

# Import opencv
import cv2 

framewidth = 640
frameheight = 480

# 0 - Laptop camera
# 1 - WebCam
cap = cv2.VideoCapture(1)  

cap.set(3, framewidth)  # width
cap.set(4, frameheight)  # height
cap.set(10, 10)  # brightneess

while True:
  is_success, img = cap.read()
#   print('is_success',is_success)
  cv2.imshow('Video', img)
  # Add a delay and keypress q to quit window
  if cv2.waitKey(25) & 0xFF == ord('q'):
    break

