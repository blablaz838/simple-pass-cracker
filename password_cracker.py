import itertools
import time

# -------------- Configuration --------------

# Le mot de passe à trouver
target_password = "salmaguenin250110"

# Si tu connais une partie du mot de passe (ex: "salmaguenin")
known_word_part = "salmaguenin"

# Jeu de caractères à utiliser (minuscules + chiffres uniquement)
chars = "abcdefghijklmnopqrstuvwxyz0123456789"

# -------------- Mode 1: Intelligent Bruteforce --------------

def smart_brute_force(word_part):
    print("\n[+] Starting smart brute-force (word + numbers)...")
    for number in range(0, 1000000):  # de 000000 à 999999
        number_str = f"{number:06d}"  # format 6 chiffres, ex: '000001'
        guess = word_part + number_str
        print(f"Trying: {guess}")
        
        if guess == target_password:
            return guess
    return None

# -------------- Mode 2: Full Bruteforce (lent) --------------

def full_brute_force(chars):
    print("\n[+] Starting full brute-force (all combinations)...")
    length = 1
    while True:
        for attempt in itertools.product(chars, repeat=length):
            guess = ''.join(attempt)
            print(f"Trying: {guess}")

            if guess == target_password:
                return guess
        length += 1

# -------------- Main Program --------------

if __name__ == "__main__":
    print(f"Target password to crack: {target_password}")
    start_time = time.time()

    # 1. Essayer l'attaque intelligente d'abord
    result = smart_brute_force(known_word_part)

    # 2. Si pas trouvé, faire un bruteforce total
    if result is None:
        print("\n[-] Smart attack failed. Starting full
