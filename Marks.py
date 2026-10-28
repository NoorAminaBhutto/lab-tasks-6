marks = {
    'Ali': 85,
    'Sara': 95,
    'Ahmed': 95,
    'Noor': 78
}
highest = max(marks.values())
for name in marks:
    if marks[name] == highest:
        print(name, ":", marks[name])