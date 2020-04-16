import sys, getopt
import time
from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk
from constants import *
import cv2

from opencvLib import *
from makeupLib import *
# creating the stuff to put into tkinter
# CITATION: I got it the code off of this website for guidiance
# based off of https://www.tutorialsteacher.com/python/create-ui-using-tkinter-in-python
# and slightly altered

def detect(img, cascade):
    rects = cascade.detectMultiScale(
        img, 
        scaleFactor=1.3, 
        minNeighbors=4, 
        minSize=(30, 30), 
        flags=cv.CASCADE_SCALE_IMAGE
    )

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
# CITATION: used for drawing rects, ellipses and making lines
# used and altered from https://docs.opencv.org/3.4/dc/da5/tutorial_py_drawing_functions.html
# cv2.line(img, p1, p2, (255, 0, 0), 3)
def draw_triangle(img,triangle,color,thickness):
    '''

    Creates 3 coordinates defined by rects on img
    param img: image to draw rectangles on
    param rects: list of rectangles to draw, format [(x1, y1, x2, y2), ...]
    param color: color to draw the rectangles, (R, G, B) coordinate.
    '''
    for pt_x1, pt_y1, pt_x2, pt_y2, pt_x3, pt_y3, in triangle:
        cv2.line(img,(pt_x1, pt_y1),(pt_x2, pt_y2), color,thickness)
        cv2.line(img,(pt_x2, pt_y2),(pt_x3, pt_y3), color,thickness)
        cv2.line(img,(pt_x3, pt_y3),(pt_x1, pt_y1), color,thickness)


class App:
    # Keep track of what state your program is in
    # TODO: you should use an enum for this for different states
    _state = 0

    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.window.bind('<Escape>', lambda e: self.window.quit())
        self.video_source = video_source
        self._state = STATE_MENU
        # open video source (by default this will try to open the computer webcam)
        self.vid = VideoCapture(self.video_source)

        # creating label outside function, making it a global variable and can be used everywhere
        l1 = Label(self.window, text = "Application of Beauty", \
        width = 40, anchor = NW, font=("Helvetica", 16))
        l2 = Label(self.window,text = "Skin Tone Questionaire",   \
        width = 20, font = ("Helvetica", 16))
        l3 = Label(self.window,text = 'Look at the veins on your wrist',\
        width = 20, font = ("Helvetica", 16))
        l4 = Label(self.window, text = 'if you mostly see blue/purple veins, then you are cool toned', \
        width = 20, font = ("Helvetica", 16))
        l5 = Label(self.window, text = "if you mostly see green veins, \
        then you're warm toned", width = 20, font = ("Helvetica" , 16))
        l6 = Label(self.window, text = "if you mostly see a blend of \
        both blue/purple and green veins, then you're neutral toned", width = 20, \
        font = ("Helvetica, 16"))
        l7 = Label(self.window, text = 'Check in one of the boxes that accurately \
            matches your description', width = 20, font =("Helvetica, 16"))
        resultlabel1 = Label(self.window)

        # create button
        # CITATION: https://www.python-course.eu/tkinter_buttons.php

        # define font
        self.text = Text(self.window)
        self.myFont = Font(family = 'Times New Roman')
        self.text.configure(font = self.myFont)
        self._button = Button(self.window, 
                   text='Start', 
                   fg="black",
                   command=self.button_func)
        self._button.pack(side=RIGHT)
        self._button['font'] = self.myFont
        self._button1 = Button(self.window, 
                text='Back', 
                fg="black",
                command=self.button_func_back)
        # self._button1.pack(side=LEFT)
        self._button1['font'] = self.myFont
        
        # Create a canvas that can fit the above video source size
        self.canvas = Canvas(window, width = self.vid.width, height = self.vid.height)

        # Respond to clicks
        self.canvas.bind("<Button-1>", self.callback_mouse)

        self.canvas.pack()

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        self.update()

        self.window.mainloop()
    
    def update_fsm(self, action):
        '''
        State machine to decide the action of the program.

        Takes in an action and looks at the current state to determine
        what next state to go to and what actions to take

        :param action: The action that occurred
        '''

        if self._state == STATE_MENU:
            if action == ACTION_BUTTON_NEXT:
                self._state = STATE_SKIN_TONE
                self._button['text'] = 'Next'
                self._button1.pack(side=LEFT)
                # Label1.place_forget()

            elif action == ACTION_BUTTON_BACK:
                self._state = STATE_MENU
            
        elif self._state == STATE_SKIN_TONE:
            if action == ACTION_BUTTON_NEXT:
                self._state = STATE_FACE

            elif action == ACTION_BUTTON_BACK:
                self._state = STATE_MENU
                self._button1.pack_forget()

        elif self._state == STATE_FACE:
            if action == ACTION_BUTTON_NEXT:
                self._state = STATE_FACE_BOX

            elif action == ACTION_BUTTON_BACK:           
                self._state = STATE_SKIN_TONE
                if self.vid.isOpened():
                    self.vid.release()

        elif self._state == STATE_FACE_BOX:
            if action == ACTION_BUTTON_NEXT:
                self._state = STATE_FACE_BOX_RESULTS

            elif action == ACTION_BUTTON_BACK:
                self._state = STATE_FACE

        elif self._state == STATE_FACE_BOX_RESULTS:
            if action == ACTION_BUTTON_NEXT:
                self._state = STATE_SKIN_TONE

            elif action == ACTION_BUTTON_BACK:
                self._state = STATE_FACE_BOX

        elif self._state == STATE_SKIN_TONE:
            if action == ACTION_BUTTON_NEXT:
                self._state = STATE_EYES

            elif action == ACTION_BUTTON_BACK:
                self._state = STATE_FACE_BOX_RESULTS

        elif self._state == STATE_EYES:
            if action == ACTION_BUTTON_NEXT:
                self._state = STATE_EYES_RESULTS

            elif action == ACTION_BUTTON_BACK:
                self._state = STATE_SKIN_TONE

        elif self._state == STATE_EYES_RESULTS:  
            if action == ACTION_BUTTON_NEXT:
                self._state = STATE_BLUSH

            elif action == ACTION_BUTTON_BACK:
                self._state = STATE_EYES

        elif self._state == STATE_BLUSH:
            if action == ACTION_BUTTON_NEXT:
                self._state = STATE_BLUSH_RESULTS

            elif action == ACTION_BUTTON_BACK:
                self._state = STATE_EYES_RESULTS

        elif self._state == STATE_BLUSH_RESULTS:
            if action == ACTION_BUTTON_NEXT:
                self._state = STATE_HIGHLIGHTER

            elif action == ACTION_BUTTON_BACK:
                self._state = STATE_BLUSH

        elif self._state == STATE_HIGHLIGHTER:
            if action == ACTION_BUTTON_NEXT:
                self._state = STATE_HIGHLIGHTER_RESULTS

            elif action == ACTION_BUTTON_BACK:
                self._state = STATE_BLUSH_RESULTS
        
        elif self._state == STATE_HIGHLIGHTER_RESULTS:
            if action == ACTION_BUTTON_NEXT:
                self._state = STATE_CONTOUR

            elif action == ACTION_BUTTON_BACK:
                self._state = STATE_HIGHLIGHTER

        elif self._state == STATE_CONTOUR:
            if action == ACTION_BUTTON_NEXT:
                self._state = STATE_CONTOUR_RESULTS

            elif action == ACTION_BUTTON_BACK:
                self._state = STATE_HIGHLIGHTER_RESULTS
        
        elif self._state == STATE_CONTOUR_RESULTS:
            if action == ACTION_BUTTON_NEXT:
                self._state = STATE_LIP

            elif action == ACTION_BUTTON_BACK:
                self._state = STATE_CONTOUR

        elif self._state == STATE_LIP:
            if action == ACTION_BUTTON_NEXT:
                self._state = STATE_LIP_RESULTS 

            elif action == ACTION_BUTTON_BACK:
                self._state = STATE_CONTOUR_RESULTS

        elif self._state == STATE_LIP_RESULTS:
            if action == ACTION_BUTTON_BACK:
                self._state = STATE_LIP
        
        # Default case 
        # Likely something that's wrong
        else:
            self._state = self.vid.get_frame(self._state)

        print('Action: {} New State:{}'.format(action, self._state))


    def button_func(self): 
        '''
        Invoked when the start/next button is clicked
        '''
        self.update_fsm(ACTION_BUTTON_NEXT)
        
    def button_func_back(self):
        '''
        Invoked when the start/next button is clicked
        '''  
        self.update_fsm(ACTION_BUTTON_BACK)

    def callback_mouse(self, event):
        self._state += 1
        print("clicked at", event.x, event.y)

        
        '''
        You can do something like if the click is within some region,
        then change the state to something
        '''
        print("State is now {}".format(self._state))

# actually does graphics
    def update(self):
        '''
        Called every self.delay milliseconds
        '''
        if self._state == STATE_MENU:
            l1.grid(row=0, column=0)
            # self.canvas.delete("all")
            # self.title_label.place(x=250, y=0)
            resultlabel1.config(text=l1)
        elif self._state == STATE_SKIN_TONE:
            l2.grid(row=0,column=0)
            # self.Label1.place_forget()
            # self.canvas.delete("all")
            # self.title_label.place_forget()
            l3.grid(row=1,column=0)
            l4.grid(row=2,column=0)
            l5.grid(row=3,column=0)
            l6.grid(row=4,column=0)
            l7.grid(row=5,column=0)
 
            # Label1 = Label(self.window, text = f'{}')
            # Get a frame from the video source
            # Pass our current state to know which box to draw
            self.canvas.delete('all')
        else:
           
            Label1 = Label(self.window, text = "State:{}".format(self._state),\
                width = 40 , font = ("Helvetica",12))

            ret, frame = self.vid.get_frame(self._state)



            if ret:
                self.photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
                self.canvas.create_image(0, 0, image = self.photo, anchor = NW)

        self.window.after(self.delay, self.update)


class VideoCapture:
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        print(dir(self.vid))


        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

        # Create classifiers
        args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade=', 'nested-cascade='])
        args = dict(args)
        cascade_fn = args.get('--cascade', "haarcascade_frontalface_alt.xml")
        nested_fn  = args.get('--nested-cascade', "haarcascade_eye.xml")
        self.cascade = cv.CascadeClassifier(cv.samples.findFile(cascade_fn))
        self.nested = cv.CascadeClassifier(cv.samples.findFile(nested_fn))

    def get_frame(self,state):
        if self.vid.isOpened():
            ret, img = self.vid.read()

            # If the camera has successfully picked up an image
            if ret:
                # Process image from webcam
                # Process image
                gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                gray = cv.equalizeHist(gray)

                # Perform face detection
                rects = detect(gray, self.cascade)

                # Copy image so we can draw on it
                vis = img.copy()

                # Facial Feature detection
                # color formatting is (blue ,green, red)
                    
                if state == STATE_FACE_BOX:
                    draw_rects(vis, rects, (0, 255, 0))
                # elif state == STATE_SKIN_TONE:

                elif state == STATE_BLUSH:  
                    cheek_rects = find_cheeks(rects)   
                    draw_rects(vis,cheek_rects,(0, 0, 255))
                elif state == STATE_HIGHLIGHTER:
                    upper_cheeks = find_upper_cheeks(rects)
                    draw_triangle(vis,upper_cheeks,(255,255,0),thickness = 1)
                elif state == STATE_CONTOUR:
                    cheek_bones = find_cheek_bones(rects)
                    draw_triangle(vis,cheek_bones,(0,255,255),thickness = 1)
                elif state == STATE_LIP:
                    lip_ellipses = find_lips(rects)
                    draw_ellipses(vis, lip_ellipses,(255,0,255),thickness = 1)
                elif state == STATE_EYES:
                    # Eye detection
                    if not self.nested.empty():
                        for x1, y1, x2, y2 in rects:
                            roi = gray[y1:y2, x1:x2]
                            vis_roi = vis[y1:y2, x1:x2]
                            subrects = detect(roi.copy(), self.nested)
                            draw_rects(vis_roi, subrects, (255, 0, 0))

                # Flip image so that the feed is mirrored to the user
                vis = cv2.flip(vis, 1)

                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(vis, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
            cv2.destroyAllWindows()

if __name__ == '__main__':
    print('Application of Beauty \nPress <Esc> anytime to quit.')

    # Start tkinter
    App(Tk(), "Makeup")