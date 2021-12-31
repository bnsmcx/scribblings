#!/bin/bash

diff -rq temp_a temp_b | while read line; 
	do 
		source_file=$(echo $line | cut -d" " -f2); 
		dest_file=$(echo $line | cut -d" " -f4); 
		cp $source_file $dest_file;
	done
