def meeting_days(name_list):
    days_list = []
    meeting_data = []

    for line in name_list:
        for x in range(1, len(line)):
            days_list.append(line[x])

    for x in range(len(days_list) - 1):
        day = days_list[x]
        for y in range(x +1, len(days_list)):
            if day not in meeting_data:
                if day == days_list[y]:
                    meeting_data.append(day)










    #for x in range(len(days_list) - 1):
        #x = 0
      #  for test in range(x + 1, len(days_list)):
       #     if days_list[x] == days_list[test]:

        #x += 1
    print(days_list)
    print(meeting_data)

def main():

    #meeting_data = {}
    name_list = []

    name = input("Enter names with dates and stop with empty line (e.g. 'Maija 21.6. 22.6. 26.6.'):\n")
    while name != "":
        print(name)
        name = name.split(" ")
        name_list.append(name)
        name = input()

    meeting_days(name_list)


main()