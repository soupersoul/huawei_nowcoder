seq = input().lower()
char_in = input()[0].lower()
print(len(seq) - len(seq.replace(char_in, "")))