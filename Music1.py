import os
from pygame import mixer

# Initialize mixer
mixer.init()

# Function to get music folder path
def get_music_folder():
    """Prompts user to select a folder containing music files"""
    folder_path = os.path.abspath(os.path.expanduser(input("Enter path to music folder: ")))
    if not os.path.isdir(folder_path):
        print("Invalid path. Please enter a valid folder path.")
        return get_music_folder()  # Recursively call if path is invalid
    return folder_path

# Function to load songs from a folder
def load_songs(folder_path):
    """Loads all song paths with supported extensions from a folder"""
    songs = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".mp3") or filename.endswith(".wav"):  # Add supported extensions
            song_path = os.path.join(folder_path, filename)
            songs.append(song_path)
    return songs

# Function to play a song
def play_song(song_path):
    """Loads and plays a song using pygame mixer"""
    mixer.music.load(song_path)
    mixer.music.play()

# Function to stop playing
def stop_song():
    """Stops playback using pygame mixer"""
    mixer.music.stop()

# Function to pause/unpause playback (toggles)
def pause_song():
    """Pauses or unpauses playback using pygame mixer"""
    if mixer.music.get_busy():
        mixer.music.pause()
    else:
        mixer.music.unpause()

# Main program loop
playing = False  # Flag to track playback state
current_song_index = -1  # Index of currently playing song

while True:
    # Get user input
    user_input = input("Enter command (play, stop, pause, select, quit): ").lower()

    # Handle user commands
    if user_input == "select":
        music_folder = get_music_folder()
        songs = load_songs(music_folder)
        current_song_index = 0
    elif user_input == "play":
        if not songs:
            print("No songs loaded. Please select a folder first.")
            continue
        if not playing:
            playing = True
            play_song(songs[current_song_index])
    elif user_input == "stop":
        playing = False
        stop_song()
    elif user_input == "pause":
        if playing:
            pause_song()
    elif user_input == "quit":
        stop_song()  # Ensure playback stops before exiting
        mixer.quit()
        break  # Exit the loop
    else:
        print("Invalid command. Please enter play, stop, pause, select, or quit.")
