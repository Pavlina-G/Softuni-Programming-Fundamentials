def company_id():
    command = input()
    company_dict = {}

    while command != "End":
        command = command.split(" -> ")
        company = command[0]
        employee_id = command[1]

        if company not in company_dict:
            company_dict[company] = [employee_id]
        else:
            if employee_id not in company_dict[company]:
                company_dict[company] += [employee_id]

        command = input()

    for company, values in company_dict.items():
        print(f"{company}")
        for id in values:
            print(f"-- {id}")


company_id()
