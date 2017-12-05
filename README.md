# Anti-Duplicator
The program recursively seeks duplicated files in a folder and prints result in console.

# How to Install
You just need to download and install python3 if you already haven't: http://python.org .

# How to use
Seeking duplicates in current directory:

```
python duplicates.py .

There is the list of found duplicates:

.\test1\test1.txt
.\test1\test2\test3\test4\test1.txt
.\test1\test2\test3\test4-2\test1.txt
.\test1\test2\test3\test4-2\test5-2\test6-2\test7-2\test1.txt

.\test1\test2\README.md
.\test1_1\test2_2\README.md
.\test1\test2\test3\test4-2\README.md
.\test1\test2\test3\test4-2\test5-2\test6-2\README.md
```

# Project Goals
The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
