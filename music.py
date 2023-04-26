import random
from linkedList import LinkedList
class Music_Collection:
    def __init__(self):
        self.list_musics = {}
        self.genres = []
        self.artists = []

    def add_music(self, music):
        
        genre = music.genre
        if genre not in self.genres:
            self.genres.append(genre)
        
        artist = music.artist
        if artist not in self.artists:
            self.artists.append(artist)
            self.list_musics[artist] = LinkedList(music)
        else:                        
            self.list_musics[artist].insert_beginning(music) 

    def find_genre_options(self, input):
        options = []
        for genre in self.genres:
            if (genre.lower().startswith(input.lower())) and (genre not in options):
                options.append(genre)        
        return options
            
    def find_artist_options(self, input):
        options = []
        for artist in self.artists:
            if (artist.lower().startswith(input.lower())) and (artist not in options):
                options.append(artist)
        return options
    
    def search_music_by_genre(self, genre):
        result = []
        for artist in self.list_musics:
            current_node = self.list_musics[artist].head_node
            while current_node:
                if current_node.get_value().genre == genre:
                    result.append(current_node.get_value())
                current_node = current_node.get_next_node()
        quicksort_by_popularity(result, 0, len(result) - 1)
        
        if len(result) < 5:
            top_music = len(result)
        else:
            top_music = 5
        print("\nTop {0} {1} musics:\n".format(top_music, genre))
        for i in range(top_music):
            print("- - - - - - - - - -\n")
            result[i].print()
    
    def search_music_by_artist(self, artist):
        result = []
        current_node = self.list_musics[artist].head_node
        while current_node:
            result.append(current_node.get_value())
            current_node = current_node.get_next_node()
        quicksort_by_popularity(result, 0, len(result) - 1)
        
        if len(result) < 5:
            top_music = len(result)
        else:
            top_music = 5
        print("\nTop {0} musics by {1}:\n".format(top_music, artist))
        for i in range(top_music):
            print("- - - - - - - - - -\n")
            result[i].print()



def quicksort_by_popularity(list, start, end):
    if start >= end:
        return
    pivot_idx = random.randrange(start, end + 1) 
    pivot_elem = list[pivot_idx].likes 
    list[pivot_idx], list[end] = list[end], list[pivot_idx]

    great_than_pointer = start

    for i in range(start, end):
        if list[i].likes > pivot_elem:
            list[i], list[great_than_pointer] = list[great_than_pointer], list[i]
            great_than_pointer += 1
        else:
            list[end], list[great_than_pointer] = list[great_than_pointer], list[end]

    quicksort_by_popularity(list, start, great_than_pointer - 1)
    quicksort_by_popularity(list, great_than_pointer, end)


        

class Music:

    def __init__(self, title, artist, genre):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.likes = random.randint(0, 100)
        
    def popularity(self):
        if self.likes < 10:
            return " "
        elif self.likes < 30:
            return "*"
        elif self.likes < 50:
            return "**"
        elif self.likes < 70:
            return "***"
        elif self.likes < 85:
            return "****"
        else: 
            return "*****"
        
    def print(self):
        print("Title: {0}\nArtist: {1}\nGenre: {2}\n{3}  {4}".format(self.title, self.artist, self.genre, self.likes, self.popularity()))

