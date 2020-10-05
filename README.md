# image-profiling
Profiling tool for images.

## Guide

1. In `UDA_profiling.py` uncomment first 4 lines in `main()` function.
2. Run `UDA_profiling.py` to generate csv files for OAI and NYU
3. Comment first 4 lines of the `main()` function and uncomment the last 4 lines
4. Open docker service and go to `docker-profiling` directory and run `run.sh`
5. Inside docker, run `python3 UDA_profiling.py` to generate html files.
