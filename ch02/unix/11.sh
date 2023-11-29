#!/bin/bash

sed  's/\t/ /g' popular-names.txt

cat popular-names.txt | tr "\t" " "

expand popular-names.txt