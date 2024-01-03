from Song import Song
import datetime

class Playlist:
    def __init__(self, file_name) -> None:
        self.__error_msg = "\nERROR: Playlist unavailable. Ensure the file name and type (text) are correct and located in the same directory as this program. Contact an administrator if the problem persists."
        self.__file_name = self.__format_fileName_extension(file_name)
        self.__headers = self.__set_headers()
        self.__songs = self.__set_songs()

    def __format_fileName_extension(self, file_name):
        result = ""
        if ("." in file_name):
            fileName_array = file_name.split(".")
            if (fileName_array[-1] == "txt"):
                result = ".".join(fileName_array)
            else:
                result = fileName_array[0] + ".txt"
        else:
            result = file_name + ".txt"
        return result
    
    def __display_error_msg(self):
        return self.__error_msg

    def __set_headers(self):
        try:
            with open(self.__file_name, encoding="utf-16") as playlist_file:
                headers = []
                str_header = playlist_file.readline()
                unfiltered_headers = str_header.split("\t")
                for header in unfiltered_headers:
                    header = header.strip()
                    headers.append(header)
                return headers
        except IOError:
            return []
        except Exception as ex:
            print(ex)
            quit()

    def __format_songs(self, song_data: list):
        formatted_songs = []
        for song_item in song_data:
            if (song_item.isnumeric()):
                song_item = int(song_item)
                formatted_songs.append(song_item)
            else:
                formatted_songs.append(song_item.strip())
        return formatted_songs

    def __set_songs(self):
        try:
            with open(self.__file_name, encoding="utf-16") as playlist_file:
                songs = []
                playlist_file.readline() # Skip headers row
                for str_song in playlist_file:
                    song_data = str_song.split("\t")
                    # Change string numbers to integers and strip whitespace from strings
                    formatted_songs = self.__format_songs(song_data)
                    
                    # If data and header length are the same then create a song with 31
                    if (len(song_data) == len(self.__headers)):
                        song = Song(formatted_songs[0], formatted_songs[1], formatted_songs[2], formatted_songs[3], 
                                    formatted_songs[4], formatted_songs[5], formatted_songs[6], formatted_songs[7], 
                                    formatted_songs[8], formatted_songs[9], formatted_songs[10], formatted_songs[11], 
                                    formatted_songs[12], formatted_songs[13], formatted_songs[14], formatted_songs[15], 
                                    formatted_songs[16], formatted_songs[17], formatted_songs[18], formatted_songs[19], 
                                    formatted_songs[20], formatted_songs[21], formatted_songs[22], formatted_songs[23],
                                    formatted_songs[24], formatted_songs[25], formatted_songs[26], formatted_songs[27],
                                    formatted_songs[28], formatted_songs[29], formatted_songs[30])
                        songs.append(song)
                    # Else create a song with 30, set location as optional arg
                    else:
                        song = Song(formatted_songs[0], formatted_songs[1], formatted_songs[2], formatted_songs[3], 
                                    formatted_songs[4], formatted_songs[5], formatted_songs[6], formatted_songs[7], 
                                    formatted_songs[8], formatted_songs[9], formatted_songs[10], formatted_songs[11], 
                                    formatted_songs[12], formatted_songs[13], formatted_songs[14], formatted_songs[15], 
                                    formatted_songs[16], formatted_songs[17], formatted_songs[18], formatted_songs[19], 
                                    formatted_songs[20], formatted_songs[21], formatted_songs[22], formatted_songs[23],
                                    formatted_songs[24], formatted_songs[25], formatted_songs[26], formatted_songs[27],
                                    formatted_songs[28], formatted_songs[29])
                        songs.append(song)
                return songs
        except IOError:
            print(self.__display_error_msg())
            return []
        except Exception as ex:
            print(ex)
            quit()

    def __get_distinct_sorted_years(self):
        # Add years to set to prevent duplicates
        year_set = set()
        for song in self.__songs:
            if (song.get_year() != "" and song.get_year() > 1000):
                year = song.get_year()
                year_set.add(year)
        # Add set to list and sort
        years = list(year_set)
        years.sort()
        return years

    def __get_distinct_sorted_genres(self):
        # Add genres to set to prevent duplicates
        genre_set = set()
        for song in self.__songs:
            if (song.get_genre() != ""):
                genre = song.get_genre()
                genre_set.add(genre)
        # Add set to list and sort
        genres = list(genre_set)
        genres.sort()
        return genres

    def __get_number_of_songs_released_by_year(self):
        # Get distinct sorted list of years
        years = self.__get_distinct_sorted_years()
        # Add year and number of songs for that year to dictionary
        # and return the dictionary object to caller
        song_release = {}
        for year in years:
            for song in self.__songs:
                if (song.get_year() == year):
                    if (year in song_release):
                        song_release[year] += 1
                    else:
                        song_release[year] = 1
        return song_release

    def __get_songs_in_genre(self):
        # Get distinct sorted list of genres
        genres = self.__get_distinct_sorted_genres()
        # Add genre and list of songs for that genre to dictionary
        # and return the dictionary object to caller
        genre_dict = {}
        for genre in genres:
            song_list = []
            for song in self.__songs:
                if (song.get_genre() == genre):
                    song_list.append(song)
            genre_dict.update({genre: song_list})
        return genre_dict

    def __get_longest_songs_from_list(self, songs: list):
        longest_songs = []
        maximum = 1
        for song in songs:
            if (song.get_time() != ""):
                song_time = song.get_time()
                if (song_time > maximum):
                    maximum = song_time
        for song in songs:
            if (song.get_time() == maximum):
                longest_songs.append(song)
        return longest_songs

    def __get_shortest_songs_from_list(self, songs: list):
        shortest_songs = []
        minimum = 1000000
        for song in songs:
            if (song.get_time() != ""):
                song_time = song.get_time()
                if (song_time < minimum):
                    minimum = song_time
        for song in songs:
            if (song.get_time() == minimum):
                shortest_songs.append(song)
        return shortest_songs

    def __add_number_of_songs_released_by_year(self):
        result = ""
        result += "\nNumber of Songs by Year:"
        songs_released = self.__get_number_of_songs_released_by_year()
        for key, value in songs_released.items():
            result += f"\n  {key} - {value} songs"
        return result

    def __add_longest_songs_in_playlist(self):
        result = ""
        result += "\n\nLongest Song(s) in Playlist:"
        longest_songs_from_list = self.__get_longest_songs_from_list(self.__songs)
        for song in longest_songs_from_list:
            result += f"\n  {song.get_time_str()}"
        return result

    def __add_shortest_songs_in_playlist(self):
        result = ""
        result += "\n\nShortest Song(s) in Playlist:"
        shortest_songs_from_list = self.__get_shortest_songs_from_list(self.__songs)
        for song in shortest_songs_from_list:
            result += f"\n  {song.get_time_str()}"
        return result

    def __add_songs_breakout_by_genre(self):
        result = ""
        result += "\n\nSongs by Genre:"
        genre_count = self.__get_songs_in_genre()
        for key, value in genre_count.items():
            result += f"\n\n  {key} - {len(value)} songs"
            result += "\n    Longest Song(s) in Genre:"
            longest_songs_from_genre = self.__get_longest_songs_from_list(value)
            for song in longest_songs_from_genre:
                result += f"\n      {song.get_time_str()}"
            result += "\n    Shortest Song(s) in Genre:"
            shortest_songs_from_genre = self.__get_shortest_songs_from_list(value)
            for song in shortest_songs_from_genre:
                result += f"\n      {song.get_time_str()}"
        return result

    def __add_number_of_songs_played(self):
        result = ""
        songs_played = 0
        for song in self.__songs:
            if (song.has_played()):
                songs_played += 1
        result += f"\n\nThe number of songs that have been played: {songs_played}"
        return result

    def __add_number_of_songs_not_played(self):
        result = ""
        songs_not_played = 0
        for song in self.__songs:
            if (not song.has_played()):
                songs_not_played += 1
        result = f"\nThe number of songs that have not been played: {songs_not_played}\n"
        return result

    def __generate_playlist_report(self):
        report_text = ""
        if (len(self.__songs) > 0):
            file_name_array = self.__file_name.split(".")
            report_text = f"{file_name_array[0]} Playlist Report:\n"
            # Get the total number of songs in the playlist
            report_text += f"\nTotal Number of Songs in Playlist: {len(self.__songs)}\n"

            # Get the number of songs released by year in the playlist
            report_text += self.__add_number_of_songs_released_by_year()

            # Get song Name & Artist of longest song or songs
            report_text += self.__add_longest_songs_in_playlist()

            # Get song Name & Artist of shortest song or songs
            report_text += self.__add_shortest_songs_in_playlist()

            # For each Genre, get number of songs, song Name & Artist of longest and shortest song or songs
            report_text += self.__add_songs_breakout_by_genre()

            # Get song count that have and have not been played
            report_text += self.__add_number_of_songs_played()
            report_text += self.__add_number_of_songs_not_played()

        return report_text

    def create_report(self):
        if (len(self.__songs) > 0):
            file_name_array = self.__file_name.split(".")
            report_file_name = f"{file_name_array[0]}_Report_{datetime.date.today()}.{file_name_array[1]}"
            try:
                with open(report_file_name, "w") as report_file:
                    report_file.write(self.__generate_playlist_report())
                print(f"\nA report named \"{report_file_name}\" was created and placed in the same directory as this program.")
            except IOError:
                print(f"\nThere was an issue writing the report ({report_file_name}). Please try again. If the issue persists, contact an administrator.\n")