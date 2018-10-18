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

**Topic: Pipes and Filters + Loops**

Ctrl-C kills the process  
Ctrl-D ends line  
Ctrl-A brings you to beginning of line  
Ctrl-E brings you to end of line  
echo “hgsj fdhg akrgwkfsh” | wc -c  
Write loops for human readers, I.e. ‘for filename in … do … $filename’ instead of ‘for x in … do … $x’  
\* matches zero or more characters  
Ctrl-Z to pause job 


### September 17, 2018

**Topic: Less and man**

Put g ahead of commands to use GNU version of it

**Topic: Searching**

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

**Exercise 1 solution**

For i in {1..9}  
do  
mv ../log/timetest{$i}_* ../log/timetest0{$i}_*  
mv ../out/timetest{$i}_* ../out/timetest0{$i}_*  
done 

* do not track large data files  
* only track files that need version control  

### September 26, 2018

* make sure to pull often!  
* use git status to check and get directions  

### October 1, 2018

* Make comments short  
* Don't document mechanics  
* Comment assumptions (i.e. assumes h<= 9)
* Comment on variable name if it is shortened/ not obvious  

Excercise: grep "ENSMUSG00000033793" Mus_musculus.GRCm38.75_chr1.gtf | cut -f 3 | sort | uniq  -c  

Most important thing to know for sed:  
sed s/pattern/replacement/ filename > newfile # do NOT redirect to input file!  

Option to replace your input file:  
sed -i s/pattern/replacement/ filename # for in-place replacement  

Best to enclode 's/pattern/placement/'  
- Unless there are variables inside  

Keeps 3 things in memory (e.g. (chr[^:]+) is 1)
* echo "chr12:74-431" | gsed -E 's/^(chr[^:]+):([0-9]+)-([0-9]+)/\1\t\2\t\3/'  
*  1:2-3 replaced by 1 tab 2 tab 3  

### October 3, 2018

-o is or
! is not
-lt is less than
$# is argument 

### October 10, 2018

awk is good for really long files, tabular data
no $ for variables within awk
getting data from the web: wget  

### October 15, 2018

git clone git@github.com:UWMadison-computingtools-2018/zmays-snps.git 

### October 18, 2018

git branch exercise 

Students are annoying who is this lady that is with Bill?s
Sorry I was on the wrong branch this sucks a lot.
