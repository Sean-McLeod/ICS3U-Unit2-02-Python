#!/usr/bin/env python3

# Created by Sean McLeod
# Created on November 2020
# This program can calculate the area and perimeter of a rectangle with
# dimensions entered by users


def main():
    # This function calculates the area and the perimeter of a rectangle

    # input
    length = int(input("Enter the length of the rectangle (mm):"))
    width = int(input("Enter the width of the rectangle (mm):"))

    # process
    area = length*width
    perimeter = 2*(length+width)

    # output
    print("")
    print("Area is {}mm²".format(area))
    print("Perimeter is {}mm".format(perimeter))


if __name__ == "__main__":
    main()
