#!/usr/bin/env python3
"""
Download official Taiwan MOE bopomofo pronunciation files from GCIN voice data.

Run this script locally:
    python download_moe_audio.py

This will download official pronunciation audio to the audio/ folder.
"""

import os
import urllib.request
import urllib.parse

os.makedirs('audio', exist_ok=True)

GCIN_BASE = 'https://audreyt.github.io/gcin-voice-data/mp3'

# Bopomofo mappings: (output_filename, gcin_folder)
# GCIN format: unmarked folder = tone 1, numbered = tones 2-4
# Files are named 3.mp3 inside each folder

consonants = [
    ('ㄅ', 'ㄅㄛ'),      # bo (tone 1 - unmarked)
    ('ㄆ', 'ㄆㄛ'),      # po
    ('ㄇ', 'ㄇㄛ'),      # mo
    ('ㄈ', 'ㄈㄛ2'),     # fo (tone 2)
    ('ㄉ', 'ㄉㄜ2'),     # de (tone 2)
    ('ㄊ', 'ㄊㄜ4'),     # te (tone 4)
    ('ㄋ', 'ㄋㄜ4'),     # ne (tone 4)
    ('ㄌ', 'ㄌㄜ4'),     # le (tone 4)
    ('ㄍ', 'ㄍㄜ'),      # ge
    ('ㄎ', 'ㄎㄜ4'),     # ke (tone 4)
    ('ㄏ', 'ㄏㄜ4'),     # he (tone 4)
    ('ㄐ', 'ㄐㄧ'),      # ji
    ('ㄑ', 'ㄑㄧ'),      # qi
    ('ㄒ', 'ㄒㄧ'),      # xi
    ('ㄓ', 'ㄓ'),        # zhi
    ('ㄔ', 'ㄔ'),        # chi
    ('ㄕ', 'ㄕ'),        # shi
    ('ㄖ', 'ㄖ4'),       # ri (tone 4)
    ('ㄗ', 'ㄗ'),        # zi
    ('ㄘ', 'ㄘ'),        # ci
    ('ㄙ', 'ㄙ'),        # si
]

vowels = [
    ('ㄚ', 'ㄚ'),        # a
    ('ㄛ', 'ㄛ'),        # o
    ('ㄜ', 'ㄜ4'),       # e (tone 4)
    ('ㄝ', 'ㄧㄝ'),      # ie/ye
    ('ㄞ', 'ㄞ'),        # ai
    ('ㄟ', 'ㄟ'),        # ei
    ('ㄠ', 'ㄠ'),        # ao
    ('ㄡ', 'ㄡ3'),       # ou (tone 3)
    ('ㄢ', 'ㄢ'),        # an
    ('ㄣ', 'ㄣ'),        # en
    ('ㄤ', 'ㄤ'),        # ang
    ('ㄥ', 'ㄥ'),        # eng
    ('ㄦ', 'ㄦ2'),       # er (tone 2) - may not exist
    ('ㄧ', 'ㄧ'),        # yi
    ('ㄨ', 'ㄨ'),        # wu
    ('ㄩ', 'ㄩ'),        # yu
]

tones = [
    ('tone1', 'ㄇㄚ'),   # ma tone 1 (unmarked)
    ('tone2', 'ㄇㄚ2'),  # ma tone 2
    ('tone3', 'ㄇㄚ3'),  # ma tone 3
    ('tone4', 'ㄇㄚ4'),  # ma tone 4
    ('tone5', 'ㄇㄚ'),   # neutral (use tone 1)
]

def download_audio(output_name, gcin_folder):
    """Download audio file from GCIN."""
    output_path = f'audio/{output_name}.mp3'

    if os.path.exists(output_path) and os.path.getsize(output_path) > 1000:
        print(f'  Skipping {output_name} (already exists)')
        return True

    url = f'{GCIN_BASE}/{urllib.parse.quote(gcin_folder)}/3.mp3'
    print(f'  Downloading {output_name} from {gcin_folder}...')

    try:
        urllib.request.urlretrieve(url, output_path)
        if os.path.getsize(output_path) > 1000:
            print(f'    ✓ Saved {output_name}.mp3')
            return True
        else:
            os.remove(output_path)
            print(f'    ✗ File too small, removed')
            return False
    except Exception as e:
        print(f'    ✗ Error: {e}')
        if os.path.exists(output_path):
            os.remove(output_path)
        return False

if __name__ == '__main__':
    print('Downloading official Taiwan MOE bopomofo audio from GCIN...\n')

    print('Consonants:')
    for name, folder in consonants:
        download_audio(name, folder)

    print('\nVowels:')
    for name, folder in vowels:
        download_audio(name, folder)

    print('\nTones:')
    for name, folder in tones:
        download_audio(name, folder)

    print('\nDone! Now update index.html and bopomofo-practice.html to use')
    print('the bopomofo character names (ㄅ.mp3) instead of Chinese characters.')
