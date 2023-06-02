# Color-Detection
This is a python based program that detects color, specifically shades of green and blue, and red.
I did this by creating a live camra frame. Converted the frame 
from BRG(Blue, Red, Green) to HSV(Hue, Saturation, Value). I then created two values a maximum and a minimum value, 
that would act as a range of colors that can be detected by the program.
I then used that range of colors, and put it into a color mask frame
where only the resulting colors, within that range of values, would show. I originally created this for the First Inspires 2022-2023 
robotics competition Charged Up where it would detect the game pieces, cones and cubes, which were yellow and purple
respectively. This explains why I label my variables cones, and cubes, and why I used two color mask frames, one 
for each game piece. I've since change the colors to a red value scale, and green-blue value scale, 
instead of the yellow and purple of the game pieces, although I've still kept these two 
range of colors seperate, in there own color mask frames.  I also have it possible to draw rectangles where 
the frame detects color, but left it comented out.