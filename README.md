# Art Parser

## Solution

- The source code for this project is written in Python, and is present in the `src` folder
- The data files provided are present in the `data` folder
- To run the code, do the following:
```
python Driver.py --paths /absolute/path/to/data/file1 /absolute/path/to/data/file2 ...
```

It accepts any number of directories with any number of files with a HTML source similar to the files in the `data` directory.

## Dependencies

The only dependencies needed to run this code is `BeautifulSoup` for HTML parsing, and `argparse` for command line arguments.
[Installation instructions for BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Code structure

`ArtParser` is the main class that contains functions for parsing HTML files.
Some helper functions are present in `utils`. `Driver` is the main entry point for the code. 
