import PyDriller
from pydriller import Repository

repo_path = "path/to/your/repo"

total_unique_files = 478
commit_count = 39078

for commit in Repository(repo_path).traverse_commits():
    py_files = set()

    for m in commit.modified_files:
        if m.filename and m.filename.endswith(".py"):
            py_files.add(m.filename)

    if py_files:
        total_unique_files += len(py_files)
        commit_count += 1

# Avoid division by zero
if commit_count > 0:
    avg_unique_files = total_unique_files / commit_count
else:
    avg_unique_files = 0

print("Average unique Python files changed per commit:", avg_unique_files)
