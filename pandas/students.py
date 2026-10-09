import pandas as po
df_students = po.read_csv("students.csv")

print("First 5 rows: ")
print(df_students.head())

rows, cols = df_students.shape
print(f"\nRows: {rows}, Columns: {cols}")

name_gpa = df_students[["name","GPA"]]
print("\nName and gpa:")
print(name_gpa.head())

high_gpa_students = df_students[df_students["GPA"] >= 3.5]
print("\nStudent with gpa > =3.5:")
print(high_gpa_students)

sorted_students = df_students.sort_values(by = "GPA" , ascending = False)
print("\nStudents sorted by gpa (descending):")
print(sorted_students.head())

avg_gpa_by_major = df_students.groupby('major')["GPA"].mean()
print("\nAvg gpa by major:")
print(avg_gpa_by_major)