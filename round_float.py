while True:
    try:
        test_num = input().strip()
        numbers = test_num.split(".")
        numbers[0] = int(numbers[0])
        if int(numbers[1]) >= 5:
            numbers[0] += 1
        print(numbers[0])
    except:
        break