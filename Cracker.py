ALPHA, alpha, numer = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz", "0123456789"
wordDict = open("wordDict.txt").read().splitlines()
commonWords = open("CommonWords.txt").read().splitlines()
encryptedString = input("Enter your encrypted word or sentence: ")

def cipher(key, inp):
    key *= -1
    String = ""
    for char in inp:
        if char.isalnum():
            if char.isnumeric():
                char = numer[(key + numer.index(char)) % 10]
            elif char.isupper():
                char = ALPHA[(key + ALPHA.index(char)) % 26]
            else:
                char = alpha[(key + alpha.index(char)) % 26]
        String += char
    return String
possibilities = []

def value(dString):
    value = 1
    if " " in dString:
        dString = dString.split(" ")
    else:
        dstring = [dString]
    for word in dString:
        if word in wordDict:
            value += 1
        if word in commonWords:
            value *= 10
    return value

for key in range(1, 26):
    decryptedString = cipher(key, encryptedString)
    possibilities.append(
        (value(decryptedString), decryptedString, key)
    )
    
possibilities.sort()
possibilities.reverse()
print("Your cipher is most likely:")
print(possibilities[0][1])
print("The key is", possibilities[0][2])

print()
print("Other possibilities are: ")
for possible in possibilities[1:11]:
    print("answer:", possible[1], "key:", possible[2])
    
