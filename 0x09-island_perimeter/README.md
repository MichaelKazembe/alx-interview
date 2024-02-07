# 0x09 Island Perimeter

This program calculates the perimeter of an island represented by a 2D grid using Python.

## Description

The program takes a 2D grid as input, where `1` represents land and `0` represents water. It calculates the perimeter of the island, which is the total length of the boundary between the land and water.

## Task
Island Perimeter
Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in grid:

* `grid` is a list of list of integers:
    * 0 represents water
    * 1 represents land
    * Each cell is square, with a side length of 1
    * Cells are connected horizontally/vertically (not diagonally).
    * `grid` is rectangular, with its width and height not exceeding 100
* The grid is completely surrounded by water
* There is only one island (or nothing).
* The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).


