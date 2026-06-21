line_count = 0
word_count = 0

with open("poem.txt", "r") as file:
    for line in file:
        line_count += 1
        word_count += len(line.split())

print(f"Lines: {line_count}")
print(f"Words: {word_count}")

summary = f"The poem has {line_count} lines and {word_count} words."

with open("summary.txt", "w") as file:
    file.write(summary)

print("Summary written to summary.txt")
