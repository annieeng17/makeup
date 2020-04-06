# from cmu_112_graphics import *
# from github
from __future__ import print_function
import cv2

import numpy as np
import cv2 as cv
from opencvLib import *

import os

# local modules
from video import create_capture
from common import clock, draw_str

# scaleFactor-size of face is detected in the image if present, scaling image

# minNeighbors- number of neighbouring rectangles needed to remain detection
    
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

def draw_ellipses(img, ellipses, color,thickness):
    '''
    Draws the rectangles defined by rects on img

    param img: image to draw rectangles on
    param rects: list of rectangles to draw, format [(x1, y1, x2, y2), ...]
    param color: color to draw the rectangles, (R, G, B) coordinate.
    '''
    for center_x1, center_y1, axes_x1, axes_y1 in ellipses:
        # Drawing your face
        cv.ellipse(img,(center_x1,center_y1),(axes_x1,axes_y1), \
        0,0,360,color,thickness)

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
        # color formatting is (blue ,green, red)
        draw_rects(vis, rects, (0, 255, 0))
        cheek_rects = find_cheeks(rects)
        draw_rects(vis,cheek_rects,(0, 0, 255))
        lip_ellipses = find_lips(rects)
        draw_ellipses(vis, lip_ellipses,(255,0,255),thickness = 1)
        
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
