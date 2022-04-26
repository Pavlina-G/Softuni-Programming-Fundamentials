def exam_results():

    exam_data = {}
    submission_data = {}

    while True:
        command = input().split("-")
        if command[0] == 'exam finished':
            break
        elif command[1] == "banned":
            username = command[0]
            for key, value in dict(exam_data).items():
                if username in key:
                    del exam_data[key]
            break

        else:
            username = command[0]
            language = command[1]
            points = int(command[2])

        if (username, language) not in exam_data:
            exam_data[(username, language)] = points
        else:
            if points > exam_data[(username, language)]:
                exam_data[(username, language)] = points

        if language not in submission_data:
            submission_data[language] = 0
        submission_data[language] += 1

    print('Results:')
    for key, value in exam_data.items():
        print(f"{key[0]} | {value}")

    print("Submissions:")
    for key, value in submission_data.items():
        print(f"{key} - {value}")


exam_results()
