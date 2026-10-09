import pandas as po 

df_students = po.read_csv('students.csv')
df_scores = po.read_csv('scores.csv')

print("Missing values in student.csv:")
print(df_students.isnull().sum())
print("\nMissing values in scores.csv:")
print(df_scores.isnull().sum())

df_students.fillna(df_students.mean(numeric_only = True), inplace=True)
df_scores.fillna(df_scores.mean(numeric_only = True), inplace=True)

df_merged = po.merge(df_students, df_scores, on = 'student_id')

score_columns = ['python', 'math', 'database']
df_merged['avg_score'] = df_merged[score_columns].mean(axis=1)

top_5_students = df_merged.sort_values(by = 'avg_score', ascending = False).head(5)
print("\nTop 5 students with the highest average score:")
print(top_5_students[['name', 'avg_score']])

avg_score_by_major = df_merged.groupby('major')['avg_score'].mean()
print("\navg score by major:")
print(avg_score_by_major)