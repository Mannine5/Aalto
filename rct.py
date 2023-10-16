import math

def calculate_avg(file, filename):
    error_count = 0
    file_total = 0
    count = 0

    for line in file:
        try:
            line = line.rstrip()
            line = line.split(",")
            file_total += int(line[1])
            count += 1
        except ValueError:
            print(f"Warning: Could not parse line '{line[0]},{line[1]}' in file '{filename}'. Skipping line.")
            error_count += 1
    if error_count == 0:
        print(f"Error: No valid data in file '{filename}'. Please check the file and try again.")

    avg = file_total / (count - error_count)

    return avg, count, error_count


def test(file1_avg, file2_avg):
    variance =
    t_result = (file1_avg - file2_avg) /




def main():
    filename1 = input("Please enter the name of the first file:\n")
    filename2 = input("Please enter the name of the second file:\n")


    try:
        file1 = open(filename1, "r")
        file2 = open(filename2, "r")
        file1_avg, count1, file1_error_count = calculate_avg(file1, filename1)
        file2_avg, count2, file2_error_count = calculate_avg(file2, filename2)

        #print(file1_avg, file1_error_count)
        #print(file2_avg, file2_error_count)

    except OSError:
        print(f"Error: Could not open file '{filename1}'. Please check the filename and try again.")

    if file1_error_count or file2_error_count == 0:
        print("Sufficient data was not found. Terminating program.")
    else:
        test_result = test(file1_avg, file2_avg, count1, count2)

main()
