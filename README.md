# makeup

- This program called Application of Beauty will detect your facial features and 
formulate what pigments best suit your skin tone and eye color. You can also 
choose from different blush, contour, eye shadow, highlighter and lipstick.

## TODOs

- Everytime you click the next button, it detects a different feature of your 
face and generates/recommends a color. Theres a timer of 1 second on each next 
and back button clicked, so the program won't crash if the user tries to spam a
button. 

- Has to switch between openCV and tkinter somehow... Done

- Use tkinter to make an intro page/ other pages displaying the facial features. Done
- highlighter and contour make it in triangles. Done

- find average color within the center (4 points) of the rectangle and ellipse

## Finite State Machine

- First part where theres no open cv and then just your face

- Then each time using the geometry to detect the part of your face as 1 step 
each and then detecting the color/outputting the result as the step after each 
one

- Specifically STATE_SKIN_TONE doesn't use the webcam but it asks the user 
whether they're cool, warm or neutral tones based on a series of questions

## Color Palette
- All RGB colors hard coded in, most color and color name references are based 
from the Sephora website

- extract average skin tone color within a shape and generate what color suits 
best for that certain facial feature

- cheeks, lips, eyes

- highlighter: upper cheek, contour: cheek color, a little bit darker

- should make a gradient/transparency color scale for each facial feature for 
better user experience and style. Extra after MVP

## Bugs to fix 

- when you click the back button on the screen to go back to START_MENU, it 
freezes, fix it somehow. FIXED

- also remove the logo when it goes to the face menu and so on. FIXED

- need to create a slider because that is very important for complexity and 
points

- need to also fix the fill eyeshadow function, for some reason it doesn't work
even though I tried to follow the way I did it for fill_in_triangle
