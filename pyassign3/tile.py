"""tile.py: Gives all solutions of a tile-paving problem.
__author__ = "Li Siyuan"
__pkuid__  = "1900011791"
__email__  = "tsd@pku.edu.cn"
"""


import turtle


def intl():
    """This function intilizes the floor(represented by
    the dictionary "base"), which gives value False to all of
    the cells(means the cells are not filled by a tile).
    """
    for i in range(bhl):
        for j in range(bvl):
            base[i, j] = False


def search(dict0):
    for i in range(bvl):
        for j in range(bhl):
            if not dict0[j, i]:
                return(j, i)
    return(False)


def hfil(base0):
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
    for x0 in range(bhl):
        for y0 in range(bvl):
            drawchart(x0, y0)
    for tiles in x:
        drawtile(tiles)


def drawchart(x, y):
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
    if not search(solvex[0]):
        solves.append(solvex[1].copy())
    else:
        try:
            basedh = hfil(solvex[0].copy())
        except:
            pass
        else:
            solvedh = [basedh, solvex[1]]
            solvedh[1].append([search(solvex[0]), True])
            recurse(solvedh)

        if hl != vl:  # Exclude the circumstances in which the tile is a square
            try:
                basedv = vfil(solvex[0].copy())
            except:
                pass
            else:
                solvedv = [basedv, solvex[1]]
                solvedv[1].append([search(solvex[0]), False])
                recurse(solvedv)
    if solvex[1] != []:
        solvex[1].remove(solvex[1][-1])


def format(solvesx):
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
            answer = format(solves)
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


vl = int(input('Length of the tile...'))
hl = int(input('Width of the tile...'))
bvl = int(input('Length of the floor...'))
bhl = int(input('Width of the floor...'))
base = dict()
intl()
solves = []
reco = []
solve = [base, reco]
if __name__ == '__main__':
    main()
