#!/bin/bash

a=2
b=2
c=$((a + b))

echo "Bash says: Hello, World!"
echo "$a + $b = $c"

declare -a arr=("User1" "User2" "User3")

echo "An Array of Strings are:"

for i in "${arr[@]}"

do

echo "$i"

done

