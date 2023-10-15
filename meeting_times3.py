def main():

    meeting_data = {}
    name_list = []

    name = input("Enter names with dates and stop with empty line (e.g. 'Maija 21.6. 22.6. 26.6.'):\n")
    while name != "":
        print(name)
        name = name.split(" ")
        meeting_data[name[0]] = name[0]
        for day in range(1, len(name)):
            meeting_data[name[0]].append(name[day])

        name = input()

    print(meeting_data)

    #meeting_days(name_list)


main()