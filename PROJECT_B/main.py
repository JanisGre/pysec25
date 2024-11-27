import matplotlib.pyplot as plt

sizes = [15, 30, 45, 10]
labels = ['18-25 gadi', '25-30 gadi', '30-40 gadi', '40+ gadi']

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
circle = plt.Circle((0, 0), 0.8, color='white')
plt.gca().add_artist(circle) 
plt.title('VA studentu vecums') 
plt.show()