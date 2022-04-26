

def exam_results():
    command = input()
    exam_details = {}
    language_details = {}
    submission = 1
    banned_submission = 0

    while command != 'exam finished':
        if "banned" not in command:

            info = command.split("-")
            username = info[0]
            language = info[1]
            points = int(info[2])

            if username not in exam_details:
                exam_details[username] = {'language': [language], 'points': [points], 'submissions': [1]}
            else:
                if language in exam_details[username]['language']:
                    exam_details[username]['submissions'].append(1)
                    if points > exam_details[username]['points']:
                        exam_details[username]['points'] = points
                else:
                    exam_details[username]['language'].append(language)
                    exam_details[username]['points'].append(points)
                    exam_details[username]['submissions'].append(1)

        else:
            ban_info = command.split("-")
            username = ban_info[0]
            banned_submission = exam_details.pop(username)
            print(banned_submission)
            # print(exam_details)

        command = input()

    print(f"Results:")
    print(exam_details.items())
    for name, b in exam_details.items():
        for c, point in b.items:
            if c == 'points':
                print(f"{name} | {sum(point)}")


        # for language,nested_points in points.items():
        #     for point in nested_points:
        #         print(point)
        #         print(f"{name} | {sum(point)}")
    print("Submissions:")

exam_results()