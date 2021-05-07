# Deep Blue Data Pre-Processing: Separate Out Specimens that are Missing Records (e.g. in iDigBio)
1. Open Anaconda Prompt
2. Navigate to the drive and the folder where the code lives
	`cd deepblue_transfer/other/deep_blue_preupload_sorting`
3. Open the file `user_configuration.py` (in e.g. Notepad++, or your favorite text editor). It is located in the `deep_blue_preupload_sorting` folder. It has the following arguments that you should set or make sure are correct:
- `OUTPUT_PATH` - This is where you set what folder the specimens with missing entries will be moved to by the script. My recommendation is to put them under the deepblue_transfer folder, in their division, in a folder called “iDigBio_Entries_Missing” and then whatever week they are associated with, as is done in the example screenshot below.
- `FOLDER_TO_SCREEN` - This is the folder that will be screened by the code for missing entries. It should be a specific week’s worth of CT scans, as in the example below.
- `TEST_RUN` - This argument determines if the code will actually perform the sorting of files or not. When it is set to True, the code will perform a “test run” where it will tell you what files would be moved, but will not actually move or change anything. If set to False, the code will actually move the files.

4. Now you are ready to run the script. Back in the Anaconda prompt window, in the deep_blue_preupload_sorting folder, type:
`python sort_files.py` and hit enter. If you have set `TEST_RUN` to True, this will just be a practice run, and the script will tell you what files it would move (in other words, which specimens are not in iDigBio). If the argument is set to False, it will actually move the files. 


