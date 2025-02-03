#!/bin/bash

directory=$1

if [ -z "$directory" ]; then
    echo "Please provide a directory."
    exit 1
fi

if [ ! -d "$directory" ]; then
    echo "Directory not found: $directory"
    exit 1
fi

for file in "$directory"/*; do
    if [ -f "$file" ] && [ ! -s "$file" ]; then
        echo "Deleting empty file: $file"
        rm "$file"
    fi
done

