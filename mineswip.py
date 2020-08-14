def num_grid(lst):
    
    for e in range(len(lst)):
        for i in range(len(lst[e])):
            n = 0
            for row in range(e - 1,e + 2):
                for col in range(i - 1, i + 1):
                    if row > -1 and row < 5 and col > -1 and col < 5:
                        n += 1 if lst[row][col] == '#' else 0
                        lst[row][col] = str(n) if lst[row][col] != '#' else '#'
    #print("\n",*lst,sep = "\n")
    return lst



'''lst_input = [

    ["-","-","-","-","-"],

    ["-","-","-","-","-"],

    ["-","-","#","-","-"],

    ["-","-","-","-","-"],

    ["-","-","-","-","-"]

]'''

lst_input = []

input_list = input().split(",")

for e in input_list:

  lst_input.append([i for i in e.split()])

print("\n",*lst_input,sep = "\n")

print("\n",*num_grid(lst_input),sep = "\n")