from LCG import LCG_alogorithm, check_valid

b,m = 0,7
for a in range(1,m):
    x = LCG_alogorithm(a,b,m,seed = 2,iterations=20)
    if check_valid(x,m):
        print(f"a = {a} is valid")


