#!/usr/bin/bash
source /home/hodalys/miniforge3/etc/profile.d/conda.sh
eval "$(conda shell.bash hook)"
conda activate iccd332
python3 main.py
