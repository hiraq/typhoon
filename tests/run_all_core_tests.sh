#!/bin/bash

#python -m unittest discover -p '*_test.py' -v

nosetests --config=core.cfg -w core
