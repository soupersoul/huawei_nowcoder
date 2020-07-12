while True:
    try:
        test_num = int(input().strip())
        next_prime = 2
        result = ""
        while next_prime ** 2 < test_num:
            if test_num % next_prime == 0:
                result += str(next_prime) + " "
                test_num = test_num / next_prime
            else:
                if next_prime == 2:
                    next_prime = 3
                else:
                    next_prime += 2
        result += str(int(test_num)) + " "
        print(result)
    except:
        break