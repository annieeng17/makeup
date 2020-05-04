import sys, getopt
from time import time
from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk
from constants import *
import cv2
from opencvLib import *
from makeupLib import *
from playsound import playsound

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
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

class App:
    # Keep track of what state your program is in
    _state = 0

    def __init__(self, window, window_title, video_source = 0): # many video sources, which camera are we using
        self.window = window
        self.window.minsize(800,700) 
        # self.window.maxsize(900,700)
        self.window.title(window_title)
        self.window.bind('<Escape>', lambda e: self.window.quit()) # can't write def in one line, make it as e
        self.video_source = video_source
        # citation: https://pythonbasics.org/python-play-sound/
        playsound('Zora.mp3', False)
        self._state = STATE_MENU
        self._tone = None
        # self._face_feature = FACE
        self._button_last_clicked = time()
        # open video source (by default this will try to open the computer webcam)
        self.vid = VideoCapture(self.video_source)
        self.window.configure(bg ='RosyBrown1')
        # creating label outside function, making it a global variable and can be used everywhere
        self.Heading1 = Label(self.window, text = "State:{}".format(self._state),\
        width = 40 , font = ("Helvetica",20), bg = 'RosyBrown1', pady = 2)
        self.photo1 = Image.open('Cover.png')
        self.photo1 = self.photo1.resize((800, 600),Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(self.photo1)
        self.photo2 = Image.open('Questionnaire.png')
        self.photo2 = self.photo2.resize((800, 500),Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(self.photo2)
        self.photo3 = Image.open('Last_Page.png')
        self.photo3 = self.photo3.resize((800, 500),Image.ANTIALIAS)
        self.photo3 = ImageTk.PhotoImage(self.photo3)
        self.l11 = Label(self.window, image = self.photo1)
        self.l12 = Label(self.window, text = f'Your closest match is: {self.vid.face_results}')
        self.recommended_color = None
        self.l13 = Label(self.window, text = f'Your closest makeup color match is: {self.vid.recommended_color}')
        # self.l13 = Label(self.window, text = '')
        self.l14 = Label(self.window, image = self.photo2)
        self.l15 = Label(self.window, image = self.photo3)
        self.color_slider = Scale(self.window, from_=0, to = 100, orient= HORIZONTAL, command = self.update_slider_value)
        self.l16 = Label(self.window, text = f' Your overall makeup results are: {self.vid.recommended_color_list}')
        # define font
        self.text = Text(self.window)
        self.myFont = Font(family = 'New Courier')
        self.text.configure(font = self.myFont)

        ## Create buttons
        # CITATION: https://www.python-course.eu/tkinter_buttons.php
        self._button_start = Button(self.window, 
                   text = 'Start', 
                   fg = "black",
                   bg ='lavender',
                   command=self.button_func)
        self._button_start['font'] = self.myFont
        self._button_next = Button(self.window, 
                   text = 'Next', 
                   fg = "black",
                   bg ='lavender',
                   command=self.button_func)
        self._button_next['font'] = self.myFont
        self._button_back = Button(self.window, 
                text = 'Back', 
                fg = "black",
                bg ='lavender',
                command=self.button_func_back)
        self._button_back['font'] = self.myFont
        self._button_cool = Button(self.window,
                text = 'Cool', 
                fg = "black",
                bg ='lavender',
                command= lambda: self.button_func_tone(SKINTONE_COOL))
        self._button_warm = Button(self.window,
                text = 'Warm', 
                fg = "black",
                bg ='lavender',
                command = lambda:self.button_func_tone(SKINTONE_WARM))
        self._button_neutral = Button(self.window,
                text = 'Neutral', 
                fg = "black",
                bg ='lavender',
                command = lambda: self.button_func_tone(SKINTONE_NEUTRAL))
        self._button_start.grid(row = 5, column = 0)       
        
        # Create a canvas that can fit the above video source size
        # CITATION: https://solarianprogrammer.com/2018/04/21/python-opencv-show-video-tkinter-window/
        # used and altered accordingly
        self.canvas = Canvas(window, width = self.vid.width, height = self.vid.height)

        # Respond to clicks
        self.l11.grid(row = 0, column = 0)
        rect = self.canvas.create_rectangle(50,25,150,75,fill = 'RosyBrown1')

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
                self.l11.grid_remove()
                self.l14.grid()

                self.Heading1.grid_remove()
                self.l12.grid_remove()
                self.l13.grid_remove()
                self.l14.grid(row = 1, column = 1)
                self._button_start.grid_remove()

                # Buttons for the skin tone menu
                self._button_next.grid(row = 1, column = 2)
                self._button_back.grid(row = 1, column = 0)
                self._button_cool.grid(row = 0, column = 0)
                self._button_neutral.grid(row = 0, column = 1)
                self._button_warm.grid(row = 0, column = 2)

            elif action == ACTION_BUTTON_BACK:
                self._state = STATE_MENU
                self.Heading1.grid_remove()
                self._button_cool.grid_remove()
                self._button_neutral.grid_remove()
                self._button_warm.grid_remove()
                
                self.l12.grid_remove()
                self.l13.grid_remove()
                self.l14.grid_remove()
            
        elif self._state == STATE_SKIN_TONE:
            if action == ACTION_BUTTON_NEXT:
                # you have to click an undertone or else you can't proceed forward with the program
                if self._tone == None:
                    return None
                else:
                    self._state = STATE_FACE
                    self.canvas.grid(row = 1, column = 1)
                    self.Heading1.grid_remove()
                    self._button_cool.grid_remove()
                    self._button_neutral.grid_remove()
                    self._button_warm.grid_remove()

                self.l12.grid_remove()
                self.l13.grid_remove()
                self.l14.grid_remove()
                self.l14.grid_remove()

            elif action == ACTION_BUTTON_BACK:
                if self._tone == None:
                    return None
                else:
                    self._state = STATE_MENU
                    self._button_start.grid()
                    self.Heading1.grid_remove()
                    self.l11.grid()
                    self.Heading1.grid_remove()
                    self._button_next.grid_remove()
                    self._button_back.grid_remove()
                    self._button_back.grid_remove()
                    self._button_cool.grid_remove()
                    self._button_neutral.grid_remove()
                    self._button_warm.grid_remove()
                    self.l12.grid_remove()
                    self.l13.grid_remove()
                    self.l14.grid_remove()

        elif self._state == STATE_FACE:
            if action == ACTION_BUTTON_NEXT:
                self._state = STATE_FACE_BOX

            elif action == ACTION_BUTTON_BACK:           
                self._state = STATE_SKIN_TONE
                # self.canvas.grid_remove()
                
        elif self._state == STATE_FACE_BOX:
            if action == ACTION_BUTTON_NEXT:
                self._state = STATE_FACE_BOX_RESULTS
                self.l12.grid()
                self.l12.grid(row = 0, column = 1)

            elif action == ACTION_BUTTON_BACK:
                self._state = STATE_FACE
                self.l12.grid_remove()
                self.l13.grid_remove()

        elif self._state == STATE_FACE_BOX_RESULTS:
            # create label
            if action == ACTION_BUTTON_NEXT:
                self._state = STATE_EYES

            elif action == ACTION_BUTTON_BACK:
                self._state = STATE_FACE_BOX
                self.l12.grid_remove()
                self.l13.grid_remove()

            elif action == ACTION_UPDATE_TEXT:
                self.l12['text'] = f'Your closest match is: {self.vid.face_results}'

        elif self._state == STATE_EYES:
            if action == ACTION_BUTTON_NEXT:
                self._state = STATE_EYES_RESULTS
                self.color_slider.grid()
                self.l12.grid(row = 0, column = 0)
                self.l13.grid(row = 0, column = 1)

            elif action == ACTION_BUTTON_BACK:
                self._state = STATE_FACE_BOX_RESULTS

        elif self._state == STATE_EYES_RESULTS:  
            if action == ACTION_BUTTON_NEXT:
                self._state = STATE_BLUSH
                self.l13.grid_remove()

            elif action == ACTION_BUTTON_BACK:
                self._state = STATE_EYES

            elif action == ACTION_UPDATE_TEXT:
                self.l12.grid_remove()
                self.l13['text'] = f'Your closest makeup color match is: {self.vid.recommended_color}'

        elif self._state == STATE_BLUSH:
            if action == ACTION_BUTTON_NEXT:
                self._state = STATE_BLUSH_RESULTS
                self.color_slider.grid()
                self.l13.grid()

            elif action == ACTION_BUTTON_BACK:
                self._state = STATE_EYES_RESULTS
                self.color_slider.grid_remove()

        elif self._state == STATE_BLUSH_RESULTS:
            if action == ACTION_BUTTON_NEXT:
                self._state = STATE_HIGHLIGHTER
                self.color_slider.grid_remove()
                self.l13.grid_remove()

            elif action == ACTION_BUTTON_BACK:
                self._state = STATE_BLUSH
                self.color_slider.grid_remove()

            elif action == ACTION_UPDATE_TEXT:
                self.l13['text'] = f'Your closest makeup color match is: {self.vid.recommended_color}'

        elif self._state == STATE_HIGHLIGHTER:
            if action == ACTION_BUTTON_NEXT:
                self._state = STATE_HIGHLIGHTER_RESULTS
                self.color_slider.grid()
                self.l13.grid()

            elif action == ACTION_BUTTON_BACK:
                self._state = STATE_BLUSH_RESULTS
        
        elif self._state == STATE_HIGHLIGHTER_RESULTS:
            if action == ACTION_BUTTON_NEXT:
                self._state = STATE_CONTOUR
                self.l13.grid_remove()

            elif action == ACTION_BUTTON_BACK:
                self._state = STATE_HIGHLIGHTER

            elif action == ACTION_UPDATE_TEXT:
                self.l13['text'] = f'Your closest makeup color match is: {self.vid.recommended_color}'

        elif self._state == STATE_CONTOUR:
            if action == ACTION_BUTTON_NEXT:
                self._state = STATE_CONTOUR_RESULTS
                self.color_slider.grid()
                self.l13.grid()

            elif action == ACTION_BUTTON_BACK:
                self._state = STATE_HIGHLIGHTER_RESULTS
        
        elif self._state == STATE_CONTOUR_RESULTS:
            if action == ACTION_BUTTON_NEXT:
                self._state = STATE_LIP
                self.l13.grid_remove()

            elif action == ACTION_BUTTON_BACK:
                self._state = STATE_CONTOUR

            elif action == ACTION_UPDATE_TEXT:
                self.l13['text'] = f'Your closest makeup color match is: {self.vid.recommended_color}'

        elif self._state == STATE_LIP:
            if action == ACTION_BUTTON_NEXT:
                self._state = STATE_LIP_RESULTS
                self.color_slider.grid()
                self.l13.grid()

            elif action == ACTION_BUTTON_BACK:
                self._state = STATE_CONTOUR_RESULTS

        elif self._state == STATE_LIP_RESULTS:
            if action == ACTION_BUTTON_NEXT:
                self._state == STATE_RESULTS
                self.canvas.grid_remove()
                self.l15.grid()
                self.l13.grid_remove()
                self.color_slider.grid_remove()
                self.l16.grid(row = 0, column = 0)
                self.l16.grid()

                print(self.vid.recommended_color_list)

            elif action == ACTION_BUTTON_BACK:
                self._state = STATE_LIP
                self.l16.grid_remove()
            
            elif action == ACTION_UPDATE_TEXT:
                self.l13['text'] = f'Your closest makeup color match is: {self.vid.recommended_color}'

        elif self._state == STATE_RESULTS:
            if action == ACTION_BUTTON_NEXT:
                self._state = STATE_MENU
                
                self.l13.grid_remove()
                self.l14.grid()
                self.l15.grid_remove()
                self.l16.grid_remove()
                self._button_start.grid()


                # self.l15.grid()

            elif action == ACTION_BUTTON_BACK:
                self._state = STATE_LIP_RESULTS

            elif action == ACTION_UPDATE_TEXT:
                self.l16['text'] = f'Your overall makeup colors are: {self.vid.recommended_color_list}'
        
        # Default case 
        # Likely something that's wrong
        else:
            self._state = self.vid.get_frame(self._state,self._tone,App)

        print('Action: {} New State:{}'.format(action, self._state))
    
    # button time created so the user can't spam the button
    def button_func(self): 
        '''
        Invoked when the start/next button is clicked
        '''
        currTime = time()
        # self.BUTTON_TIME_REQUIRED = 500
        # check if enough time has passed to press the button
        if (currTime - self._button_last_clicked > BUTTON_TIME_REQUIRED):
            self.update_fsm(ACTION_BUTTON_NEXT)
            # update the last time we clicked
            self._button_last_clicked = currTime

    def button_func_back(self):
        '''
        Invoked when the start/next button is clicked
        '''  
        currTime = time()
        if (currTime - self._button_last_clicked > BUTTON_TIME_REQUIRED):
            self._button_last_clicked = currTime
            self.update_fsm(ACTION_BUTTON_BACK)

    def button_func_tone(self,tone):
        self._tone = tone
        print('tone',self._tone)

    def update_slider_value(self, value):
        self.vid.update_slider(value)

    def recommended_color(self,color):
        self.recommended_color = color
        print('color',self.recommended_color)

    # actually does graphics
    def update(self):
        '''
        Called every self.delay milliseconds
        '''
        # try:
        if self._state not in [STATE_MENU, STATE_SKIN_TONE, STATE_RESULTS]:

            ret, frame = self.vid.get_frame(self._state,self._tone,App)

            # Update label text if anything exists
            self.update_fsm(ACTION_UPDATE_TEXT)

            if ret:
                self.photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
                self.canvas.create_image(0, 0, image = self.photo, anchor = NW)

        self.window.after(self.delay, self.update)

class VideoCapture:
    def __init__(self, window, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        print(dir(self.vid))
        self.face_results = None
        self.recommended_color = None
        self.recommended_color_list = { 
            FEATURE_CHEEKS: None,
            FEATURE_EYES: None,
            FEATURE_UPPER_CHEEKS: None,
            FEATURE_CHEEK_BONES: None,
            FEATURE_LIPS: None
        } 
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
        self.cascade = cv2.CascadeClassifier(cv2.samples.findFile(cascade_fn))
        self.nested = cv2.CascadeClassifier(cv2.samples.findFile(nested_fn))

        # Default opacity
        self.opacity = 0.5

    def update_slider(self, value):
        print(f'New slider value: {value}')
        self.opacity = float(value)/100

    def get_frame(self,state,tone,App):
        if self.vid.isOpened():
            # makes the program handle errors
            try:
                ret, img = self.vid.read() #abbreviation for return
            except:
                print("camera cannot be run")
            # if return is not 0
            # If the camera has successfully picked up an image
            if ret:
                # Process image from webcam
                # Process image
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                gray = cv2.equalizeHist(gray)

                # Perform face detection
                
                rects = detect(gray, self.cascade)

                # Copy image so we can draw on it
                # img = original git
                vis = img.copy()

                # Facial Feature detection
                # color formatting is (blue ,green, red)
                    
                if state == STATE_FACE_BOX:
                    draw_rects(vis, rects, (0, 255, 0))

                elif state == STATE_FACE_BOX_RESULTS:
                    if len(rects) > 0:
                        # Only find skintone once
                        if self.face_results == None:
                            self.face_results = find_skintone(vis, rects)
                            print(f'Detected skintone as {self.face_results}')
                
                elif state == STATE_EYES:
                    eye_rects = get_eye(rects)
                    print('eye_rects', eye_rects)
                    draw_hexagon(vis,eye_rects,(255,0,0))

                elif state == STATE_EYES_RESULTS:
                    eye_rects = get_eye(rects)
                    fillcolor = COLOR_PALETTE[self.face_results][FEATURE_EYES][tone][0]
                    fill_hexagon(vis,eye_rects,fillcolor, thickness = -1)
                    self.recommended_color = COLOR_PALETTE[self.face_results][FEATURE_EYES][tone][1]
                    self.recommended_color_list[FEATURE_EYES] = self.recommended_color
                    print(self.recommended_color)
                
                elif state == STATE_BLUSH:  
                    cheek_rects = find_cheeks(rects)   
                    draw_rects(vis,cheek_rects,(0, 0, 255))

                elif state == STATE_BLUSH_RESULTS:
                    #citation: https://docs.opencv.org/2.4/modules/core/doc/drawing_functions.html
                    print(self.face_results, FEATURE_CHEEKS, tone)
                    cheek_rects = find_cheeks(rects)
                    fillcolor = COLOR_PALETTE[self.face_results][FEATURE_CHEEKS][tone][0]
                    draw_rects(vis,cheek_rects,fillcolor,thickness = -1)
                    draw_rects(vis,cheek_rects,(0, 0, 255))
                    self.recommended_color = COLOR_PALETTE[self.face_results][FEATURE_CHEEKS][tone][1]
                    self.recommended_color_list[FEATURE_CHEEKS] = self.recommended_color            
    
                elif state == STATE_HIGHLIGHTER:
                    upper_cheeks = find_upper_cheeks(rects)
                    draw_triangle(vis,upper_cheeks,(255,255,0),thickness = 1)

                elif state == STATE_HIGHLIGHTER_RESULTS:
                    upper_cheeks = find_upper_cheeks(rects)
                    fillcolor = COLOR_PALETTE[self.face_results][FEATURE_UPPER_CHEEKS][tone][0]
                    fill_triangle(vis,upper_cheeks,fillcolor,thickness = -1)
                    self.recommended_color = COLOR_PALETTE[self.face_results][FEATURE_UPPER_CHEEKS][tone][1]
                    self.recommended_color_list[FEATURE_UPPER_CHEEKS] = self.recommended_color
                    # fill in the shape

                elif state == STATE_CONTOUR:
                    cheek_bones = find_cheek_bones(rects)
                    draw_triangle(vis,cheek_bones,(0,255,255),thickness = 1)

                elif state == STATE_CONTOUR_RESULTS:
                    cheek_bones = find_cheek_bones(rects)
                    fillcolor = COLOR_PALETTE[self.face_results][FEATURE_CHEEK_BONES][tone][0]
                    fill_triangle(vis,cheek_bones,fillcolor,thickness = -1)
                    self.recommended_color = COLOR_PALETTE[self.face_results][FEATURE_CHEEK_BONES][tone][1]
                    self.recommended_color_list[FEATURE_CHEEK_BONES] = self.recommended_color
                    
                elif state == STATE_LIP:
                    lip_ellipses = find_lips(rects)
                    draw_ellipses(vis, lip_ellipses,(255,0,255),thickness = 1)

                elif state == STATE_LIP_RESULTS:
                    lip_ellipses = find_lips(rects)
                    fillcolor = COLOR_PALETTE[self.face_results][FEATURE_LIPS][tone][0]
                    draw_ellipses(vis, lip_ellipses, fillcolor,thickness = -1)
                    self.recommended_color = COLOR_PALETTE[self.face_results][FEATURE_LIPS][tone][1]
                    self.recommended_color_list[FEATURE_LIPS] = self.recommended_color
                    print(self.recommended_color)

                # add weighted function
                
                # Return a boolean success flag and the current frame converted to BGR
                cv2.addWeighted(vis, self.opacity, img, 1 - self.opacity, 0, img)
                # Flip image so that the feed is mirrored to the user
                img= cv2.flip(img, 1)

                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
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
    App(Tk(), "Application of Beauty")