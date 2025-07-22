MORSE_CODE = {
    'A': '.-',    'B': '-...',  'C': '-.-.',
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',
    '&': '.-...',  "'": '.----.', '@': '.--.-.',
    ')': '-.--.-', '(': '-.--.',  ':': '---...',
    ',': '--..--', '=': '-...-',  '!': '-.-.--',
    '.': '.-.-.-', '-': '-....-', '+': '.-.-.',
    '"': '.-..-.', '?': '..--..', '/': '-..-.',
    ' ': '/'
}

def encode_to_morse(text):
    morse_text = []
    for char in text.upper():
        if char in MORSE_CODE:
            morse_text.append(MORSE_CODE[char])
        else:

            pass
    return ' '.join(morse_text)

def main():
    user_input = input("Enter text to convert to Morse Code:\n")
    morse_output = encode_to_morse(user_input)
    print("\nMorse Code:")
    print(morse_output)

if __name__ == "__main__":
    main()
