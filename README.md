# aicg-week1-boids
Simulates the flocking behaviour of birds following Craig Reynolds' rules

<p align="center">
  <img src="https://github.com/ArthurSZANTYR/aicg-week1-boids/blob/main/examples/vast-bird-shaped-murmuration-flock-of-starlings.png" alt="Bird Flock" width="300">
</p>


## Goals
I realized this project as a part of the AICG course week1 from the IFT program. I had to render a "*Boids*" simulation following Craig Reynolds' rules.

> Boids is an artificial life program, developed by Craig Reynolds in 1986, which simulates the flocking behaviour of birds. His paper on this topic was published in 1987.

The instructions were to use python and numpy in an efficient way.

--------

## Installation and Usage
To test this simulation follow these steps :


__Installation__
1. Make sure you have the following dependencies installed : 
   ```shell
   pip install -r requirements.txt 

2. Launch the file "main.py"
    ```shell
     python main.py

__Usage__

* You can modify parameters such as the number of boids and their maximum speed when creating the Flock instance in the main.py files

__Simulation test__

<p align="center">
  <img src="https://github.com/ArthurSZANTYR/aicg-week1-boids/blob/main/examples/boids_simulation_50.gif" alt="Boids Simulation" width="400">
</p>


## Project Structure

The project is organized as follows:

- `fenetre.py` file containing the size of the pygame window
- `flock.py` file containing the Flock class, you can go there to modify even more parameters such as maximum steering force - to modify the boids behavior
- `render.py` file containing the pygame window parameters for the rendering
