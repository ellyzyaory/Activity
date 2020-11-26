def info():
    with open("csv_file.csv", 'r') as d:
        data = d.read().split("\n")
    dictionary = {}
    for line in range(0, len(data)):
        temp = data[line].split(',"')
        temp2 = data[line].split(',')
        if line == 0:
            for header in temp:
                dictionary[header.split('"')[1]] = []


        else:
            if len(temp) == 1:
                break
            dictionary['steps'].append(temp2[0].strip('"'))
            dictionary['date'].append(temp2[1].strip('"'))
            dictionary['interval'].append(temp2[2].strip('"'))

    total = {}
    total_key = {}
    mean = {}
    steps_in_day = {}
    interval_in_day = {}
    median = {}
    week = {}
    day = 1

    for count in range(len(dictionary['steps']) - 1):
        date = dictionary['date'][count]
        steps = dictionary['steps'][count]
        interval = dictionary['interval'][count]
        interval_in_day.setdefault(date, [])
        interval_in_day[date].append(interval)
        total.setdefault(date, 0)
        total_key.setdefault(date, 0)
        mean.setdefault(date, 0)
        steps_in_day.setdefault(date, [])
        median.setdefault(date, 0)
        week.setdefault(date, 0)

        if steps == "NA":
            new = steps.replace("NA", "0")
            new = int(new)
            if date == date:
                total[date] += new
                total_key[date] += 1
                mean[date] = total[date] / total_key[date]
                steps_in_day[date].append(new)
                length_s = len(steps_in_day[date])
                length_i = len(interval_in_day[date])
                median_steps = length_s % 2
            if median_steps == 0:
                index = length_i // 2
                median[date] = steps_in_day[date][index]

            else:
                index = length_i // 2
                median[date] = steps_in_day[date][index - 1]

        else:
            steps = int(steps)
            if date == date:
                total[date] += steps
                total_key[date] += 1
                mean[date] = total[date] / total_key[date]
                steps_in_day[date].append(steps)
                length_s = len(steps_in_day[date])
                length_i = len(interval_in_day[date])
                median_steps = length_s % 2
            if median_steps == 0:
                index = length_i // 2
                median[date] = steps_in_day[date][index]

            else:
                index = length_i // 2
                median[date] = steps_in_day[date][index-1]
        if day <= 5:
            week[date] = "Weekday"
            day += 1
        else:
            week[date] = "Weekend"
            day += 1
        if day > 7:
            day = 1

    print("Total number of steps taken per day: ", total)
    print("Mean: ", mean)
    print("Median: ", median)
    print("Weekday or Weekend: ", week)

if __name__ == "__main__":
    info()
