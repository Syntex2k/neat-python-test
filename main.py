import os

import neat

from game import evaluate_genomes


def run(config_file):
    # Load in the config file for the neat architecture
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_file)

    # Create a population out of the provided config
    population = neat.Population(config)

    # Add so-called reporter. They enable to print out statistics in the console allowing for deeper analysis
    population.add_reporter(neat.StdOutReporter(True))
    population.add_reporter(neat.StatisticsReporter())

    # We let the population run. In order to do this, we need to provide a fitness-function which takes two
    # arguments:
    #   1. The population as a list of (genome_id, genome) tuples.
    #   2. The current configuration object.
    # In this function the whole logic of the game takes place. It does contain the game loop and assigns each bird
    # their fitness score.
    # We let the simulation run until there are 50 generations or a bird in a previous generation does so well that
    # it does not hit a pole anymore, so we can stop there.
    winner = population.run(evaluate_genomes, 50)

    # Print out the stats (genomes, with their weights and connections) of the best bird
    print('\nBest genome:\n{!s}'.format(winner))


if __name__ == '__main__':
    # Concatenate the paths so we do not get problems with different Operating Systems and working directories.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    # Starts the game by creating a neat population and running the simulation
    run(config_path)
