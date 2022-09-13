# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import eyed3
import os
import subprocess
import time
import datetime
import random

temp_dir_name = "temp_dir"

def main():

    #find current folder
    cd = os.getcwd()
    print(cd)
    home = os.path.join(cd,"music")
    print(home)

    print("spotDL wrapper")
    download_link = str(input("download link : "))

    music_type = str(input("what kind of link? < [A] Album | [P] Playlist | [S] Song | [U] Update Playlist> : "))

    if music_type == "U" or music_type == "u":
        folder_name = str(input("What is the playlist name? : "))
        dir_name = os.path.join(home, folder_name)
    else:

        timestamp = str(datetime.datetime.now(datetime.timezone.utc))

        timestamp = timestamp.split(" ")[-1]
        timestamp = timestamp.split("+")[0]
        timestamp = timestamp.replace(':', '')
        timestamp = timestamp.replace('.', '')

        print(timestamp)

        dir_name = os.path.join(home, (temp_dir_name + timestamp))

        try:

            os.mkdir(dir_name)
            print("Directory [{}] Created".format(dir_name))
        except FileExistsError:
            print("Directory [{}] already exists".format(dir_name))

    #change directory and start download
    os.chdir(dir_name)

    # Run spotDL
    subprocess.run(["spotDL",download_link])

    #get tag information

    #delete all non mp3 files
    for (dirpath,dirnames,filenames) in os.walk(dir_name):
        for file in filenames:
            if ".spotdl-cache" in file or ".mp3" not in file:
                os.remove(os.path.join(dirpath,file))

    song_paths = []
    index = 0
    for (dirpath, dirnames, filenames) in os.walk(dir_name):
        for file in filenames:
            song_paths.append(os.path.join(dirpath,file))
            print("Filepaths [{}]: {}".format(index,song_paths[index]))
            index = index + 1

    audiofiles = []

    for file in song_paths:
        audiofiles.append(eyed3.load(file))


    if music_type == "A" or music_type == "a":
        folder_name = process_album(audiofiles)
    elif music_type == "P" or music_type == "p":
        folder_name = process_playlist(audiofiles)
    elif music_type == "S" or music_type == "s":
        folder_name = process_song(audiofiles)

    rename_folder(dir_name, folder_name)

def process_album(audiofiles):
    album_name = audiofiles[0].tag.album

    same_album = True
    # check to see if all album names are the same
    for audiofile in audiofiles:
        if audiofile.tag.album != album_name:
            same_album = False

    #allow for the files to finish downloading
    time.sleep(5)

    if same_album != True:
        print("Album on some items do not match")

        album_match_decision = str(input("Choices: < [A] Change Album Name | [D] Delete files with album keyword[s]"))

        if album_match_decision == "A" or album_match_decision == "a":
            album_name = rename_album(audiofiles)
        elif album_match_decision == "D" or album_match_decision == "d":
            delete_files_with_tag(audiofiles, "A")

    add_genre(audiofiles)

    return album_name

def process_playlist(audiofiles):
    print("\n")
    playlist_name = str(input("Name your playlist : "))

    #add_genre(audiofiles)

    return playlist_name

def process_song(audiofiles):
    print(audiofiles)

def add_genre(audiofiles):
    print("Current Genre(s):")

    for audiofile in audiofiles:
        print("\t{} \t\t\t\t\t | {}".format(audiofile.tag.title, audiofile.tag.genre))

    change_genre = str(input("would you like to change genre? <[Y]/[N]"))

    if change_genre == "Y" or change_genre == "y":
        new_genre = str(input("enter genre : "))

        for audiofile in audiofiles:
            audiofile.tag.genre = new_genre
            audiofile.tag.save()

def rename_album(audiofiles):
    new_album_name = str(input("Manual Album Name: "))
    for audiofile in audiofiles:
        audiofile.tag.album = new_album_name
        audiofile.tag.save()

    return new_album_name

def delete_files_with_tag(audiofiles, tag):

    for audiofile in audiofiles:
        print(audiofile.path)

    keylist_str = str(input("input list of keywords with commas separating"))

    keylist = keylist_str.split(",")

    for audiofile in audiofiles:
        for key in keylist:
            # if album
            if tag == "A" or tag == "a":
                if key in audiofile.tag.album:
                    os.remove(audiofile.path)







def rename_folder(dir_name, new_dir_name):



    temp_dir = os.path.join(home,dir_name)

    os.chdir(os.path.join(temp_dir,r"..\\"))

    new_dir = os.path.join(home,new_dir_name)

    os.rename(temp_dir,new_dir)


        # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
