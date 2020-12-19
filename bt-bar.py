import matplotlib.pyplot as plt
color_names = ['Ngân', 'Quỳnh', 'Hưng', 'Thi', 'Long']
colors = ['#3498db', '#fd79a8', '#f1c40f', '#273c75', '#e74c3c']
num_favorite = [7,5,10,9,6]
xs = [i + 0.03 for i, _ in enumerate(color_names)]
plt.bar(xs, num_favorite, color=colors)
plt.title('Học sinh lớp 9')
plt.xticks([i+0.1 for i, _ in enumerate(color_names)], color_names)
plt.xlabel('Tên học sinh')
plt.ylabel('Điểm')
plt.show()
