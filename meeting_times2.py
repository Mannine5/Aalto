def meeting_days(name_list, filename):
    days_list = []
    meeting_data = {}

    for line in name_list:
        for x in range(1, len(line)):
            days_list.append(line[x])

    try:
        if filename != "":
            file = open(f"{filename}", "w")
        else:
            print(f"Error in writing to file '{filename}'. Closing program.")
            return

        for x in range(len(days_list) - 1):
            count = 1
            day = days_list[x]
            for y in range(x + 1, len(days_list)):
                test = days_list[y]
                if day not in meeting_data and day == test:
                    count += 1
            if day not in meeting_data:
                meeting_data[day] = count

        for day in meeting_data:
            file.write(f"{day} - {meeting_data[day]} people\n")
        file.close()
        print(f"Meeting information written in the file {filename}.")

    except OSError:
        print(f"Error in writing to file '{filename}'. Closing program.")


def main():

    name_list = []

    name = input("Enter names with dates and stop with empty line (e.g. 'Maija 21.6. 22.6. 26.6.'):\n")
    while name != "":
        name = name.split(" ")
        name_list.append(name)
        name = input()

    filename = input("Enter the name of the file to be created for your meeting data:\n")

    meeting_days(name_list, filename)


main()