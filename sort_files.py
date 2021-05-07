#! /bin/env python
"""
Main point of code execution. Most other files are imported to here.

Quick Start:
1. Open the program Anaconda Prompt
2. Go to the code location by typing 'cd Path\to\sort_files'
3. type 'python sort_files.py'

"""
#%% import dependencies #######################################################
#import time #for log_data.py
from builtins import input
from builtins import zip
from builtins import range
import shutil
import pandas as pd #for input_specimens.py
import idigbio #for query_idigbio.py
import sys #for exiting if there's a problem
import os #to check if files exist
import re #for stripping file endings, etc.
import copy
import os, re, csv

import user_configuration as uc

#%% #Start. Get the files in. #################################################
print('\nStarting...')
#%% Scan metadata files########################################################

if uc.FOLDER_TO_SCREEN is not None and uc.OUTPUT_PATH is not None: 
    # make the directory for the ones not in idigbio
    #run the extract settings script, modified temporarily
    FileNames = []
    print("Checking files in " + uc.FOLDER_TO_SCREEN + "...")
    if os.path.isdir(uc.FOLDER_TO_SCREEN): #check to make sure the folder exists
    	print('Path to files found.')
    	for file in os.listdir(uc.FOLDER_TO_SCREEN):
            sub_dir = os.path.join(uc.FOLDER_TO_SCREEN, file)
            # only take the names of the sub directories - these will be the folders that hold each specimen's data
            if os.path.isdir(sub_dir):
                filename_nodate = file.split(" [")[0]
                #split museum/collection/number from notes section
                identifier = filename_nodate.split("_")[0]
                components = identifier.split("-")
                museum = components[0].lower()
                collection = components[1].lower()
                number = components[2]
                
                if collection == "fish" and museum == "ummz":
                    collection = "ummz_fish"
                
                Query = {"institutioncode": museum,
                 "catalognumber": number,
                 "collectioncode": collection}
                api = idigbio.json() #shorten
                TempRecords = api.search_records(rq= Query )
                if not bool(TempRecords['items']):
                    ## this means that no record was found on idigbio. append an empty item instead
                    print("Missing " + number)
                    if uc.TEST_RUN:
                        FileNames.append(file)
                    else:
                        print("Moving folder to new directory...")
                        destination = uc.OUTPUT_PATH
                        print(destination)
                        # make the new directory if it doesn't exist
                        if not os.path.isdir(destination):
                            os.makedirs(destination)
                        dest = shutil.move(sub_dir, destination, copy_function = shutil.copytree)
                        print("Folder moved to " + dest)
                else:
                    print("Found " + number)
        
    
    else:
        sys.exit('Path to folder to screen not found.')    
    
    
    if uc.TEST_RUN:
        print("\nExecuting this code with TEST_RUN=False would move the following folders to the iDigBio Entries Missing directory:")
        print(*FileNames, sep="\n")
                
else:
    sys.exit('Path to folder to screen not set in user configuration file.')
