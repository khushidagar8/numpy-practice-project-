import numpy as np

subjects = ["Maths", "Python", "AI"]

marks = np.array([
    [85, 90, 88],
    [72, 80, 75],
    [95, 92, 96],
    [38, 45, 35],
    [66, 70, 68]
])

print("All Students Marks:")
print(marks)

print("\nSubject Average:")
print(np.mean(marks, axis=0))

print("\nStudent Average:")
print(np.mean(marks, axis=1))

print("\nHighest Marks in Each Subject:")
print(np.max(marks, axis=0))

print("\nLowest Marks in Each Subject:")
print(np.min(marks, axis=0))
