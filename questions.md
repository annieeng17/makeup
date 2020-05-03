# Questions for `makeup`

1. Do you know what the following code is doing?

  ```python
  def detect(img, cascade):
      rects = cascade.detectMultiScale(
          img, 
          scaleFactor=1.3, 
          minNeighbors=4, 
          minSize=(30, 30), 
          flags=cv2.CASCADE_SCALE_IMAGE
      )
  ```
the function is used to find the facial and eye features, img stands for the 
the image where objects are detected, scaleFactors stands for the parameter
that specifies how much the image size is reduced at each image scale,
minNeighbors stands for how many neighbors each rectangle should have. The less, 
the better quality. Flags mean the parameter containing the Old Cascade 
  
2. How did you layout items in your UI?
I layed out the items in my UI by hand drawing the first two and last pages
of the states. I placed named the UI components in the init with self.etc, and 
placed them in the FSM. As each state changed, I would either have to 
place(grid) or remove depending on which state the component needed to be at.

3. How do buttons respond to clicks?
The button responds to clicks by changing each state one at a time. For the 
undertone buttons, it is stored in self._tone and if one of them is clicked, its
"stored". If an undertone button was not clicked, then the screen won't respond 
at all to clicks from the next and back button until an undertone button is 
clicked.

4. Why did you use an FSM in your project?
I used a FSM because that would be most efficient for the components of every
facial detection and their corresponding makeup features. Since each screen
is constantly changing depending on the code, I can change the implementation 
each time the screen changes and its easy to manage. Basically each state can
decide what the next states' feautures can "stay" for the next. Each state
behaves differently compared to the one before.

5. How does your color recommender work?
My color recommender works by calling onto a color palette dictionary I created 
in the makeupLib.py file that calls a specific makeup feature and undertone,
depending on the facial tone they get when detected on STATE_SKIN_TONE. This 
function is called during the get_frame function. The colors were chosen from my
research into undertones, and colors that best suit for specific facial tones. 
The names were chosen from colors of makeup products that closely resembled the 
colors I chosen from the Sephora website. How did I chose the colors? Some I 
went on the Sephora website, screenshotted and page and uploaded onto an RGB 
color detector, chose them carefully and implemented into the dictionary.

6. Can you explain how you does opacity overlays for makeup?

   ```python
   cv2.addWeighted(vis, self.opacity, img, 1 - self.opacity, 0, img)
   ```
  the opacity overlays for makeup by blending images together and consttructing
  the transparent overlay. self.opacity is the default transparency set to a 
  specific value. I set it to 0.5 


7. Can you explain how you drew rectangles / triangles, and how you filled them in?
I drew the rectangles and triangles by researching the openCV function online
and learning that they take in empty lists of rects. I filled them in by 
implementing a fill color,calling onto the dictionary for the corresponding
fill color and called the rectangle/triangle function, replacing the default 
color(none) and replacing it with the fill color.

8. How does your face recognition algorithm work? (I expect them to ask you this
 even though you didn't code it. Read up on <https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html>)
My facial recognition algorithm works by needing a lot of positive images 
(images of faces) and negative images (images without faces) to train the 
classifier. Then it extracts the features from them. OpenCV already contains 
many pre-trained classifiers for face, eyes, smile etc. and such examples can be 
the two files I included in the zip that is needed in order for my face and eye
functions to work properly. ('haarcascade_frontalface_default.xml') and
('haarcascade_eye.xml') Theres the concept of Cascade of Classifiers where there
are actually many groups of features to detect the specified facial feature, but
they generate the best ones out of all of them. Sort of like showcasing the best
of the best. 

9. How does your feature recognition algorithm work? (e.g. detecting eyes, 
cheeks, lips, etc)
My feature recognition algorithm works by taking in rectangles of the face where
my code takes in extremely specific coordinates of the width and length of the 
face and creating shapes made for the feature. To do this, I had to draw and 
think of how and where the points need to be placed on the face to make the 
shape. If I had to make two shapes for a facial feature, I would have to 
"reflect" the coordinates I made for one side by subtracting the distance 
between a point and the middle of the face rectangle and creating a new
variable for the reflected point. Then the algorithm returns all the points in a 
rect.

10. Why did you have to convert your image to grayscale before doing anything?

   ```python
   gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   gray = cv2.equalizeHist(gray)
   ```
I converted my image to grayscale before doing anything because many functions
later require grayscale such as faceCascade.detectMultiScale() and 
CascadeClassifier::detectMultiScale(const Mat& image,...), if I didn't, my
later functions won't be able to properly work. My program will also be able to
have better performance once I convert to grayscale.

11. How did you keep track of things like the slide the program is on, what 
colors you recommend for what features, and the skin tone the user selected?

I kept track of things like the slide the program is one by creating SELF_STATE
in the init, and each state increments by 1 everytime the next button is clicked.
So, it is simple to keep track of and I made print statements in case I got lost.
I kept track of colors I recommended by creating an empty dictionary that I set
each facial feature to None first and after that, where each feature was called
it would update the feature. I kept track of the skin tone the user selected by 
making the tone self._tone and it is remembered later on in the program with 
self.face_results.