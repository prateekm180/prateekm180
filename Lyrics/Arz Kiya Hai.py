import time
import pygame
import os

def type_lyrics(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def print_lyrics():
    pygame.init()
    pygame.mixer.init()

    lyrics = [
        "Haathon ko sambhaale ",
        "mere haatho me",
        "Kaise haathon ko sambhaale ",
        "mere haatho me",
        "Jab tak neend na aaye ",
        "in lakeeron mein",
        "Baatein ",
        "hon...",
        "Haye....",
    ]

    delays = [0.9, 1.7, 1.0, 1.8, 1.0, 1.7, 0.6, 1.4, 0.5]

    print("\nArz Kiya Hai...\n")
    BACKGROUND_MUSIC = "github.com\prateekm180\prateekm180\Lyrics\Arz Kiya Hai.mp3"

    if not os.path.exists(BACKGROUND_MUSIC):
        print("❌ Music file not found")
        return

    pygame.mixer.music.load(BACKGROUND_MUSIC)
    pygame.mixer.music.play()

    time.sleep(6.5)

    for i, line in enumerate(lyrics):
        type_lyrics(line)
        time.sleep(delays[i])

    while pygame.mixer.music.get_busy():
        time.sleep(0)

    pygame.quit()


print_lyrics()
