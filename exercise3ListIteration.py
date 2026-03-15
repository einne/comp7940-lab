l = [52633, 8137, 1024, 7919]
for num in l:
    print("Factors of", num, ":")
    for i in range(2, num):
        if num % i == 0:
            print(i)

            