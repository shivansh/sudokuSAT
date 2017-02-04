# SAT-sudoku

## Initial setup
Following environment variables are to be exported before running z3py python scripts -
```
export LD_LIBRARY_PATH=~/software-downloads/z3/build && export PYTHONPATH=~/software-downloads/z3/build/python
```
----

## Results and Benchmarks
* **Sudoku-Generator:** <br>
  For generating a valid 9x9 grid (satisfying all the 4 constraints) -
  ```
  python sudoku-generator.py  25.28s user 0.02s system 99% cpu 25.333 total
  ```

  For multiple iterations, same variation of sudoku was generated.

  For generating a valid sudoku using the generated 9x9 grid - <br>
  Program was taking too long to halt, possibly because the **random selection** of indices `(i,j)` to be removed from the generated grid contributes greatly to the non-determinism, since as the grid gets close to being sparsely populated (many empty cells), the probability of a randomly generated non-empty cell keeps decreasing
