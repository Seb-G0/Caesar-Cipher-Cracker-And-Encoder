ALPHA, alpha, numer = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz", "0123456789"
mode = input("Enter a mode (encode or decode): ")
while mode != "encode" and mode != "decode": mode = input("Mode not recognized: enter 'encode' or 'decode': ")
inp = input("Enter your message to be encoded or enter a file name ending with .txt: ")
if inp[-4:] == ".txt":
    try:
        inp = open(inp).read().splitlines()
    except:
        print("Text file not found")
        exit()
key = input("Enter your shift key: ")
while not(key.isnumeric()): key = input("Enter your shift key as a number: ")
key = int(key)
if mode == "decode":
    key *= -1
String = ""
for char in inp:
    if char.isalnum():
        if char.isnumeric():
            char = numer[(numer.index(char) + key) % 10]
        elif char.isupper():
            char = ALPHA[(ALPHA.index(char) + key) % 26]
        else:
            char = alpha[(alpha.index(char) + key) % 26]
    String += char
print(String)