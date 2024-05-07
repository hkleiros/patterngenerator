from random import randint
from pathlib import Path
import numpy as np


def pick(options: list, height: int, width: int) -> list[list]:
    """
    Generate a grid pattern based on the contents of options
    Paramteters:
        - options [list] : the options for the pattern
        - width   [int] : number of choices per row
        - height  [int] : number of rows

    Return :
        list[list[any]]: the generated pattern
    """

    return [
        [options[randint(0, len(options) - 1)] for _ in range(width)]
        for _ in range(height)
    ]


def prettyprint(matrix: list[list]) -> None:
    """
    Print out a matrix like a generated pattern line for line with spaces between characters
    Parameters:
        matrix [list[list[any]]] : the matrix to print

    Return :
        None
    """

    for i in matrix:
        for j in i:
            for k in j:
                print(k, end=" ")
            print()


def save(parent: Path, pattern: list[list]) -> None:
    """
    Function to save the generated pattern to a text file.
    Parameters:
        pattern [list[list[any]]] : the pattern to save

    Return :
        None
    """

    if input("Save pattern? ") == "":
        return
    with open(parent.joinpath(input("Name the file ") + ".txt"), "w") as f:
        for i in pattern:
            for j in i:
                for k in j:
                    f.write(f"{k} ")
                f.write("\n")


def ten_print(height: int = 10, width: int = 10) -> None:
    """
    Generate the 10_print pattern with dot (based on https://archive.bridgesmathart.org/2022/bridges2022-281.pdf)
    Parameters:
        - height [int] : the number of rows in the generated picture
        - width [int] : the number of choices in each row

    Returns:
        None
    """
    path = work_dir.joinpath("10_print")

    left = [l.split() for l in list(open(work_dir / "leftleaning.txt"))]
    right = [r.split() for r in list(open(work_dir / "rightleaning.txt"))]
    chosen = pick([left, right], height, width)
    res = []
    for c in chosen:
        res.append(np.concatenate(c, axis=1))
    prettyprint(res)
    save(path, res)


if __name__ == "__main__":
    work_dir = Path(__file__).parent.absolute()
    ten_print(height=10, width=15)
