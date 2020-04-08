import cv2 as cv
import numpy as np
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
        cheek_x1 = int(0.8*x1) + int(0.4*x2) - 95
        cheek_y1 = int((y1 + y2) / 2) - 10
        # Draw a box around your cheeks
        # Figure out where cheek coordinates are
        cheek_x2 = int(0.8*x1) + int(0.4*x2) - 15
        cheek_y2 = int((y1 + y2) / 2) - 10

        cheek_rects.append((cheek_x1, cheek_y1, cheek_x1 + 35, cheek_y1 + 35))
        cheek_rects.append((cheek_x2, cheek_y2, cheek_x2 + 35, cheek_y2 + 35))

    return cheek_rects

# image = cv2.ellipse(image, center_coordinates, axesLength, 
#    angle, startAngle, endAngle, color, thickness)

# img – Image where the circle is drawn.
    
def find_lips(rects):
    lip_ellipses = []
    for x1, y1, x2, y2 in rects:
        delta = -20   
        center_x1 = int((x1 + x2)/2) 
        center_y1 = int((0.9*y2) +(0.1*y1)) + delta
        axes_x1 = 25  
        axes_y1 = 12
        lip_ellipses.append((center_x1,center_y1, axes_x1,axes_y1 ))
    return lip_ellipses

# algorithm used to reflect shape onto opposite side of face  
# finding distance between x coordinate and midpoint, then doubling 
# distance and adding that onto corresponding x coordinate
def find_upper_cheeks(rects):
    upper_cheeks = []
    for x1, y1, x2, y2 in rects:
        delta = -10
        delta_2 = 5
        pt_1x = int(0.2*x1) + int(0.8*x2) + delta_2
        pt_1y = int(0.6*y1) + int(0.4*y2) + delta
        pt_2x = int(0.1*x1) + int(0.9*x2) + delta_2
        pt_2y = int(0.5*y1) + int(0.5*y2) + delta
        pt_3x = int(0.3*x1) + int(0.7*x2) + delta_2
        pt_3y = int(0.4*y1) + int(0.6*y2) + delta
        midpoint = int((x1 + x2)/2)
        distance_1 = midpoint - pt_1x
        distance_2 = midpoint - pt_2x
        distance_3 = midpoint - pt_3x
        reflect_1x = 2*(distance_1) + (pt_1x)
        reflect_2x = 2*(distance_2) + (pt_2x)
        reflect_3x = 2*(distance_3) + (pt_3x)
        upper_cheeks.append((pt_1x,pt_1y, pt_2x,pt_2y , pt_3x,pt_3y))
        upper_cheeks.append((reflect_1x,pt_1y, reflect_2x,pt_2y,reflect_3x,pt_3y))
        
    return upper_cheeks

def find_cheek_bones(rects):
    cheek_bones = []
    for x1, y1, x2, y2 in rects:
        delta = 20
        delta_2 = 5
        pt_1x = int(0.1*x1) + int(0.9*x2) + delta_2
        pt_1y = int(0.6*y1) + int(0.4*y2) + delta
        pt_2x = int(0.1*x1) + int(0.9*x2) + delta_2
        pt_2y = int(0.5*y1) + int(0.5*y2) + delta
        pt_3x = int(0.3*x1) + int(0.7*x2) + delta_2
        pt_3y = int(0.4*y1) + int(0.6*y2) + delta
        midpoint = int((x1 + x2)/2)
        distance_1 = midpoint - pt_1x
        distance_2 = midpoint - pt_2x
        distance_3 = midpoint - pt_3x
        reflect_1x = 2*(distance_1) + (pt_1x)
        reflect_2x = 2*(distance_2) + (pt_2x)
        reflect_3x = 2*(distance_3) + (pt_3x)
        cheek_bones.append((pt_1x,pt_1y, pt_2x,pt_2y , pt_3x,pt_3y))
        cheek_bones.append((reflect_1x,pt_1y, reflect_2x,pt_2y, reflect_3x,pt_3y))
    
    return cheek_bones

def find_avg_color(img, x, y):
    # turns into a numpy list, better than normal lists. can't do in python
    delta = 3
    upperLeft = np.array(img[y-delta,x-delta])
    upperRight = np.array(img[y-delta,x+delta])
    lowerLeft = np.array(img[y+delta, x-delta])
    lowerRight = np.array(img[y+delta, x+delta])
    average = (upperLeft + upperRight+ lowerLeft+ lowerRight)/4
    return average
