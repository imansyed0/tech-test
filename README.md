# Technical test for Software Engineer candidates`

## Building
`git clone https://github.com/imansyed0/bookcreator-test.git`

## Running
python 3.7.6
Windows 10.0.19041

1. If you want to use your own test items, overwrite the file 'testitems.txt' with your desired file. if not, the program will clean the premade list in 'testitems.txt'.
2. Run 'bctest.py' in a python interpreter. 
3. Cleaned items from 'testitems.txt' will be written into file 'cleanitems.txt'.

## Assumptions:
- Word from block list should only be blocked in items if it appears as a whole word.

## Design Decisions
To approach undestanding 'bctest.py' we can break it down as follows:
1. Input a text file to be cleaned and a block list
2. Converts each file to respective python lists where each item is a string corresponding to a line of text
3. Searches each string from the strings to be cleaned sequentially for each blocked word (with suitable adjustments)
4. If a word is found, do nothing and move on to the next string to be cleaned
5. If no blocked word is found, as the clean item to an initally empty list
6. Convert the list of cleaned items to a text file

- I began by trying to get the program to generate a list of blocked lines then 'subtract' it from the original lines of the item. I realised quickly that this would be computationally expensive as it would require a lengthy comparison of the two lists. Instead, I changed it to only write the clean lines into a list.
- If a string in the block list is a substring of another word, eg. 'bad' and 'badminton', you don't want to block the other word. So I used the `re` python package to only look for whole strings.
- If a word has a different sequence of capital and lower case letters but is the same word, eg. 'Terrible' and 'terrible', you still want to block both. So I made strings from both files all lowercase.
- The generation of clean lines is iterative so will make duplicates if there is multiple blocked words eg 'I had a bad bad day'. So I made the program move on when it discovers the first blocked word in an item.

[book]: https://read.bookcreator.com/Gr0k3Ie4s3gXU7stHRzFJiILKD83/UEzOFQjyR121W1pKRm47Lg