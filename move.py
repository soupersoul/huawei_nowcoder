import re

while True:
    try:
        migrations = input().strip().split(";")
        x = 0
        y = 0
        for m in migrations:
            matchObj = re.match(r'^([ASWD])(\d{1,2})$', m)
            if matchObj:
                direction = matchObj.group(1)
                steps = int(matchObj.group(2))
                if direction == 'A':
                    x -= steps
                elif direction == 'S':
                    y -= steps
                elif direction == 'W':
                    y += steps
                elif direction == 'D':
                    x += steps
        print("{},{}".format(x, y))
    except:
        break