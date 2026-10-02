lookup_table = [
    ("A", 0),
    ("B", 1),
    ("C", 2),
    ("D", 3),
    ("E", 4),
    ("F", 5),
    ("G", 6),
    ("H", 7),
    ("I", 8),
    ("J", 9),
    ("K", 10),
    ("L", 11),
    ("M", 12),
    ("N", 13),
    ("O", 14),
    ("P", 15),
    ("Q", 16),
    ("R", 17),
    ("S", 18),
    ("T", 19),
    ("U", 20),
    ("V", 21),
    ("W", 22),
    ("X", 23),
    ("Y", 24),
    ("Z", 25)
]

def encryption():
    temp = input("Enter the plaintext: ")
    plaintext = temp.upper()
    key = int(input("Enter the key: "))

    ciphertext = ""

    for char in plaintext:
        for a, b in lookup_table:
            if char == a:
                index = (b + key) % 26
                ciphertext += lookup_table[index][0]
                break

    print(f"\nCiphertext: {ciphertext}")

def decryption():
    temp = input("Enter the plaintext: ")
    ciphertext = temp.upper()
    key = int(input("Enter the key: "))
    
    plaintext = ""

    for char in ciphertext:
        for a,b in lookup_table:
            if char == a:
                index = (b-key) % 26
                plaintext += lookup_table[index][0]
                break

    print(f"\nCiphertext: {plaintext}")

encryption()
decryption()