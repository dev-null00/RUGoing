#!/bin/bash

echo "run register tests"
python testRegister.py 

echo "run recommended tests"
python testRecommendedEvents.py 

echo "run rating tests"
python testRating.py 

echo "run modify account tests"
python testModUser.py 

echo "run insert event tests"
python ~/testInsert.py
