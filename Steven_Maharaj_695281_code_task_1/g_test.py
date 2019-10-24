from LCG import LCG_alogorithm,prob_of_two_sixs
import matplotlib.pyplot as plt
import seaborn as sns
from time import sleep
sns.set_style("darkgrid")

a,b,m = 858,0,997
x = LCG_alogorithm(a,b,m,seed = 2,iterations=10000)
dice_throws = (x%6)+1

probabilty_of_two_sixs = prob_of_two_sixs(x)

print(x[:100])

print("For 10000 dice rolls")
print(f'The empirical probabilty of rolling two sixs is {probabilty_of_two_sixs}')

# Plots
hist = sns.countplot(x=dice_throws)
plt.xlabel("Dice values")
plt.ylabel("Freqency")
plt.title("Dice throws")
plt.savefig("fig/dice_freqency_bad",dpi=250)
plt.show(hist)

