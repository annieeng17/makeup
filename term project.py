# from cmu_112_graphics import *
# from github
from __future__ import print_function
import cv2

import numpy as np
import cv2 as cv

import os

# local modules
from video import create_capture
from common import clock, draw_str

# scaleFactor-size of face is detected in the image if present, scaling image
# minNeighbors- number of neighbouring rectangles needed to remain detection
import basic_graphics
    

def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30),
                                     flags=cv.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

def draw_rects(img, rects, color):
    '''
    Draws the rectangles defined by rects on img

    param img: image to draw rectangles on
    param rects: list of rectangles to draw, format [(x1, y1, x2, y2), ...]
    param color: color to draw the rectangles, (R, G, B) coordinate.
    '''
    for x1, y1, x2, y2 in rects:
        # Drawing your face
        cv.rectangle(img, (x1, y1), (x2, y2), color, 2)

# own code created
def find_cheeks (rects):
    '''
    Converts the rectangles in rects to cheek rectangles

    param rects: list of face rectangles to find the cheeks in,
    format [(x1, y1, x2, y2), ...]

    return: A list of the cheek coordinates, format [(x1, y1, x2, y2), ...]
    '''
    cheek_rects = []

    for x1, y1, x2, y2 in rects:
    # Draw a box around your cheeks
        # Figure out where cheek coordinates are
        cheek_x1 = int(0.8*x1) + int(0.2*x2)
        cheek_y1 = int((y1 + y2) / 2)
        # Draw a box around your cheeks
        # Figure out where cheek coordinates are
        cheek_x2 = int(0.8*x1) + int(0.2*x2) + 20  
        cheek_y2 = int((y1 + y2) / 2) + 20

        cheek_rects.append(cheek_x1, cheek_y1, cheek_x1 + 10, cheek_y1 + 10)
        cheek_rects.append(cheek_x2, cheek_y2, cheek_x2 + 10, cheek_y2 + 10)

    return cheek_rects

# image = cv2.ellipse(image, center_coordinates, axesLength, 
        #    angle, startAngle, endAngle, color, thickness)
# draw lips
def find_lips(oval):
    lip_rect = []
    for x1, y1, x2, y2 in rects:
        lip_x1 = int(0.4*x2)
        lip_y1 = int(0.85*y1)
        lip_x2 = lip_x1 + 20
        lip_y2 = lip_y1 + 10
        lip_rect.append(lip_x1, lip_y1, lip_x2, lip_y2)
    
    return lip_rect
    while True:
        t = clock()
        rects = detect(gray,cascade)
        vis = img.copy()
        draw_rects(vis,rects,(255,0,255))
        lip_rects = find_lip(rects)
        draw_rects(vis,cheek_lip,(255,0,255))



# eyes = eyeCascade.detectMultiScale(roi_gray)
#     for (ex,ey,ew,eh) in eyes:
#         cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
#         cv2.putText(frame,'Eye',(x + ex,y + ey), 1, 1, (0, 255, 0)

def main():
    import sys, getopt

    args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade=', 'nested-cascade='])
    try:
        video_src = video_src[0]
    except:
        video_src = 0
    args = dict(args)
    cascade_fn = args.get('--cascade', "haarcascade_frontalface_alt.xml")
    nested_fn  = args.get('--nested-cascade', "haarcascade_eye.xml")

    cascade = cv.CascadeClassifier(cv.samples.findFile(cascade_fn))
    nested = cv.CascadeClassifier(cv.samples.findFile(nested_fn))

    import os
    print('>>>',os.listdir(os.getcwd()))
    cam = create_capture(video_src, fallback='synth:bg={}:noise=0.05'.format(cv.samples.findFile('lena.jpg')))

    while True:
        _ret, img = cam.read()
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        gray = cv.equalizeHist(gray)

        t = clock()
        rects = detect(gray, cascade)
        vis = img.copy()
        draw_rects(vis, rects, (0, 255, 0))

        cheek_rects = find_cheek(rects)
        draw_rects(vis,cheek_rects,(0,255,0))
        
        if not nested.empty():
            for x1, y1, x2, y2 in rects:
                roi = gray[y1:y2, x1:x2]
                vis_roi = vis[y1:y2, x1:x2]
                subrects = detect(roi.copy(), nested)
                draw_rects(vis_roi, subrects, (255, 0, 0))
        dt = clock() - t

        draw_str(vis, (20, 20), 'time: %.1f ms' % (dt*1000))
        cv.imshow('facedetect', vis)

        # press escape to close the camera
        if cv.waitKey(5) == 27:
            break

    print('Done')

# own code
# detecting cheek


if __name__ == '__main__':
    print(__doc__)
    main()
    cv.destroyAllWindows()
