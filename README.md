# NameAnimation

I have been trying to learn how to make visually appealing
graphics over the past two weeks using matplotlib. I was 
wondering if I could make a sort of virtual businesscard in 
the form of a gif and thought it might be fun to try and make an 
animation of my name using matplotlib! 

------------------------------------------------------
Step 1: Get a sense for how the name would look

I was wondering how my name would look on a grid,
so I decided to open up Excel and black out each
cell that would be used to spell my name. Then, I entered
in their coordinates so I could find their x-y positions
in a plot. This excel file became extremely useful when
building the graphic!

-----------------------------------------------------
Step 2: Read this excel data

While I could have just copied the data and pasted it
directly into my python program, I figured it would
be good practice for me to just extract and clean the data
from the excel file. Because of this I used pandas to read
the data in and plot the points, one by one.

------------------------------------------------------
Step 3: Animate it all together!

This was by far the hardest part. While I could have just
stopped when the graphic was full of dots, I decided to 
draw each line to spell out my name more clearly. After each
dot is placed in the graph, dozens of lines are used to 
trace these dots in a specific pattern. The code gets messy,
but because this is more of a proof-of-concept project to
me 

-------------------------------------------------------
Step 4: Future directions

It is certainly not practical to animate each individual
letter every time I want to make a graphic. If I were
to continue to use this type of program, I would want 
to develop it in an object-oriented way. In this way,
I would take a string and convert it into an animated plot!
