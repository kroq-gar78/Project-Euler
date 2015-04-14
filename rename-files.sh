#!/bin/bash

# only take care of python or data files because in Java, you have to edit the class names too


for i in $(ls | egrep "problem([0-9]{1,3}).*\.(py|txt)"); do
    num=$(printf '%03d' $(echo $i|egrep -om1 "[0-9]{1,3}"))
    #echo $num $i
    newfile=$(echo $i|sed "s/problem[0-9]*/p$num/")
    #echo $newfile
    
    # needs two moves because some files aren't in git, and we need to move those too
    git mv -v "$i" "$newfile"
    mv -v "$i" "$newfile" 
done
