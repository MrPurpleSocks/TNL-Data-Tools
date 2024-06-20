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

fig, ax = plt.subplots()
fig.suptitle("All {}".format(num))
fig.canvas.manager.set_window_title("All NDY RPM")

for j in range(num):
    found_x = 0

    file = 'data/{}-{}-{}-{}.csv'.format(bot_info[j][0], year, month, day)
    data = np.genfromtxt(file, delimiter=',', dtype=None)

    dia = float(bot_info[j][1])
    
    # find the first y value of 14500 or greater
    for f in range(1, len(data)):
        match = False
        if int(data[f][2]) >= 14500:
            match = True
            found_x = f
            print("line {} proccessed, value {}, is match {}".format(f, data[f][2], match))
            print("Match found at line {}!".format(f))
            break
        print("line {} proccessed, value {}, is match {}".format(f, data[f][2], match))

    # get values in range
    first_index = found_x - 45
    last_index = found_x + 45

    x = []
    y = []
    for f in range(first_index, last_index):
        y.append(float(data[f][2]))
        print("line {} proccessed, value {}".format(f, data[f][2]))
    for i in range(90):
        x.append(i)

    ax.plot(x, y)

plt.show()