for number in range(1,10):
    print(number, end= "|")
    for numb in range(1,10):
        multiply = number * numb
        print(f"{multiply:>2} ",  end = " ")
    print()

