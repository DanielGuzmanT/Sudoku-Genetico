from creation.res.sudoku.puzzle import create_puzzle, display
from creation.res.genetic.population import create_population, evaluate_population
from creation.res.genetic.fitness import fitness_sudoku
from creation.res.genetic.genetic_algorithm import genetic_sudoku
import click


def get_arguments(arguments):
    args = dict(tuple(param.split('=')) for param in arguments.split(','))
    
    assert set(args) == set(['w', 'Cx', 'm', 'maxGener']), "Arguments not valid, check --help"
    
    args['w'], args['m'], args['maxGener'] = int(args['w']), float(args['m']), int(args['maxGener'])
    return args


@click.command()
@click.option('-p','--puzzle', 'puzzle'   , required=True, prompt="Puzzle filepath", type=click.Path(exists=True), help="file path of sudoku puzzle data (i.e. creation/res/sudoku/puzzleA.txt)")
@click.option('-s','--solver', 'solver'   , required=True, prompt="Algorithm",       type=click.Choice(['sa', 'ga']), help="algorithms to use (args for ga: w ,Cx, m, maxGener)")
@click.option('-a','--args'  , 'arguments', required=True, prompt="Arguments",       type=str, help="algorithm chosen arguments separated by commas")
def run(puzzle, solver, arguments):
    print(puzzle, solver, arguments)
    args = get_arguments(arguments)
    genetic_sudoku(namefile=puzzle, numInd=args['w'], ngen=args['maxGener'], pmut=args['m'],crossover=args['Cx'], mutation='position', selection="tournament")
    # python main.py -p creation/res/sudoku/puzzleA.txt -s ga -a w=10,Cx=onepoint,m=0.1,maxGener=10000
    # python main.py -p creation/res/sudoku/puzzleA.txt -s ga -a w=10,Cx=uniform,m=0.1,maxGener=10000
    # python main.py -p creation/res/sudoku/puzzleA.txt -s ga -a w=10,Cx=newform,m=0.1,maxGener=10000


if __name__ == "__main__":
    run()
    

