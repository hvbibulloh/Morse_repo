alph = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', '/': '-..-.',
    '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': ' '
}
invert_alph = {v: k for k, v in alph.items()}


def to_morse_code(english_plain_text):
    morse_code = ""
    for char in english_plain_text:
        if char.upper() in alph:
            morse_code += alph[char.upper()] + " "
        elif char == " ":
            morse_code += "  "
    return morse_code


def to_english_plain_text(morse_code):
    # Adding a space at end to decode the last character
    try:
        morse_code += " "
        english_plain_text = ""
        current_char_morse_code = ""
        for char in morse_code:
            if char != " ":
                # adding morse code char to the current character
                current_char_morse_code += char
            else:
                # adding decoded character to the result
                if current_char_morse_code in invert_alph:
                    english_plain_text += invert_alph[current_char_morse_code]
                    current_char_morse_code = ""
                elif current_char_morse_code == "":
                    english_plain_text += " "
        return english_plain_text
    except:
        return False
