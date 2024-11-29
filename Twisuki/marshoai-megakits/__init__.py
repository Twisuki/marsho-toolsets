import random

# Twisuki
async def twisuki () :
    return "Twiuski(苏阳)是megakits插件作者, Github : 'https://github.com/Twisuki'"

# Random Turntable
async def random_turntable (upper : int, lower : int = "0") :
    return str(random.randint(lower, upper))

# Number Calc
async def number_calc (a : str, b : str, op : str) :
    a, b = float(a), float(b)
    match op :
        case "+" : return str(a + b)
        case "-" : return str(a - b)
        case "*" : return str(a * b)
        case "/" : return str(a / b)
        case "**" : return str(a ** b)
        case "%" : return str(a % b)
        case _ : return "未知运算符"

# MorseCode
DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    '.': '.-.-.-', ':': '---...', ',': '--..--', ';': '-.-.-.',
    '?': '..--..', '=': '-...-', '\'': '.----.', '/': '-..-.',
    '!': '-.-.--', '-': '-....-', '_': '..--.-', '\"': '.-..-.',
    '(': '-.--.', ')': '-.--.-', '$': '...-..-', '&': '....',
    '@': '.--.-.', ' ': ' '
}

# MorseCode Encrypt
async def morse_encrypt (msg : str) :
    result = ""
    msg = msg.upper()
    for char in msg :
        if char in DICT :
            result += DICT[char]
        else :
            result += '..--..'
        result += ' '

    return result

# MorseCode Decrypt
async def morse_decrypt (msg : str) :
    result = ""

    msg_arr = msg.split()
    for char in msg_arr :
        tmp = [key for key, value in DICT.items() if value == char]
        if not tmp :
            tmp = '?'
        result += tmp

    return result

