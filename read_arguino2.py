import matplotlib.pyplot as plt
filename = './data/arduino.txt'
voltes = []
count = 0
with open(filename, 'r', encoding='utf-8') as file_to_read:
    while True:
        count = count + 1
        lines = file_to_read.read()
        if not lines:
            break
        if count >= 0:
            volt = lines[16:22]
            volt = float(volt)
            voltes.append(volt)
        if count >= 3200004:
            break

plt.plot(voltes)
plt.ylim([2, 3.2])
plt.show()