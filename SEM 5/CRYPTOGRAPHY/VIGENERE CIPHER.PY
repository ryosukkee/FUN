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
    plaintext = input("Enter the plaintext: ").upper()
    rkey = input("Enter the key: ").upper()

    if len(plaintext) != len(rkey):
        return

    key = []

    for i in rkey:
        for a,b in lookup_table:
            if i == a:
                key.append(b)

    ciphertext = ""

    for char in plaintext:
        for a,b in lookup_table:
            if char == a:
                index = (b + key.pop(0)) % 26
                ciphertext += lookup_table[index][0]
                break

    print(f"\nCiphertext: {ciphertext}")

def decryption():
    ciphertext = input("Enter the ciphertext: ").upper()
    rkey = input("Enter the key: ").upper()

    if len(ciphertext) != len(rkey):
        return

    key = []

    for i in rkey:
        for a,b in lookup_table:
            if i == a:
                key.append(b)

    plaintext = ""

    for char in ciphertext:
        for a,b in lookup_table:
            if char == a:
                index = (b - key.pop(0)) % 26
                plaintext += lookup_table[index][0]
                break

    print(f"\nPlaintext: {plaintext}")



encryption()
decryption()