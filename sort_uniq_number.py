while True:
	try:
	    num_size = int(input())
	    numbers = set()
	    for i in range(num_size):
	        numbers.add(int(input()))
	    numbers = sorted(numbers)
	    for num in numbers:
	        print(num)
	except:
		break
