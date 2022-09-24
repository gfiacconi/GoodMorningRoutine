#!/bin/bash

cd Desktop
#find what time it is and the current date
date=$(date +%d-%m-%Y)
time=$(date +%H:%M)
#find what day it is
day=$(date +%A)
# say 'buongiorno gabriele' and the current date and time
say "buongiorno gabriele, oggi è $date, $day e sono le $time"
python GoodMorning.py






