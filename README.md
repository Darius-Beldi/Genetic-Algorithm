# Genetic Algorithm Optimizer

A Python implementation of a genetic algorithm that finds the maximum value of quadratic functions in the form `f(x) = ax² + bx + c`.

## Overview

This project uses genetic algorithms to find the maximum value of a quadratic function within a specified domain. It represents potential solutions as chromosomes with binary encoding, and evolves the population through selection, crossover, and mutation operations.

## Features

- Binary representation of floating-point numbers
- Fitness-proportional selection mechanism
- Single-point crossover
- Bit-flip mutation
- Elitism to preserve the best solution
- Customizable parameters including population size, domain range, and genetic operators
- GUI for easy parameter configuration and result visualization

## Running the Application

```
python gui.py
```

## Parameters

- **Population Size**: Number of chromosomes in the population
- **Domain Start/End**: Search space boundaries
- **A, B, C**: Coefficients of the quadratic function (ax² + bx + c)
- **Precision**: Decimal precision for floating-point values
- **Crossover Probability**: Chance of chromosomes participating in crossover (%)
- **Mutation Probability**: Chance of bit flips during mutation (%)
- **Generation Number**: Maximum number of evolution cycles

## Default Configuration

The default settings optimize the function `f(x) = -x² + x + 2` over the domain [-1, 2] with a population size of 20 for 50 generations.

## Project Structure

- `chromosome.py`: Definition of the Chromosome class
- `functions.py`: Core genetic algorithm operations
- `main.py`: Execution logic and optimization process
- `gui.py`: Tkinter-based user interface
