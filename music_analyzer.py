from Playlist import Playlist

def ask_user_to_continue():
    user_continue = input("\nWould you like to analyze another music playlist? (y/n) ").lower()
    if (user_continue != "y"):
        return False
    else:
        return True

def main():
    print("\nWelcome to the Music Playlist Analyzer")
    continue_running = True

    while (continue_running):
        # Get file name from user
        file_name = input("\nPlease enter the playlist name:  ")
        
        # Create a playlist and analyze it
        playlist = Playlist(file_name)
        playlist.create_report()

        # Ask user to continue
        continue_running = ask_user_to_continue()

main()