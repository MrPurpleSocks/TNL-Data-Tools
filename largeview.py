'''
Displays the RPM of multiple robots at once
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

bot_info = []

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

num = int(input("Number of Bots: "))

for i in range(num):
    print("")
    name = input("Bot {}'s profile name: ".format(i+1))

    if not name:
        name = "NDY_{}".format(i+1)

    dia = input("Bot {}'s blade diameter in mm: ".format(i+1))
    bot_info.append([name, dia])

start = datetime.now()

#RPM
for j in range(num):
    file = 'data/{}-{}-{}-{}.csv'.format(bot_info[j][0], year, month, day)
    data = np.genfromtxt(file, delimiter=',', dtype=None)

    dia = float(bot_info[j][1])

    x2 = []
    y2 = []

    top_rpm = 0.0

    for f in range(1, len(data)):
        x2.append(f)
        y2.append(float(data[f][2]))
        if float(data[f][2]) > top_rpm:
            top_rpm = float(data[f][2])
        print("line {} proccessed, value {}".format(f, data[f][2]))

    top_speed = round(2 * math.pi * (dia / 2) * top_rpm / 26820, 1)

    fig, ax = plt.subplots()

    ax.plot(x2, y2)
    text = fig.text(0.02, 0.02, "Top RPM: {}, Top Speed: {} MPH".format(top_rpm, top_speed))
    fig.suptitle("File: {}".format(file))
    fig.canvas.manager.set_window_title("NDY {} RPM".format(j+1))

#amps
for j in range(num):
    file = 'data/{}-{}-{}-{}.csv'.format(bot_info[j][0], year, month, day)
    data = np.genfromtxt(file, delimiter=',', dtype=None)

    dia = float(bot_info[j][1])

    x2 = []
    y2 = []

    top_amps = 0.0

    for f in range(1, len(data)):
        x2.append(f)
        y2.append(float(data[f][1]))
        if float(data[f][1]) > top_amps:
            top_amps = float(data[f][1])
        print("line {} proccessed, value {}".format(f, data[f][1]))

    fig, ax = plt.subplots()

    ax.plot(x2, y2)
    text = fig.text(0.02, 0.02, "Top Amperage: {} Amps, Avg. Amperage: {} Amps".format(top_amps, round(np.mean(y2), 1)))
    fig.suptitle("File: {}".format(file))
    fig.canvas.manager.set_window_title("NDY {} Amperage".format(j+1))

print("Time taken: {}".format(datetime.now() - start))

plt.show()