# beefree

first the program takes an argumant from the command line and parsing it into numpy format.
than the program indicates all the ghosts' cords.
the route function creates a queue and a set.
  a queue to store all the cords pairs and a set to store all the cords that we were been to.
as long the queue is not empty and we haven't reached the packman for each cell we chack it's neighboars and if
  the cell is between the bounds and is not a wall and first time visiting
    mark the cords as visited and append the pair into the queue
when we find the packman return the path variable length
append each path length to a list and sort it using bubble sort in the end.
