# lit2go-dl
lit2go-dl is a python script to download audiobooks from [lit2go's](https://etc.usf.edu/lit2go/) free online collection. The script:
1. Prompts for an audiobook link from [this](https://etc.usf.edu/lit2go/books/) page
2. Creates a folder with the book's title
3. Downloads and numbers each chapter as a tagged mp3

Author and chapter information should show up in media players, since the audio files are tagged.

## Prerequisites
The python package `Beautiful Soup` is required from `bs4`. To install, run:

    pip3 install bs4
    
## Installation
Download the script:

    wget https://raw.githubusercontent.com/sawatkins/lit2go-dl/master/lit2go-dl.py

## Usage
Copy a link to an audiobook from [this](https://etc.usf.edu/lit2go/books/) page. Example: `https://etc.usf.edu/lit2go/21/the-adventures-of-huckleberry-finn/`. Then, run the script:

    python3 lit2go-dl.py


***    
### Known Issues
There could be some issues with user validation and numbering.

### Future Plans
Fix known issues and allow downloading from cli arguments.
