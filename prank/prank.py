import os
import re

def rename_files():
    prank_files = os.listdir(r"D:\Python\Udacity-Python\prank");

    for file in prank_files:
        newfile = re.sub(r'\d', '', file)
        os.rename(file, newfile)
    

    
rename_files();
