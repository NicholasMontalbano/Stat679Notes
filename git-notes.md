# Stat 679 Notes 

### September 10, 2019

* Relative paths are more portable and better to use  
  * If I want to share code with other person, their directory will be different from mine – absolute paths will be different  
  * Also, if you relocate your own files  
* Spaces in names  
  * Ex. “rmdir raw sequences” will try to remove both ‘raw’ AND ‘sequences’ instead of ‘raw sequences’ 
  * Have to add \\
  * rmdir raw\ sequences
  * Instead, use -, _, capitalized letters (rawSequences)
  * Word documents, files, all no spaces  
* Some programs do not generate output files themselves, but instead require that empty files have already been generated. When the program is run, it searches for an existing file to populate with its output. The touch command allows you to efficiently generate a blank text file to be used by such programs.
* Deleting is forever
* “rm -r” is a recursive algorithm
  * Starts from the bottom of the directory and works its way up until it deletes the directory
* Before doing something irreversible, replace ‘rm’ with ‘echo’ to see what you will actually be doing (good for when using r* and nonspecific commands)

### September 11, 2018

Topic: Pipes and Filters + Loops

Ctrl-C kills the process  
Ctrl-D ends line  
Ctrl-A brings you to beginning of line  
Ctrl-E brings you to end of line  
echo “hgsj fdhg akrgwkfsh” | wc -c  
Write loops for human readers, I.e. ‘for filename in … do … $filename’ instead of ‘for x in … do … $x’  
\* matches zero or more characters  
Ctrl-Z to pause job 


### September 17, 2018

Topic: Less and man

Put g ahead of commands to use GNU version of it

Topic: Searching

Shell
  * \* = anything, any length
  * ? = one character
  * . = .
regexp is different
* Ex.
  * To check what we’re doing is ok: grep -v “^>” tb1.fasta | less
  * Then just keep: grep -v “^>” tb1.fasta
  * grep -v “^>” tb1.fasta | grep [^ACGTacgt] | less
  * grep -v “^>” tb1.fasta | grep --color [^ACGTacgt]
  * grep -v “^>” tb1.fasta | grep -o [^ACGTacgt]
  * grep -v “^>” tb1.fasta | grep -on [^ACGTacgt]
  * grep -v “^>” tb1.fasta | grep -oni [^ACGT]
  * grep -v “^>” tb1.fasta | grep -oni [^acgt]

### September 19, 2018

grep -c “| GTR+G “ partitionfinder.txt 
grep -E  ‘^\s+$’ partition.txt | wc
rm $(find ~ -name “.DS_Store”)

### September 23, 2018

Exercise 1 solution

For i in {1..9}  
do  
mv ../log/timetest{$i}_* ../log/timetest0{$i}_*  
mv ../out/timetest{$i}_* ../out/timetest0{$i}_*  
done 

* do not track large data files  
* only track files that need version control  