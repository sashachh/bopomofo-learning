#!/usr/bin/env python3
"""
Generate audio files for Bopomofo characters using Google TTS.

Run this script locally to generate audio files:
    pip install gtts
    python generate_audio.py

This will create audio files named after each bopomofo character (e.g., ㄅ.mp3)
in the audio/ directory.
"""

from gtts import gTTS
import os

# Change to audio directory
os.makedirs('audio', exist_ok=True)
os.chdir('audio')

# Bopomofo consonants with their standard Taiwan Mandarin pronunciations
# Each consonant is pronounced with a supporting vowel as taught in schools
consonants = [
    ('ㄅ', 'ㄅㄛ'),   # bo
    ('ㄆ', 'ㄆㄛ'),   # po
    ('ㄇ', 'ㄇㄛ'),   # mo
    ('ㄈ', 'ㄈㄛ'),   # fo
    ('ㄉ', 'ㄉㄜ'),   # de
    ('ㄊ', 'ㄊㄜ'),   # te
    ('ㄋ', 'ㄋㄜ'),   # ne
    ('ㄌ', 'ㄌㄜ'),   # le
    ('ㄍ', 'ㄍㄜ'),   # ge
    ('ㄎ', 'ㄎㄜ'),   # ke
    ('ㄏ', 'ㄏㄜ'),   # he
    ('ㄐ', 'ㄐㄧ'),   # ji
    ('ㄑ', 'ㄑㄧ'),   # qi
    ('ㄒ', 'ㄒㄧ'),   # xi
    ('ㄓ', 'ㄓ'),     # zhi (standalone retroflex)
    ('ㄔ', 'ㄔ'),     # chi
    ('ㄕ', 'ㄕ'),     # shi
    ('ㄖ', 'ㄖ'),     # ri
    ('ㄗ', 'ㄗ'),     # zi (standalone dental sibilant)
    ('ㄘ', 'ㄘ'),     # ci
    ('ㄙ', 'ㄙ'),     # si
]

# Bopomofo vowels with their standard pronunciations
vowels = [
    ('ㄚ', 'ㄚ'),     # a
    ('ㄛ', 'ㄛ'),     # o
    ('ㄜ', 'ㄜ'),     # e
    ('ㄝ', 'ㄧㄝ'),   # ie/ye
    ('ㄞ', 'ㄞ'),     # ai
    ('ㄟ', 'ㄟ'),     # ei
    ('ㄠ', 'ㄠ'),     # ao
    ('ㄡ', 'ㄡ'),     # ou
    ('ㄢ', 'ㄢ'),     # an
    ('ㄣ', 'ㄣ'),     # en
    ('ㄤ', 'ㄤ'),     # ang
    ('ㄥ', 'ㄥ'),     # eng
    ('ㄦ', 'ㄦ'),     # er
    ('ㄧ', 'ㄧ'),     # yi/i
    ('ㄨ', 'ㄨ'),     # wu/u
    ('ㄩ', 'ㄩ'),     # yu/ü
]

# Tone examples using 媽麻馬罵嗎
tones = [
    ('tone1', '媽'),  # 1st tone (high level)
    ('tone2', '麻'),  # 2nd tone (rising)
    ('tone3', '馬'),  # 3rd tone (dipping)
    ('tone4', '罵'),  # 4th tone (falling)
    ('tone5', '嗎'),  # neutral tone
]

def generate_audio(symbol, text, lang='zh-TW'):
    """Generate audio file for a bopomofo symbol."""
    filename = f'{symbol}.mp3'
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        print(f'  Skipping {filename} (already exists)')
        return

    print(f'  Generating {filename} from "{text}"...')
    try:
        tts = gTTS(text=text, lang=lang)
        tts.save(filename)
        print(f'  Created {filename}')
    except Exception as e:
        print(f'  ERROR generating {filename}: {e}')

if __name__ == '__main__':
    print('Generating Bopomofo audio files...\n')

    print('Consonants:')
    for symbol, text in consonants:
        generate_audio(symbol, text)

    print('\nVowels:')
    for symbol, text in vowels:
        generate_audio(symbol, text)

    print('\nTones:')
    for symbol, text in tones:
        generate_audio(symbol, text)

    print('\nDone! Audio files are in the audio/ directory.')
