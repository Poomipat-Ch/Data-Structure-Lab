
# def integer_right_triangles(p):
#     res = []
#     for i, j, k in range(p/2):
#         print(i,j,k)
#     raise NotImplementedError()


# if __name__ == "__main__":
#     n = int(input())
#     integer_right_triangles(n)

def integer_right_triangles(p):
    res = []
    for a in range(1, p):
        for b in range(a, p):
            c = p-a-b
            if c<a or c<b:
                break
            if c*c == a*a + b*b:
                res.append((a,b,c))
    return res

print(integer_right_triangles(8400))