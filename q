[1mdiff --git a/constants.py b/constants.py[m
[1mindex 3abb9b9..5575b56 100644[m
[1m--- a/constants.py[m
[1m+++ b/constants.py[m
[36m@@ -14,6 +14,7 @@[m [mSTATE_CONTOUR = 12[m
 STATE_CONTOUR_RESULTS = 13[m
 STATE_LIP = 14[m
 STATE_LIP_RESULTS = 15[m
[32m+[m[32mSTATE_RESULTS = 16[m
 [m
 # Button action identifiers[m
 ACTION_BUTTON_NEXT  = 1[m
[1mdiff --git a/main.py b/main.py[m
[1mindex d329212..dd69d43 100644[m
[1m--- a/main.py[m
[1m+++ b/main.py[m
[36m@@ -149,7 +149,7 @@[m [mclass App:[m
         self.l12 = Label(self.window, text = f'Your closest match is:{self.vid.face_results}')[m
         self.recommended_color = None[m
         self.l13 = Label(self.window, text = f'Your closest makeup color match is:{self.recommended_color}')[m
[31m-        self.l14 = Label(self.window, image = self.photo2)[m
[32m+[m[32m        self.l14 = Label(self.window, image = self.photo2)git[m[41m [m
         # create button[m
         # CITATION: https://www.python-course.eu/tkinter_buttons.php[m
 [m
[36m@@ -260,6 +260,7 @@[m [mclass App:[m
         elif self._state == STATE_EYES:[m
             if action == ACTION_BUTTON_NEXT:[m
                 self._state = STATE_EYES_RESULTS[m
[32m+[m[32m                self.color_slider.grid()[m
 [m
             elif action == ACTION_BUTTON_BACK:[m
                 self._state = STATE_FACE_BOX_RESULTS[m
[36m@@ -274,55 +275,70 @@[m [mclass App:[m
         elif self._state == STATE_BLUSH:[m
             if action == ACTION_BUTTON_NEXT:[m
                 self._state = STATE_BLUSH_RESULTS[m
[32m+[m[32m                self.color_slider.grid()[m
 [m
             elif action == ACTION_BUTTON_BACK:[m
                 self._state = STATE_EYES_RESULTS[m
[32m+[m[32m                self.color_slider.grid_remove()[m
 [m
         elif self._state == STATE_BLUSH_RESULTS:[m
             if action == ACTION_BUTTON_NEXT:[m
                 self._state = STATE_HIGHLIGHTER[m
[32m+[m[32m                self.color_slider.grid_remove()[m
 [m
             elif action == ACTION_BUTTON_BACK:[m
                 self._state = STATE_BLUSH[m
[32m+[m[32m                self.color_slider.grid_remove()[m
 [m
         elif self._state == STATE_HIGHLIGHTER:[m
             if action == ACTION_BUTTON_NEXT:[m
                 self._state = STATE_HIGHLIGHTER_RESULTS[m
[32m+[m[32m                self.color_slider.grid()[m
 [m
             elif action == ACTION_BUTTON_BACK:[m
                 self._state = STATE_BLUSH_RESULTS[m
[32m+[m[32m                self.color_slider.grid()[m
         [m
         elif self._state == STATE_HIGHLIGHTER_RESULTS:[m
             if action == ACTION_BUTTON_NEXT:[m
                 self._state = STATE_CONTOUR[m
[32m+[m[32m                self.color_slider.grid_remove()[m
 [m
             elif action == ACTION_BUTTON_BACK:[m
                 self._state = STATE_HIGHLIGHTER[m
[32m+[m[32m                self.color_slider.grid_remove()[m
 [m
         elif self._state == STATE_CONTOUR:[m
             if action == ACTION_BUTTON_NEXT:[m
                 self._state = STATE_CONTOUR_RESULTS[m
[32m+[m[32m                self.color_slider.grid()[m
 [m
             elif action == ACTION_BUTTON_BACK:[m
                 self._state = STATE_HIGHLIGHTER_RESULTS[m
[31m-        [m
[32m+[m[32m                self.color_slider.grid()[m
[32m+[m
         elif self._state == STATE_CONTOUR_RESULTS:[m
             if action == ACTION_BUTTON_NEXT:[m
                 self._state = STATE_LIP[m
[32m+[m[32m                self.color_slider.grid_remove()[m
 [m
             elif action == ACTION_BUTTON_BACK:[m
                 self._state = STATE_CONTOUR[m
[32m+[m[32m                self.color_slider.grid_remove()[m
 [m
         elif self._state == STATE_LIP:[m
             if action == ACTION_BUTTON_NEXT:[m
                 self._state = STATE_LIP_RESULTS [m
[32m+[m[32m                self.color_slider.grid()[m
 [m
             elif action == ACTION_BUTTON_BACK:[m
                 self._state = STATE_CONTOUR_RESULTS[m
[32m+[m[32m                self.color_slider.grid()[m
 [m
         elif self._state == STATE_LIP_RESULTS:[m
             if action == ACTION_BUTTON_BACK:[m
                 self._state = STATE_LIP[m
[32m+[m[32m                self.color_slider.grid_remove()[m
         [m
         # Default case [m
         # Likely something that's wrong[m
[1mdiff --git a/term project.py b/term project.py[m
[1mdeleted file mode 100644[m
[1mindex 6f16a00..0000000[m
[1m--- a/term project.py[m	
[1m+++ /dev/null[m
[36m@@ -1,116 +0,0 @@[m
[31m-# from cmu_112_graphics import *[m
[31m-# from github[m
[31m-from __future__ import print_function[m
[31m-import cv2[m
[31m-[m
[31m-import numpy as np[m
[31m-import cv2 as cv[m
[31m-from opencvLib import *[m
[31m-[m
[31m-import os[m
[31m-[m
[31m-# local modules[m
[31m-from video import create_capture[m
[31m-from common import clock, draw_str[m
[31m-[m
[31m-# scaleFactor-size of face is detected in the image if present, scaling image[m
[31m-[m
[31m-# minNeighbors- number of neighbouring rectangles needed to remain detection[m
[31m-    [m
[31m-def detect(img, cascade):[m
[31m-    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30),[m
[31m-                                     flags=cv.CASCADE_SCALE_IMAGE)[m
[31m-    if len(rects) == 0:[m
[31m-        return [][m
[31m-    rects[:,2:] += rects[:,:2][m
[31m-    return rects[m
[31m-[m
[31m-def draw_rects(img, rects, color):[m
[31m-    '''[m
[31m-    Draws the rectangles defined by rects on img[m
[31m-[m
[31m-    param img: image to draw rectangles on[m
[31m-    param rects: list of rectangles to draw, format [(x1, y1, x2, y2), ...][m
[31m-    param color: color to draw the rectangles, (R, G, B) coordinate.[m
[31m-    '''[m
[31m-    for x1, y1, x2, y2 in rects:[m
[31m-        # Drawing your face[m
[31m-        cv.rectangle(img, (x1, y1), (x2, y2), color, 2)[m
[31m-[m
[31m-def draw_ellipses(img, ellipses, color,thickness):[m
[31m-    '''[m
[31m-    Draws the rectangles defined by rects on img[m
[31m-[m
[31m-    param img: image to draw rectangles on[m
[31m-    param rects: list of rectangles to draw, format [(x1, y1, x2, y2), ...][m
[31m-    param color: color to draw the rectangles, (R, G, B) coordinate.[m
[31m-    '''[m
[31m-    for center_x1, center_y1, axes_x1, axes_y1 in ellipses:[m
[31m-        # Drawing your face[m
[31m-        cv.ellipse(img,(center_x1,center_y1),(axes_x1,axes_y1), \[m
[31m-        0,0,360,color,thickness)[m
[31m-[m
[31m-# eyes = eyeCascade.detectMultiScale(roi_gray)[m
[31m-#     for (ex,ey,ew,eh) in eyes:[m
[31m-#         cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)[m
[31m-#         cv2.putText(frame,'Eye',(x + ex,y + ey), 1, 1, (0, 255, 0)[m
[31m-[m
[31m-def main():[m
[31m-    import sys, getopt[m
[31m-[m
[31m-    args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade=', 'nested-cascade='])[m
[31m-    try:[m
[31m-        video_src = video_src[0][m
[31m-    except:[m
[31m-        video_src = 0[m
[31m-    args = dict(args)[m
[31m-    cascade_fn = args.get('--cascade', "haarcascade_frontalface_alt.xml")[m
[31m-    nested_fn  = args.get('--nested-cascade', "haarcascade_eye.xml")[m
[31m-[m
[31m-    cascade = cv.CascadeClassifier(cv.samples.findFile(cascade_fn))[m
[31m-    nested = cv.CascadeClassifier(cv.samples.findFile(nested_fn))[m
[31m-[m
[31m-    import os[m
[31m-    print('>>>',os.listdir(os.getcwd()))[m
[31m-    cam = create_capture(video_src, fallback='synth:bg={}:noise=0.05'.format(cv.samples.findFile('lena.jpg')))[m
[31m-[m
[31m-    while True:[m
[31m-        _ret, img = cam.read()[m
[31m-        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)[m
[31m-        gray = cv.equalizeHist(gray)[m
[31m-[m
[31m-        t = clock()[m
[31m-        rects = detect(gray, cascade)[m
[31m-        vis = img.copy()[m
[31m-        # color formatting is (blue ,green, red)[m
[31m-        draw_rects(vis, rects, (0, 255, 0))[m
[31m-        cheek_rects = find_cheeks(rects)[m
[31m-        draw_rects(vis,cheek_rects,(0, 0, 255))[m
[31m-        lip_ellipses = find_lips(rects)[m
[31m-        draw_ellipses(vis, lip_ellipses,(255,0,255),thickness = 1)[m
[31m-        [m
[31m-        if not nested.empty():[m
[31m-            for x1, y1, x2, y2 in rects:[m
[31m-                roi = gray[y1:y2, x1:x2][m
[31m-                vis_roi = vis[y1:y2, x1:x2][m
[31m-                subrects = detect(roi.copy(), nested)[m
[31m-                draw_rects(vis_roi, subrects, (255, 0, 0))[m
[31m-        dt = clock() - t[m
[31m-[m
[31m-        draw_str(vis, (20, 20), 'time: %.1f ms' % (dt*1000))[m
[31m-        cv.imshow('facedetect', vis)[m
[31m-[m
[31m-        # press escape to close the camera[m
[31m-        if cv.waitKey(5) == 27:[m
[31m-            break[m
[31m-[m
[31m-    print('Done')[m
[31m-[m
[31m-# own code[m
[31m-# detecting cheek[m
[31m-[m
[31m-[m
[31m-if __name__ == '__main__':[m
[31m-    print(__doc__)[m
[31m-    main()[m
[31m-    cv.destroyAllWindows()[m
