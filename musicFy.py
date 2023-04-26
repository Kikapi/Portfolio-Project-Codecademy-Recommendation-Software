
from linkedList import *
from music import *
import csv

def search_again():
    new_input = input("\nDo you want to search again? Enter y for yes and n for no\n")
    if new_input == 'y':
        return True
    else:
        return False


print("""
*********************************************

**********    WELCOME TO MUSIC-FY  **********

*********************************************

 ---------------------------------------------------------             
|***  WHAT KIND OF MUSIC DO YOU FANCY TO HEAR TODAY???  ***|
----------------------------------------------------------  """)

#load musics into music_collection:
myCollection = Music_Collection()
with open('musics.csv') as musics_file:
    musics_file_dict = csv.DictReader(musics_file)
    for row in musics_file_dict:
        music = Music(row['title'], row['artist'], row['genre'])
        myCollection.add_music(music)

#get input from user and check if input partially matches any artist or genre in the collection
selected_music = ""
while len(selected_music) == 0:
    user_input = input("\nEnter the beginning of the artist or genre you want to look for: \n")
    artist_options = myCollection.find_artist_options(user_input)
    genre_options = myCollection.find_genre_options(user_input)
    
    #No matches found 
    if len(artist_options) == 0 and len(genre_options) == 0:
        print('\nNo artists or genres matching "{0}" were found. '.format(user_input))
        
        if not search_again():
            selected_music = "end"

    #if only one match for artist was found   
    elif len(artist_options) == 1 and len(genre_options) == 0:
        new_input = input("\nDo you want to check out {0}'s music? Enter y for yes and n for no\n".format(artist_options[0]))
                
        if new_input == 'y':
            myCollection.search_music_by_artist(artist_options[0])
            
        if not search_again():
            selected_music = "end"

    #if only one match for genre was found   
    elif len(genre_options) == 1 and len(artist_options) == 0:
        new_input = input("\nDo you want to check out {0} musics? Enter y for yes and n for no\n".format(genre_options[0]))
                
        if new_input == 'y':
            myCollection.search_music_by_genre(genre_options[0])
            
        if not search_again():
            selected_music = "end"

    #if more than 1 matches were found:
    else:
        print("{0} artists matching {1}: ".format(len(artist_options), user_input))
        print(list(artist_options))
        print("{0} genres matching {1}: ".format(len(genre_options), user_input))
        print(list(genre_options))

print("""Thank you for using musicFy!
      See you next time!!!""")

   

