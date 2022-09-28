#!/usr/bin/env python3
# Created by: Katie
# Created on: September 27th, 2022
# This program calculates the circumference of a
# circle with user input, using the formula
# involving tau.
import constants


def main():
    # get the radius from the user
    radius = float(input("Please input the radius of your circle in cm: "))

    # calculate the circumference using the Tau formula
    circumference = constants.TAU * radius

    # display the results of the circumference calculation
    # back to the user.
    print("")
    print(
        "The circumference of the circle (calculated using Tau!), with the radius you inputted is: {} cm".format(
            circumference
        )
    )


if __name__ == "__main__":
    main()
