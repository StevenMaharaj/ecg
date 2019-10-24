from LCG import LCG_alogorithm

a,b,m = 825,0,997
x = LCG_alogorithm(a,b,m,seed = 2,iterations=50)
dice_throws = (x%6)+1
print(dice_throws)