"""
Date: 2/10/2025 
This file generates random romaji for learning hiragana and katakana 
"""
import random

vowels = ["a", "i", "u", "e", "o"]
consonants = ["k", "s", "t", "n", "h", "m", "y", "r", "w"]

def generate_romaji():
    if random.random() < 0.025: 
        return "n"
    
    consonant = random.choice(consonants) if random.random() < 0.9 else "" 
    vowel = random.choice(vowels)
    
    if consonant == "y" and vowel in ["i", "e"]: 
        vowel = random.choice(["a", "u", "o"])
    
    if consonant == "w" and vowel in ["i", "u", "e"]: 
        vowel = random.choice(["a", "o"])

    if consonant == "s" and vowel == "i": 
        return "shi"
    elif consonant == "t" and vowel == "i": 
        return "chi"
    elif consonant == "t" and vowel == "u": 
        return "tsu"
    elif consonant == "h" and vowel == "u":
        return "fu"
    
    return consonant + vowel

for _ in range(5):
    print(generate_romaji())
