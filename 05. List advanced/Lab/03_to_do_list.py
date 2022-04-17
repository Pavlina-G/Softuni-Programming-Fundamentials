command = input()
notes = [0] * 10

while command != "End":
    note_split = command.split("-")
    priority = int(note_split[0]) - 1
    task = note_split[1]
    notes[priority] = task

    command = input()

result = [task for task in notes if task != 0]
print(result)