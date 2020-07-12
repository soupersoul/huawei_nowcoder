in20 = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','forteen','fifteen','sixteen','seventeen','eighteen','nineteen']
tens = ['','','twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

def en100(num):
    re = ''
    i = num // 100
    if i > 0:
        re = in20[i] + ' hundred '
    num = num%100
    if i > 0 and num > 0:
        re += 'and '
    if num >= 20:
        re  += tens[num // 10] + ' ' + in20[num%10]
    else:
        re += in20[num]
    return re.strip()
 
def to_en(num):
    re = ''
    i = num // 1000000000
    if i > 0:
        re = en100(i) + ' billion '
    num = num%1000000000
    i = num // 1000000
    if i > 0:
        re += en100(i) + ' million '
    num = num%1000000
    i = num // 1000
    if i > 0:
        re += en100(i) + ' thousand '
    num = num%1000
    re += en100(num)
    return re.strip()

print(to_en(483222))
print(to_en(1762932))
