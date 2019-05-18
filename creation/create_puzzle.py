
import json
from os import path


def get_squares():
    digits = '123456789'
    rows   = 'ABCDEFGHI'
    cols   = digits 
    squares = [a+b for a in rows for b in cols]
    return squares


def create_dict_puzzle(grid):
    chars = [c for c in grid if c in '123456789' or c == '0']
    squares = get_squares()
    return dict(zip(squares, chars))


def display(sudoku):
    squares = get_squares()
    width = 1 + max(len(sudoku[s]) for s in squares)
    line = '+'.join(['-'*(width*3)]*3)
    for r in 'ABCDEFGHI':
        print(''.join(sudoku[r+c].center(width)+('|' if c in '36' else '') for c in '123456789'))
        if r in 'CF': 
            print(line)
    print('\n')


def read_puzzle(filename):
    with open(path.join(path.dirname(__file__), filename),"r") as fd: 
        array = fd.readline()    
        puzzle = []
        for row in array:
            for col in row:
                puzzle.append(str(col))
        fd.close()
    return puzzle

def create_puzzle(filename):
    puzzle_values = read_puzzle(filename) 
    puzzle_dict = create_dict_puzzle(puzzle_values)    
    display(puzzle_dict)

if __name__ == "__main__":
    create_puzzle("puzzleB.txt")
