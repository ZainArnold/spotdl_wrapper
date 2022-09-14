# spotdl_wrapper
a wrapper for spotdl


Setup (for first time use):

1. Ensure you have python 3.7 at least
    1. open a command prompt
    2. type "where python"
    3. it should show you where the python.exe file is
        1. Mine was in C:\Python37\python.exe 
2. create a folder called "music" in the base folder
3. create and activate a virtual environment
    1. python3 -m venv /path/to/new/virtual/environment
        1. This path should be in the same place your main.py is held
    2. A "Scripts" folder will be made
    3. your project folder should look like this:
        - .idea [folder]
        - Include [folder]
        - Lib [folder]
        - music [folder]
        - Scripts [folder]
        - .gitignore
        - READNE.md
        - main.py
    4. open a command window in this folder location
        1. to open a command window in this folder, copy the folder path from the top path bar, open a command window, and type "cd /path/to/folder"
    6. type: "Scripts\activate"
    7. this should activate your virtual environment. A virtual environment is active when there is something in brackets in front of the command prompt
4. then, with your virtual environment running, install the following python modules
    1. "pip install eyed3, spotdl"
5. Installing FFMPEG
    1. go to the following link: https://www.gyan.dev/ffmpeg/builds
    2. download a git master build, full version
    3. extract contents of folder to a folder on your C drive called "ffmpeg"
    4. run cmd as administrator
    5. send the following command: setx /m PATH "C:\ffmpeg\bin;%PATH%"
    6. restart your computer
    7. now your venv should be able to see ffmpeg

Using the spotDL wrapper

To run:
1. start your virtual environment
    1. open cmd in folder, type "Scripts/activate"
2. type "python main.py" to run the tool
3. follow the instructions in the tool

All songs, albums, and playlists are downloaded into the music folder

Albums and Playlists work fairly similar, you find the web link that gets you to the album or playlist on spotify and paste it into the tool. The playlist option will ask you to name your playlist at the end

Update playlist will avoid downloading already downloaded songs to the playlist folder you care about, but in order for it to find your playlist folder, the name must match exactly
