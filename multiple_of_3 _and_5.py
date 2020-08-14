def multiple_of_3_and_5(n):
    sum = 0
    for i in range(n):
        sum += i if i % 3 == 0 or i % 5 == 0 else 0
    return sum
    raise NotImplementedError()

if __name__ == "__main__":
    n = int(input())
    print(multiple_of_3_and_5(n))