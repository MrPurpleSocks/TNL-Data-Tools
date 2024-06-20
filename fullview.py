'''
Displays all availible stats of a single robot
Developed by: Patrick Woollvin, Team Ninth Life

    Copyright (C) 2024 Patrick Woollvin

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import numpy as np
import matplotlib.pyplot as plt
import math
from datetime import datetime

columns = [1, 2, 3]

# UI Shit

year = input("Enter year of recording or press enter for current year (YYYY): ")
month = input("Enter month of recording or press enter for current month (MM): ")
day = input("Enter day of recording or press enter for current day (DD): ")

if not year:
    year = str(datetime.now().year)
if not month:
    month = str(datetime.now().month)
    if len(month) < 2:
        month = "0" + month
if not day:
    day = str(datetime.now().day)

print("")
name = input("Bot's profile name: ")

dia = int(input("Bot's blade diameter in mm: "))

#RPM
file = 'data/{}-{}-{}-{}.csv'.format(name, year, month, day)
data = np.genfromtxt(file, delimiter=',', dtype=None)

x = []
y = []

top_rpm = 0.0

for f in range(1, len(data)):
    x.append(f)
    y.append(float(data[f][2]))
    if float(data[f][2]) > top_rpm:
        top_rpm = float(data[f][2])
    print("line {} proccessed, value {}".format(f, data[f][2]))

top_speed = round(2 * math.pi * (dia / 2) * top_rpm / 26820, 1)

fig, ax = plt.subplots()

ax.plot(x, y)
text = fig.text(0.02, 0.02, "Max RPM: {}, Max Speed: {} MPH".format(top_rpm, top_speed))
fig.suptitle("File: {}".format(file))
fig.canvas.manager.set_window_title("{} RPM".format(name))


#amps
x2 = []
y2 = []

top_amps = 0.0

for f in range(1, len(data)):
    x2.append(f)
    y2.append(float(data[f][1]))
    if float(data[f][1]) > top_amps:
        top_amps = float(data[f][1])
    print("line {} proccessed, value {}".format(f, data[f][1]))

fig2, ax2 = plt.subplots()

ax2.plot(x2, y2)
text = fig2.text(0.02, 0.02, "Max Amperage: {} Amps, Average Amperage: {} Amps".format(top_amps, round(np.mean(y2), 1)))
fig2.suptitle("File: {}".format(file))
fig2.canvas.manager.set_window_title("{} Amps".format(name))


#Temp
x3 = []
y3 = []

top_temp = 0.0

for f in range(1, len(data)):
    x3.append(f)
    y3.append(float(data[f][3]))
    if float(data[f][3]) > top_temp:
        top_temp = float(data[f][3])
    print("line {} proccessed, value {}".format(f, data[f][3]))

fig3, ax3 = plt.subplots()

ax3.plot(x3, y3)
text = fig3.text(0.02, 0.02, "Max Temperature: {} C".format(top_temp))
fig3.suptitle("File: {}".format(file))
fig3.canvas.manager.set_window_title("{} Temp".format(name))

plt.show()