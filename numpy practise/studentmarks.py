import numpy as np

np.random.seed(42)
marks = np.random.randint(0,101,50)
print(marks)

mean = np.mean(marks)
median = np.median(marks)
std = np.std(marks)

print(mean)
print(median)
print(std)

top5 = np.sort(marks)[-5:][::-1]
print("top 5 student: ",top5)