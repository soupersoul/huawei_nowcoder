line1=input().strip()
line2=input().strip()
def format_line(line):
    length = len(line)
    if length == 0:
        return
    if length <= 8:
        print(line.ljust(8, '0'))
    else:
        print(line[:8])
        format_line(line[8:])
format_line(line1)
format_line(line2)