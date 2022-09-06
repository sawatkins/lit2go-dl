# lit2go-dl
lit2go-dl is a python script to download audiobooks from [lit2go's](https://etc.usf.edu/lit2go/) free online collection. The script 1.) prompts for a link from [this](https://etc.usf.edu/lit2go/books/) page, 2.) creates a folder with the book's title, and 3.) downloads each chapter in order. Audio files are downloaded as tagged mp3s, so author and chapter information should show up on any media player.

## Prerequisites
The python package `Beautiful Soup` available in `bs4`.

    pip3 install bs4
    
## Installation
Download the script:

    wget https://raw.githubusercontent.com/sawatkins/lit2go-dl/master/lit2go-dl.py

## Usage
Find and copy a link to an audiobook from [this](https://etc.usf.edu/lit2go/books/) page. Example: `https://etc.usf.edu/lit2go/21/the-adventures-of-huckleberry-finn/`. Then, run the script:

    python3 lit2go-dl.py


***    
#### Known Issues
There are a few bugs with user validation and numbering. Planning to polish the script when I get a chance.
