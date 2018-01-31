# SAT-sudoku

## Initial setup
Following environment variables are to be exported before running z3py python scripts -
```
export LD_LIBRARY_PATH=${z3_location}/build
export PYTHONPATH=${z3_location}/build/python
```

Ideally, the python scripts should be run inside `build/python` under the local z3 installation directory. However, the directory `build/python/z3` can be symlinked to the project root and all the python scripts can then be invoked where they are located.

All the above instructions are encapsulated in [`setup.sh`](setup.sh), and the initial setup can be done via `./setup.sh`.
**NOTE:** Update the location variables used in the script before proceeding to run it.

## Running
[`pattern.py`](pattern.py) contains encoding for sudoku solving patterns (WIP), and running it should generate an incompletely solved sudoku puzzle with a few fixed and rest pencilled entries.

----
### _Everything below this point was written a year back and may no longer be valid._

## Grammar definitions
The grammar used is defined in [grammar.py](grammar.py).

## Results and Benchmarks
* **Sudoku-Generator:** <br>
  For generating a valid 9x9 grid (satisfying all the 4 constraints) -
  ```
  python sudoku-generator.py  25.28s user 0.02s system 99% cpu 25.333 total
  ```

  For multiple iterations, same variation of sudoku was generated.

  For generating a valid sudoku using the generated 9x9 grid - <br>
  Program was taking too long to halt, possibly because the **random selection** of indices `(i,j)` to be removed from the generated grid contributes greatly to the non-determinism, since as the grid gets close to being sparsely populated (many empty cells), the probability of a randomly generated non-empty cell keeps decreasing

## Todo
* Reduce the grid into a 3-D binary form which can be fed directly to the SAT solver.
* Find a better way of selecting cells to be removed from a valid 9x9 grid for generating a sudoku. A random selection (not optimal) is being used currently.
