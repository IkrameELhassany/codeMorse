import winsound
import time




def morse(string,morse_dictionary):
    string=string.upper()
    morse_code=""
    for letter in string:
       if letter in morse_dictionary.keys():
            morse_code+=(morse_dictionary[letter])
       elif letter==" ":
           morse_code+=(" ")
    return morse_code 
string=input('entrez un texte pour le coder en morse \n')


def play_sound(morse_code):
    dot_duration=200
    dash_duration=3*dot_duration
    symbol_gap=dot_duration
    letter_gap=dash_duration
    morse_sound={
        '.' : dot_duration,
        '-' : dash_duration,
        ' ' : None
    }
    for symbol in morse_code:
        if symbol in morse_sound:
            duration=morse_sound[symbol]
            if duration:
                winsound.Beep(1000,duration)
                time.sleep(duration/1000)
            else:
                time.sleep(letter_gap/1000)
        else:
            time.sleep(symbol_gap/1000)


morse_dictionary={
        'A': '.-', 
        'B': '-...', 
        'C': '-.-.', 
        'D': '-..', 
        'E': '.', 
        'F': '..-.', 
        'G': '--.', 
        'H': '....',
        'I': '..', 
        'J': '.---', 
        'K': '-.-', 
        'L': '.-..', 
        'M': '--', 
        'N': '-.', 
        'O': '---', 
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...', 
        'T': '-', 
        'U': '..-', 
        'V': '...-', 
        'W': '.--', 
        'X': '-..-',
        'Y': '-.--', 
        'Z': '--..',
        '1': '.----',
        '2': '..---', 
        '3': '...--', 
        '4': '....-', 
        '5': '.....', 
        '6': '-....', 
        '7': '--...',
        '8': '---..', 
        '9': '----.', 
        '0': '-----',
        '.': '.-.-.-',
        ',': '--..--',
        '?': '..--..',
        "'": '.----.',
        '!': '-.-.--', 
        '/': '-..-.',
        '(': '-.--.',
        ')': '-.--.-',
        '&': '.-...', 
        ':': '---...', 
        ';': '-.-.-.', 
        '=': '-...-',
        '+': '.-.-.', 
        '-': '-....-',
        '_': '..--.-', 
        '"': '.-..-.', 
        '$': '...-..-',
        '@': '.--.-.',
}
morse_code=morse(string,morse_dictionary)
play_sound(morse_code)