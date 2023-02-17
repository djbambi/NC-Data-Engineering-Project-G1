#!/bin/bash
# this scripts adds the input file to the zip with pg8000 dependencies
# zip file should exist either in the current directory or in the PYTHONPATH !

#arguments: 
#$1:path [c]current path  or [p]YTHONPATH , input .py file (relative to path), output.zip file (relative to path)
#best usage: set the PYTHONPATH to the lambda directory first, and then run the script from the deployment direct

if [[ $1 == "p" || $1 == "P" && $PYTHONPATH != "" ]]; then
    path=$PYTHONPATH
else
    path=$(pwd)
fi
in_name=$2
out_name=$3
if [[ ${in_name:0:1} == "/" ]]; then
    in_name=${in_name:1}
fi
#full paths
in_file_path="$path/${in_name}"

if [[ ${out_name:0:1} == "/" ]]; then
    out_name=${out_name:1}
fi
out_file_path="$path/${out_name}"

zip_path=$(pwd)
zip_file="$zip_path/pg8000_dep.zip"

if [[ ! -e $zip_file ]]; then
    zip_file="$PYTHONPATH/pg8000_dep.zip"

fi
in_name_base=${in_name##*/}
if [[  -e $zip_file ]]; then
    cd $(pwd)
    cp $in_file_path $in_name_base
    zip -g  $zip_file $in_name_base
    cp $zip_file $out_file_path
    rm $in_name_base
    
    #echo $in_file_old
    #echo $out_file
else
    echo pg8000 zip does not exists
fi
