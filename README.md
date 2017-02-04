# SAT-sudoku

## Initial setup
Following environment variables are to be exported before running z3py python scripts -
```
export LD_LIBRARY_PATH=~/software-downloads/z3/build && export PYTHONPATH=~/software-downloads/z3/build/python
```
----

## Results and Benchmarks
* **Sudoku-Generator:** <br>

  ```
  python sudoku-generator.py  25.28s user 0.02s system 99% cpu 25.333 total
  ```

  For multiple iterations, same variation of sudoku was generated.
