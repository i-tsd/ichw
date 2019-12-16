"""tile.py: Gives all solutions of a tile-paving problem.
__author__ = "Li Siyuan"
__pkuid__  = "1900011791"
__email__  = "tsd@pku.edu.cn"
"""


import turtle


def intl():
    """In this program, the floor is consisted with 1 x 1 cells.
    Every cell is represented by an item in a dictionary.
    The key of the dictionary is a tuple (the position of the
    cell), while the value is a boolean. Value True represents
    the cell is occupied by a tile, while False represents the
    cell is vacent.
    This function intializes the floor (dictionary) with its
    horizontal length ('bhl') and vertical length ('bvl') given
    by global variables, and give value False to all of the cells
    (items).
    """
    for i in range(bhl):
        for j in range(bvl):
            base[i, j] = False


def search(dict0):
    """Return: A tuple (x, y) or boolean value False.
    This functions finds the first unfilled cell (from the left-
    bottom) of the floor, and returns its position.
    If this cell can't be found(which means the floor has been
    adequately filled by tiles), the function will return with
    value False.
    The input shall be a dictionary which describes a floor in
    the format described above.
    """
    for i in range(bvl):
        for j in range(bhl):
            if not dict0[j, i]:
                return(j, i)
    return(False)


def hfil(base0):
    """Return: a new dictionary describing a modified floor.
    This function receives a floor, finds the first unfilled cell
    with the function "search", and fills a tile HORIZONTALLY with
    the cell at the its left-bottom). THe function will return with
    a NEW dictionary describing the modified floor.
    The function will raise an exception if the tile can't be filled
    at the position.
    The input shall be a dictionary which describes a floor in
    the format described above.
    """
    baset = base0.copy()
    x, y = search(baset)
    for i in range(hl):
        for j in range(vl):
            if not baset[i + x, j + y]:
                baset[i + x, j + y] = True
            else:
                raise(AssertionError)
    return(baset)


def vfil(base0):
    """The function works in the same way as the function "hfil", but
    fills the tile VERTICALLY.
    """
    baset = base0.copy()
    x, y = search(baset)
    for i in range(hl):
        for j in range(vl):
            if not baset[j + x, i + y]:
                baset[j + x, i + y] = True
            else:
                raise(AssertionError)
    return(baset)


def visualize(x):
    # Visualize the given result with the Python module Turtle.
    for x0 in range(bhl):
        for y0 in range(bvl):
            drawchart(x0, y0)
    for tiles in x:
        drawtile(tiles)


def drawchart(x, y):
    # A part of the visualization function, which draws the background.
    d = 36
    tsd = turtle.Turtle()
    tsd.speed(0)
    tsd.pencolor('blue')
    tsd.hideturtle()
    tsd.penup()
    tsd.goto(x * d, y * d)
    tsd.pendown()
    tsd.goto((x + 1) * d, y * d)
    tsd.goto((x + 1) * d, (y + 1) * d)
    tsd.goto(x * d, (y + 1) * d)
    tsd.goto(x * d, y * d)
    tsd.penup()
    tsd.goto((x + 0.5) * d, (y + 0.5) * d)
    tsd.write((x, y), move=False, align="center", font=("Arial", 7, "normal"))


def drawtile(a):
    # A part of the visualization function, which draws the tiles.
    x, y = a[0]
    d = 36
    dirt = a[1]
    tsd = turtle.Turtle()
    tsd.speed(0)
    tsd.pensize(3)
    tsd.hideturtle()
    tsd.penup()
    tsd.goto(x * d, y * d)
    tsd.pendown()
    if dirt:
        tsd.goto((x + hl) * d, y * d)
        tsd.goto((x + hl) * d, (y + vl) * d)
        tsd.goto((x) * d, (y + vl) * d)
        tsd.goto(x * d, y * d)
    else:
        tsd.goto((x + vl)*d, y * d)
        tsd.goto((x + vl)*d, (y + hl) * d)
        tsd.goto((x) * d, (y + hl) * d)
        tsd.goto(x * d, y * d)
    tsd.penup()


def recurse(solvex):
    if not search(solvex[0]):  # Append a result to the list
        solves.append(solvex[1].copy())
    else:
        try:  # Try to fill a tile horizontally
            basedh = hfil(solvex[0].copy())
        except:  # The branch will be stopped if the tile can't be filled
            pass
        else:  # Pass the modified floor and the record on
            solvedh = [basedh, solvex[1]]
            solvedh[1].append([search(solvex[0]), True])
            recurse(solvedh)  # Continue

        if hl != vl:  # Exclude the circumstances in which the tile is a square
            try:  # Try to fill a tile vertically
                basedv = vfil(solvex[0].copy())
            except:
                pass
            else:
                solvedv = [basedv, solvex[1]]
                solvedv[1].append([search(solvex[0]), False])
                recurse(solvedv)
    if solvex[1] != []:  # Remove the most recent record when it finishes
        solvex[1].remove(solvex[1][-1])


def formatres(solvesx):
    """The result is not represented in the form given by the example, but in
    a form described by the following pattern: Every tile is represented by
    a tuple, in which the first item is the position of its left-bottom cell,
    the second value is a boolean(True=horizontal;False = vertical).
    This function converts the result into the pattern of the example."""
    formlist = []
    for sols in solvesx:
        outp = []
        for tiles in sols:
            midp = []
            x0, y0 = tiles[0]
            if tiles[1]:
                for i in range(hl):
                    for j in range(vl):
                        midp.append((x0 + i, y0 + j))
            else:
                for i in range(vl):
                    for j in range(hl):
                        midp.append((x0 + i, y0 + j))
            outp.append(midp.copy())
        formlist.append(outp.copy())
    return(formlist)


def main():
    recurse(solve)
    if solves == []:
        print('No solution, please try other values')
        input()
    else:
        print("Found %i solution(s)." % len(solves))
        print(
            'I recommend not to print the solutions if the number is large,' +
            'For printing all of them can be really slow.'
        )
        print('You can still view the visualization of any of the solutions.')
        doprint = input('Input Y to print the solutions...')
        if doprint == "Y":
            answer = formatres(solves)
            for ans in answer:
                print(ans)
        else:
            pass
        maxi = (len(solves)) - 1
        tm = int(
            turtle.numinput(
                "salty fish", "Input number of 0 - %i:" % maxi,
                0, minval=0, maxval=maxi
            )
        )
        visualize(solves[tm])
        input()


vl = int(input('Length of the tile (a)...'))  # a in the example
hl = int(input('Width of the tile (b)...'))  # b in the example
bvl = int(input('Length of the floor (m)...'))  # m in the example
bhl = int(input('Width of the floor (n)...'))  # n in the example
base = dict()  # Create the floor
intl()  # Initialize the floor
solves = []  # The result-containing list
reco = []  # The initial value of the record, which is empty
solve = [base, reco]  # The initial value passed to the recurse function
if __name__ == '__main__':
    main()
