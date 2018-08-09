import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
import SentimentAnalysis3 as sa
from matplotlib import path as path
from matplotlib import patches as pat

# In[44]:


def create_bar_graph(names, graph_label):

    i = 0
    r = []
    bars = []
    for name in names:
        bars.append(sa.main(name))
        r.append(i)
        i = i + 1

    orangeBars = []
    greenBars = []
    redBars = []

    for bar in bars:
        orangeBars.append(float(bar[1]) + float(bar[0]) + float(bar[2]))
        greenBars.append(float(bar[1]) + float(bar[0]))
        redBars.append(float(bar[0]))

    barWidth = 0.80

    print(orangeBars)

    # Create orange Bars
    plt.bar(r, orangeBars, color='#e90c00', edgecolor='white', width=barWidth, label="Neutral Sentiment")
    # Create green Bars
    plt.bar(r, greenBars, color='#00cf0b', edgecolor='white', width=barWidth, label="Positive Sentiment")
    # Create blue Bars
    plt.bar(r, redBars, color='#ff8f03', edgecolor='white', width=barWidth, label="Negative Sentiment")

    fig_size = plt.rcParams["figure.figsize"]
    fig_size[0] = 12
    fig_size[1] = 8
    plt.rcParams["figure.figsize"] = fig_size
    plt.rcParams.update({'font.size': 14})

    # Custom x axis
    plt.xticks(r, names)
    plt.xlabel("\n" + graph_label)

    # Add a legend
    plt.legend(loc='upper left', bbox_to_anchor=(1,1), ncol=1)
    #plt.figure(figsize=(1000,300))
    # Show graphic
    plt.show()


def create_pie_chart(names):

    graph_colors = ['#ff8f03', '#00cf0b', '#e90c00']
    orange_pat = pat.Patch(color='orange', label='Neutral')
    green_pat = pat.Patch(color='green', label='Positive')
    red_pat = pat.Patch(color='red', label='Negative')

    count=0
    for name in names:
        if name != '':
            count = count+1

    nr = (count/3) + 1

    if count <= 3:
        nc = count
    elif count == 3:
        nr = 2
        nc = 2
    else:
        nc = 3

    i = 1
    for name in names:
        val = sa.main(name)
        plt.subplot(nr, nc, i)
        plt.title(name)
        plt.pie(val, colors=graph_colors, shadow=True)
        i = i+1

    plt.legend(handles = [orange_pat, green_pat, red_pat])
    plt.show()

def create_line_graph(names):

    line_colors = ['#ff8f03', '#00cf0b', '#e90c00']

    neu_values = []
    pos_values = []
    neg_values = []

    neu_unit = path.Path.unit_circle()
    pos_unit = path.Path.unit_regular_polygon(5)
    neg_unit = path.Path.unit_regular_asterisk(6)

    x = []
    i = 0
    for name in names:
        if name!='':
            val = sa.main(name)
            neu_values.append(val[0])
            pos_values.append(val[1])
            neg_values.append(val[2])
            x.append(i)
            i=i+1

    plt.xticks(x, names)
    plt.ylabel('Percentage %')
    plt.plot(neu_values, color='#ff8f03', marker=neu_unit, label='Neutral')
    plt.plot(pos_values, color='#00cf0b', marker=pos_unit, label='Positive')
    plt.plot(neg_values, color='#e90c00', marker=neg_unit, label='Negative')
    plt.legend(loc='upper right')

    plt.show()


def create_area_graph(names):

    area_colors = ['#ff8f03', '#00cf0b', '#e90c00']

    neu_values = []
    pos_values = []
    neg_values = []

    x = []
    i = 0
    for name in names:
        if name != '':
            val = sa.main(name)
            neu_values.append(float(val[0]))
            pos_values.append(float(val[1]))
            neg_values.append(float(val[2]))
            x.append(i)
            i = i+1

    plt.subplot()
    plt.xticks(x, names)
    plt.ylabel('Percentage %')
    plt.stackplot(x, neu_values, pos_values, neg_values, labels=['Neutral', 'Positive', 'Negative'], colors=area_colors)
    plt.legend()
    plt.show()
