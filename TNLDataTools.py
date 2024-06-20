'''DEMO FILE FOR PYPLOT DONT USE'''

import matplotlib.pyplot as plt
import numpy as np

def graph():
    fig, ax = plt.subplots()

    fruits = ['Frog: Blue', 'Butterfly: Red', 'Frog: Yellow', 'Frog: White']
    counts = [2, 1, 1, 1]
    bar_labels = ['Blue', 'Red', 'Yellow', 'White']
    bar_colors = ['tab:blue', 'tab:red', 'tab:olive', 'tab:gray']

    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

    ax.set_ylabel('Number Found')
    ax.set_title('Number of Animals Found in 60 Second by Kind and Color')
    text = fig.text(0.02, 0.02, "Created Using BioHonors Quick Plot, Developed by Patrick Woollvin")
    ax.legend(title='Key: color')

    plt.show()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    graph()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
