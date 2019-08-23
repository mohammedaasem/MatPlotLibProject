import matplotlib.pyplot as plt

y = [30, 32, 33, 23, 30, 41, 37, 35, 32, 33, 37, 35]
print(len(y))
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(len(x))
tick_labels = ['JULY-18', 'AUG', 'SEPT', 'OCT', 'NOV', 'DEC-18', 'JAN-19', 'FEB', 'MAR', 'APR', 'MAY', 'JUNE']
print(len(tick_labels))

plt.bar(x,y,width=0.7,color=['b'])
plt.xticks(x,tick_labels)
plt.xlabel("Count")
plt.ylabel("Month(2018-2019)")
plt.title("Data-CID1207192122")
plt.show()
