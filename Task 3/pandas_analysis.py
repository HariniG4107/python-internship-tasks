import pandas as pd

# Load CSV file
data = pd.read_csv("student_data.csv")

# Convert Marks to numeric and clean invalid values
data["Marks"] = pd.to_numeric(data["Marks"], errors="coerce")
data = data.dropna()
data["Marks"] = data["Marks"].astype(int)

# Display full dataset
print("\nSTUDENT DATA\n")
print(data)

# Filter students with marks > 80
high_marks = data[data["Marks"] > 80]
print("\nSTUDENTS WITH MARKS ABOVE 80\n")
print(high_marks)

# Average marks by department
avg_marks = data.groupby("Department")["Marks"].mean()
print("\nAVERAGE MARKS BY DEPARTMENT\n")
print(avg_marks)
print("\nFINAL INSIGHTS\n")

# Top performer
top_student = data.loc[data["Marks"].idxmax()]
print(f"1. Top Performer: {top_student['Name']} with {top_student['Marks']} marks")

# Lowest performer
low_student = data.loc[data["Marks"].idxmin()]
print(f"2. Lowest Performer: {low_student['Name']} with {low_student['Marks']} marks")

# Best department
best_dept = avg_marks.idxmax()
print(f"3. Best Performing Department: {best_dept} with average {avg_marks.max():.2f} marks")

# Overall average
print(f"4. Overall Average Marks: {data['Marks'].mean():.2f}")