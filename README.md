# IndexHelper
## Introduction

I created Index Helper to assist with my workflow for writing monograph indexes. As I read through the page proofs, I tell Index Helper what page I am on and what terms to assign to that page. When I am done, I have a .txt file with an alphabetical list of terms and their page numbers.
### What Index Helper Can't Do:

Index Helper doesn't help create any cross references, subentries, or special formatting; nor does it create page number ranges. 
### How To Use Index Helper:

When you run Index Helper you will see a field labeled "Enter Page Number." Your current page number goes there. Add your terms one by one to the "Enter Terms" field and press return after each addition. You will see your terms displayed in the window below. If you make a mistake do not try to fix it in the window. You will have a chance to edit later. When you move on to another page, simply replace the page number and continue adding terms. When you are done, press the "save" button and save your file as a .txt file.

To add more terms to an existing index, just start writing your page numbers and terms as above, THEN go to File > Update and choose the index you want to add to.

If you want to view and edit an existing index, go to File > Open and select which index you want to view. You can make spelling or page number corrections but please be careful to follow the existing formatting with spaces, commas, and colons- otherwise it may not save. When you are done with your edits, go to File > Save Changes.

Index Helper saves your index as a json dictionary, which doesn't look like a book index. When you are done working you can choose File > Format and select your index to format it as a nice alphabetical list of terms and page numbers.
## Built With

Python
## Prerequisites

-Python 3.11

-Libraries installed from requirements.txt
## Installation

1. download the indexhelper.py, ihgui.py, and requirements.txt files in a new project folder
2. download the required libraries to run this script by running this command in your IDE: pip install -r requirements.txt

## If you are an indexer and just want to try Index Helper as an app: 

Please contact me and I will send you and exec file for your operating system.
