
import csv
filename = 'D:/Desktop/4.29newdata/NI_new/2060-30ms-4096-128.csv'
f = open("D:/Desktop/4.29newdata/NI_new/2060-30ms-4096-128-arduino.csv", "w", encoding="utf-8", newline="")
csv_writer = csv.writer(f)
csv_writer.writerow([8920])
count = 0
with open(filename, 'r', encoding='utf-8') as file_to_read:
    while True:
        lines = file_to_read.readline()  # read line
        if not lines:
            break
        if count >= 5:
            p_tmp, volte = [float(i) for i in lines.split(',')]
            if p_tmp >= count * 1.0 / 8920:
                csv_writer.writerow([volte])
                count = count + 1
        else:
            count = count + 1
        # if count >= 3200004:
        #     break
