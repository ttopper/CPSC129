# Algorithm Overview and Pseudocode

Look over the Wikipedia page’s section on algorithms for simulating 
Conway's Game of Live. This will give you an idea about the basic 
algorithm. As well as some variations that we will implement in the 
assignment (like the toroidal universe). Running the game of life is 
computationally expensize with the simple algorithm we are going to 
implement this week. Later on in the course we will have the 
opportunity to make our implementation more visually snazzy and 
computaionally efficient.

The basic steps for creating the Game of Life are the following:

    Create the universe
    Initialize the universe
    Forever:
        Display the universe 
        Age the universe

This algorithm is a very general description of what we need to do. 
Before I start translating this to python I want to provide a bit more 
detail about how I will age the universe.

    Create the universe
    Initialize the universe

    Forever:
        Display the universe
            
        Age the universe:
        Consider every cell in the universe
        Counts its live neighbours
        Based on its current state and its number of live neighbours
            Decide if it lives, dies, or is born
            Record the result in next universe
                
        Replace universe with next universe

Now we are ready to start implemeting the code in python.