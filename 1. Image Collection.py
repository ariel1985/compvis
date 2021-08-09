#!/usr/bin/env python
# coding: utf-8

# # 1. Import Dependencies
# Import opencv
import cv2 

# Import uuid
import uuid

# Import Operating System
import os

# Import time
import time


# # 2. Define Images to Collect

labels = ['thumbsup', 'thumbsdown', 'livelong']
number_imgs = 3

# # 3. Setup Folders 

IMAGES_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'collectedimages')

# # 4. Capture Images
for label in labels:
    cap = cv2.VideoCapture(1)
    seconds = 5
    print('Start Collecting images for {} in {} seconds'.format(label, seconds))
    time.sleep(seconds)  # you might want to pause for more
    for imgnum in range(number_imgs):
        print('Collecting image {}'.format(imgnum))
        ret, frame = cap.read()
        imgname = os.path.join(IMAGES_PATH,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)
        time.sleep(4)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()


TRAIN_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'train')
TEST_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'test')
ARCHIVE_PATH = os.path.join('Tensorflow', 'workspace', 'images', 'archive.tar.gz')


