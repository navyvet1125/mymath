""" This module contains functions for calculating the area of a rectangle and a circle. """
from math import pi

def area_of_rectangle(width = 1, height = 1):
    """
    This function returns the area of a rectangle given its width and height
    """
    return width *  height

def area_of_circle(radius = 1):
    """
    This function returns the area of a circle given its radius
    """
    return pi*radius**2
