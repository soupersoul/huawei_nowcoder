def reverse(s):
    new_s = ""
    for c in s:
        if c.isalpha():
            new_s += c
        else:
            new_s += " "
    words = new_s.split()
    rs_words = words[::-1]
    return " ".join(rs_words)

print(reverse('I am a student'))
