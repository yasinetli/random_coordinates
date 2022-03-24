# random.coordinates.py
# Author : Yasin ETLİ
# Date created: 24/03/2022
# This script generates the desired number of random coordinates from within the rectangular area created by the
# determined 4 coordinates.

import random


# Here, is a function to convert the entered coordinate data to split seconds.

def coordinate_transformer(coord):
    transformed_coordinate = int(str(coord)[0:2]) * 216000 + int(str(coord)[2:4]) * 3600 + \
                             int(str(coord)[4:6]) * 60 + int(str(coord)[6:])
    return transformed_coordinate


# Here, is a function that will convert random coordinates generated in split second format to classical
# degree-minute-second-split second format.

def reverse_transformer(dec):
    degree = int(dec / 216000)
    minute = int((dec - degree * 216000) / 3600)
    second = int((dec - (degree * 216000 + minute * 3600)) / 60)
    split = int((dec - (degree * 216000 + minute * 3600 + second * 60)) / 1)
    transformed_coordinate = f"{degree}° {minute}' {second}.{split}''"
    return transformed_coordinate

# Here, is the main function. Coordinates to be entered as input must be entered in degree-minute-second-split
# second format, which is frequently used. If any of these is a single digit number, it must be entered with
# a leading zero. For example the coordinate 38°00'01.13" must be entered as 38000113. Otherwise, the script
# will give an incorrect output.


def random_coordinates():
    coordinate_num = int(input("How many random coordinates do you need?"))
    smaller_meridian = int(input("Smaller Meridian Value:"))
    greater_meridian = int(input("Greater Meridian Value:"))
    smaller_parallel = int(input("Smaller Parallel Value:"))
    greater_parallel = int(input("Greater Parallel Value:"))
    smaller_meridian_transformed = coordinate_transformer(smaller_meridian)
    greater_meridian_transformed = coordinate_transformer(greater_meridian)
    smaller_parallel_transformed = coordinate_transformer(smaller_parallel)
    greater_parallel_transformed = coordinate_transformer(greater_parallel)
    coordinate_dict = {}
    for i in range(1, coordinate_num + 1):
        meridian_name = f"meridian {i}"
        parallel_name = f"parallel {i}"
        meridian_value = random.randint(smaller_meridian_transformed, greater_meridian_transformed)
        parallel_value = random.randint(smaller_parallel_transformed, greater_parallel_transformed)
        meridian_reverse = reverse_transformer(meridian_value)
        parallel_reverse = reverse_transformer(parallel_value)
        coordinate_dict[meridian_name] = meridian_reverse
        coordinate_dict[parallel_name] = parallel_reverse
    print(coordinate_dict)


random_coordinates()
