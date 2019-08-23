import matplotlib.pyplot as plt

activites = ['CID-109121','CID-109410','CID-109411','CID-109324']
slices = [3,7,8,6]
colors = ['r','g','m','b']

plt.pie(slices, labels=activites, colors=colors,startangle=90,shadow=True,
       explode=(0.2,0,0,0),autopct='%1.2f%%')

plt.legend()

plt.show()