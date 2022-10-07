#!/bin/bash
#ask the website he want to visit
echo "Who is using me?"
read name
name=$name

while [ $website != "exit" ]
do
echo "What is the website you want to visit?"
read website
website=$website
echo "$website" >> all.txt
done

#open the file and read it
cat $name.txt

