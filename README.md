# random_coordinates
Author : Yasin ETLİ
Date created: 24/03/2022
This script generates the desired number of random coordinates from within the rectangular area created by the determined 4 coordinates.
Coordinates to be entered as input must be entered in degree-minute-second-split second format, which is frequently
used. If any of these is a single digit number, it must be entered with a leading zero. For example 
the coordinate 38°00'01.13" must be entered as 38000113. Otherwise, the script will give an incorrect output.
When the largest and smallest meridians and the largest and smallest parallels of the region where random coordinates
will be generated are entered, the smallest parallelogram surrounding the relevant area is found.
For example, when finding the largest and smallest coordinate values for a region in the northern and eastern hemispheres: 
the parallel of the southernmost point of the area is the smallest parallel, the parallel of the northernmost point is the largest parallel, 
the meridian of the westernmost point is the smallest meridian, and the meridian of the easternmost point is the smallest meridian.
Naturally, some selected points will be inside the created peripheral parallelogram, but outside the desired area (which is most likely an irregularly shaped area).
In this case, re-running the script and generating new coordinates was considered as a solution.
In order for all generated random coordinates to be in the desired area, a script that requires entering much more coordinates or spacial data and image processing 
will be required. In this respect, the script given here offers a relatively simple solution, even if it is incomplete.
