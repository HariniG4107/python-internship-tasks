import os
import shutil

# 1. Write to file
with open("sample.txt", "w") as file:
    file.write("Hello, this is a sample file.\n")
    file.write("Python File Handling Task.\n")

print("File written successfully.")

# 2. Read file
with open("sample.txt", "r") as file:
    content = file.read()

print("\nFile Content:")
print(content)

# 3. Append to file
with open("sample.txt", "a") as file:
    file.write("This line is appended.\n")

print("Data appended successfully.")

# 4. Rename file (FIX)
if os.path.exists("renamed.txt"):
    os.remove("renamed.txt")

os.rename("sample.txt", "renamed.txt")
print("File renamed successfully.")

# 5. Copy file
shutil.copy("renamed.txt", "copy.txt")
print("File copied successfully.")