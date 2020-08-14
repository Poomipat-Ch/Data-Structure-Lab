def odd_list(al):
    li = []
    for i in al:
        if i % 2 == 1:
            li.append(i)
    return li


print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)