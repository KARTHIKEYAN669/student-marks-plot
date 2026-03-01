import matplotlib.pyplot as plt
subjects = ["Math", "Science", "English", "Computer"]
student_A = [78, 85, 90, 88]
student_B = [70, 80, 75, 82]
student_C = [88, 92, 85, 91]
plt.figure(figsize=(8,5))
plt.plot(subjects, student_A, marker='o', linestyle='--', label="Student A")
plt.plot(subjects, student_B, marker='o', color='red', label="Student B")
plt.plot(subjects, student_C, marker='o', label="Student C")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student Marks Comparison")
plt.legend()
plt.grid(True)
plt.show()