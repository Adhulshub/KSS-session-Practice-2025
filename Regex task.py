import re

with open("show_version.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Extract Defect IDs (pattern starts with CSC followed by letters/numbers)
defect_pattern = re.compile(r"\b(CSC\w+)\b", re.IGNORECASE)
defect_ids = defect_pattern.findall(content)

# Remove duplicates while keeping order
unique_defect_ids = list(dict.fromkeys(defect_ids))

for defect in unique_defect_ids:
    print(defect)
