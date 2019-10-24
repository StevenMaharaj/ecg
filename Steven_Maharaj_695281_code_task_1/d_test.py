from LCG import LCG_alogorithm, check_valid

b,m = 0,997
count = 0
for a in range(1,m):
    x = LCG_alogorithm(a,b,m,seed = 2,iterations=2000)
    if check_valid(x,m):
        count += 1

print(f"There are {count} vaild")