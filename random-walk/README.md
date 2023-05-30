# Random Walk in 2D

## Description

A random walk in 2D is a mathematical concept that describes the movements of particles or objects as they move around in two dimensions. The movement is random and can be described using probability distributions. Random walks are used in many branches of science and engineering, such as modeling stock market trends or movement of molecules in liquids.

This program generates a random walk in 2D and displays it as a grid-like output.  The grid represents the path of the walk, and the starting and ending positions are displayed below the grid.

## How it Works

- The programs begins by importing the `random` module, which is used to generate to generate random numbers and consequently the direction of the random walk.

- The `main()` function is defined. It initializes the variables `N` (number of steps), `step_length`, `x`, and `y` (initial position).

- The `simulate_random_walk()` function takes the number of steps `N`, step length `d`, and initial positions `x` and `y`. It generates a random walk by iterating `N` times. At each step, a random number between 0 and 1 is generated using `random.random()`. Based on the value of the random number, the next position (`x` and `y`) is updated accordingly. The position `(x, y)` at each step is appended to the walk list.

- After generating the random walk, the `display_random_walk()` function is called. It takes the walk list and the starting positions `start_x` and s`tart_y`. In the `display_random_walk()` function, the boundaries of the grid are determined by finding the minimum and maximum `x` and `y` values in the walk list.

- A grid is created using nested list comprehension. The size of the grid is determined by the range of `min_x` to `max_x` and `min_y` to `max_y`. Each cell of the grid is initially set to `' '`.

- The walk path is then updated in the grid by substituting the corresponding cell with `'██'`. This represents the path of the random walk. The grid is printed row by row, with the cells joined by a space.

- Finally, the starting and ending positions are printed below the grid.


## Program Input & Output

When you run the program `random_walk.py`, the output will look like this;

```

Random Walk in 2-Dimensions.

                                                ██ ██    ██                                          
                                                ██ ██ ██ ██                                          
                                             ██ ██ ██ ██ ██ ██                ██ ██                  
                                       ██ ██ ██ ██ ██ ██ ██ ██ ██          ██ ██ ██                  
                                       ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██                  
                                       ██    ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██                  
                                       ██ ██ ██ ██ ██ ██ ██ ██ ██ ██       ██ ██                     
                                       ██ ██ ██ ██ ██ ██ ██    ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██      
                                       ██ ██ ██ ██ ██ ██ ██    ██ ██ ██ ██       ██ ██ ██ ██ ██ ██   
                                          ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██       ██ ██    ██ ██ ██   
                     ██ ██                ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██       ██       ██ ██ ██   
                     ██ ██       ██       ██ ██    ██    ██ ██ ██ ██ ██ ██    ██ ██ ██ ██ ██ ██ ██ ██
                     ██ ██ ██ ██ ██    ██ ██ ██          ██ ██ ██ ██ ██ ██    ██ ██ ██ ██ ██ ██ ██ ██
                  ██ ██ ██    ██ ██ ██ ██ ██    ██ ██ ██ ██ ██ ██ ██    ██ ██ ██ ██ ██ ██ ██ ██      
                  ██ ██ ██ ██    ██ ██ ██          ██ ██ ██          ██ ██ ██ ██ ██ ██ ██ ██         
               ██ ██ ██ ██             ██ ██                         ██    ██ ██ ██ ██ ██ ██ ██      
                           ██ ██ ██    ██ ██ ██                      ██ ██ ██ ██                     
      ██ ██ ██ ██          ██ ██ ██       ██ ██ ██                   ██ ██ ██ ██                     
██ ██ ██ ██    ██ ██       ██ ██ ██ ██    ██ ██ ██                                                   
██ ██ ██    ██ ██          ██ ██    ██ ██ ██                                                         
██ ██ ██    ██ ██ ██ ██ ██ ██ ██       ██ ██                                                         
            ██ ██ ██ ██ ██    ██ ██ ██                                                               
                        ██ ██ ██ ██ ██ ██                                                            
                  ██ ██ ██ ██ ██    ██                                                               
               ██ ██ ██ ██ ██ ██ ██ ██                                                               
            ██ ██ ██ ██ ██ ██                                                                        
      ██ ██ ██ ██ ██ ██ ██ ██ ██                                                                     
      ██ ██ ██ ██ ██ ██ ██ ██                                                                        
               ██ ██ ██    ██                                                                        
                  ██                                                                                 

Starting Position: (0, 0)
Ending Position: (-10, 4)

sh-5.1$ /usr/bin/python3 ".../random-walk/random_walk.py"


Random Walk in 2-Dimensions.

                                                                     ██ ██ ██ ██       ██         
                                                                  ██ ██ ██    ██ ██ ██ ██         
                                                               ██ ██ ██ ██ ██ ██ ██ ██ ██         
                                                                           ██ ██ ██    ██         
                                                ██ ██ ██                   ██       ██ ██         
                                                ██ ██ ██ ██ ██          ██ ██ ██ ██ ██            
                                                ██          ██       ██ ██ ██ ██ ██               
                                                ██       ██ ██          ██ ██ ██ ██ ██            
                                                            ██ ██       ██ ██ ██ ██ ██ ██         
                                                            ██ ██ ██ ██ ██    ██ ██    ██         
                                                               ██ ██ ██ ██    ██       ██         
                                                                     ██ ██ ██ ██ ██ ██            
                                                            ██ ██ ██ ██ ██ ██ ██ ██ ██            
                                                            ██ ██ ██ ██ ██ ██ ██ ██               
                                                            ██ ██ ██ ██ ██ ██    ██ ██ ██         
                                                            ██ ██ ██ ██ ██ ██    ██ ██ ██         
                                                               ██ ██ ██ ██ ██    ██ ██            
                                                                  ██ ██ ██ ██    ██ ██            
                                                            ██ ██ ██ ██ ██       ██ ██            
                                                               ██ ██ ██ ██ ██    ██ ██            
                                                               ██ ██ ██ ██ ██ ██ ██               
                                                      ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██            
                                                            ██ ██ ██ ██ ██    ██ ██               
                                    ██ ██ ██ ██       ██ ██ ██       ██ ██    ██                  
                        ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██       ██ ██ ██ ██          ██ ██   
                        ██ ██ ██ ██ ██ ██ ██ ██ ██ ██    ██       ██ ██ ██ ██ ██       ██ ██ ██   
                  ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██       ██ ██ ██ ██ ██ ██ ██ ██       ██    ██   
                     ██ ██    ██ ██ ██ ██                         ██ ██    ██ ██ ██ ██ ██    ██ ██
                     ██ ██       ██ ██ ██                                  ██ ██ ██ ██       ██ ██
               ██    ██          ██ ██ ██ ██                            ██ ██                   ██
         ██ ██ ██ ██ ██          ██ ██ ██ ██ ██                         ██ ██                   ██
      ██ ██ ██ ██ ██ ██ ██ ██    ██ ██ ██ ██                               ██ ██ ██    ██       ██
   ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██                         ██ ██ ██ ██ ██ ██ ██ ██
██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██                            ██ ██ ██ ██ ██ ██      
██ ██ ██    ██ ██    ██             ██       ██                               ██ ██ ██ ██ ██      
   ██ ██ ██ ██ ██ ██ ██             ██ ██ ██ ██    ██                                             
               ██ ██                ██ ██    ██ ██ ██ ██                                          
               ██ ██                         ██ ██ ██ ██                                          
               ██                               ██ ██ ██                                          
                                                   ██ ██                                          
                                             ██ ██ ██                                             
                  ██ ██ ██ ██ ██       ██ ██ ██ ██ ██ ██                                          
                     ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██ ██                                       
                           ██ ██ ██ ██ ██ ██ ██ ██ ██ ██                                          
                           ██ ██          ██ ██ ██ ██ ██                                          
                                             ██       ██                                          

Starting Position: (0, 0)
Ending Position: (10, -34)
```
