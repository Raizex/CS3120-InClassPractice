#!/bin/bash

# File deletion code modified from https://stackoverflow.com/a/31318241
if [ -f output.txt ] ; then
    rm output.txt
fi

echo "Name: Justin Huffman" >> output.txt
echo "Date: $(date)" >> output.txt
echo "Class: Machine Learning" >> output.txt
echo "Assignment: In Class Practice $1" >> output.txt
echo "Source code: https://github.com/$(git config remote.origin.url | cut -f 2 -d ':' | cut -f 1 -d '.')/tree/master/$1" >> output.txt
echo "" >> output.txt

# Execution code modified from https://stackoverflow.com/a/10523501
for file in $1/*.py
do
    echo "---------" >> output.txt
    echo "$file" | cut -d "/" -f 2 >> output.txt
    echo "---------" >> output.txt
    python3 "$file" >> output.txt
    echo "---------" >> output.txt
    echo "" >> output.txt
done
