# makeup

This program will detect your facial features and formulate what pigments best
suit your skin tone and eye color. You can also choose from different lip colors, 
eye shadow and blush.

## TODOs

- Everytime you click the next button, it detects a different feature of your 
face and generates/recommends a color

- Has to switch between openCV and tkinter somehow...

- Use tkinter to make an intro page/ other pages displaying the facial features
- highlighter and contour make it in triangles

- find average color within the center (4 points) of the rectangle and ellipse

## Finite State Machine

- First part where theres no open cv and then just your face

- Then each time using the geometry to detect the part of your face as 1 step 
each and then detecting the color/outputting the result as the step after each 
one

- Specifically STATE_SKIN_TONE doesn't use the webcam but it asks the user 
whether they're cool, warm or neutral tones based on a series of questions

## Color Palette

- extract average skin tone color within a shape and generate what color suits 
best for that certain facial feature

- cheeks, lips, eyes

- highlighter: upper cheek, contour: cheek color, a little bit darker

- should make a gradient/transparency color scale for each facial feature for 
better user experience and style

## Bugs to fix 

- when you click the back button on the screen to go back to START_MENU, it 
freezes, fix it somehow. FIXED

- also remove the logo when it goes to the face menu and so on. FIXED
