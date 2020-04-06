import cv2 as cv
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
        center_x1 = int((x1 +x2)/2)
        center_y1 = int((0.9*y2) +(0.1*y1))
        axes_x1 = 100   
        axes_y1 = 50
        lip_ellipses.append((center_x1,center_x1, axes_x1,axes_y1 ))
    return lip_ellipses

 