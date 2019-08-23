import matplotlib.pyplot as plt

ages = [2,50,70,40,30,45,50,45,43,40,44,60,
       7,13,51,18,90,77,32,21,20,40]

range = (0,100)
bins = 10

plt.hist(ages,bins,range,color='green',histtype='bar',rwidth=0.7)

plt.xlabel('Ages')
plt.ylabel('Bins')

plt.title('CID1098981')

plt.show()