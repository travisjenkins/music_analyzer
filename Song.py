class Song:
    # 31 headers in both files, but both playlists have 30 in song 
    # lines except for the last few in the Music.txt playlist that actually have 31
    def __init__(self, name: str, artist: str, composer: str, album: str, grouping: str, work: str, movement_number: int, movement_count: int, movement_name: str, genre: str, size: int, time: int, disc_number: int, disc_count: int, track_number: int, track_count: int, year: int, date_modified: str, date_added: str, bit_rate: int, sample_rate: int, volume_adjustment: str, kind: str, equalizer: str, comments: str, plays: int, last_played: str, skips: int, last_skipped: str, my_rating: str, location: str = "") -> None:
        self.__name = name
        self.__artist = artist
        self.__composer = composer
        self.__album = album
        self.__grouping = grouping
        self.__work = work
        self.__movement_number = movement_number
        self.__movement_count = movement_count
        self.__movement_name = movement_name
        self.__genre = genre
        self.__size = size
        self.__time = time
        self.__disc_number = disc_number
        self.__disc_count = disc_count
        self.__track_number = track_number
        self.__track_count = track_count
        self.__year = year
        self.__date_modified = date_modified
        self.__date_added = date_added
        self.__bit_rate = bit_rate
        self.__sample_rate = sample_rate
        self.__volume_adjustment = volume_adjustment
        self.__kind = kind
        self.__equalizer = equalizer
        self.__comments = comments
        self.__plays = plays
        self.__last_played = last_played
        self.__skips = skips
        self.__last_skipped = last_skipped
        self.__my_rating = my_rating
        self.__location = location

    def has_played(self):
        if (self.__plays != ""):
            if (self.__plays >= 1):
                return True
        return False

    def get_year(self):
        return self.__year

    def get_time(self):
        return self.__time

    def get_time_str(self):
        return f"Time: {self.__time}, Name: {self.__name}, Artist: {self.__artist}"

    def get_genre(self):
        return self.__genre