import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
import SentimentAnalysis3 as sa
from matplotlib import path as path

# In[44]:


def create_bar_graph(names, graph_label):

    # Data
    r = [0,1,2,3]

    bars = [sa.main(names[0]), sa.main(names[1]), sa.main(names[2]), sa.main(names[3])]

    orangeBars = [bars[0][0], bars[1][0], bars[2][0], bars[3][0]]
    greenBars = [bars[0][1], bars[1][1], bars[2][1], bars[3][1]]
    blueBars = [bars[0][2], bars[1][2], bars[2][2], bars[3][2]]

    barWidth = 0.80

    # Create orange Bars
    plt.bar(r, orangeBars, bottom=greenBars, color='#e90c00', edgecolor='white', width=barWidth, label="Negative Sentiment")
    # Create green Bars
    plt.bar(r, greenBars, color='#00cf0b', edgecolor='white', width=barWidth, label="Positive Sentiment")
    # Create blue Bars
    plt.bar(r, blueBars, bottom=[i+j for i,j in zip(greenBars, orangeBars)], color='#ff8f03', edgecolor='white', width=barWidth, label="Neutral Sentiment")

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

    count=0
    for name in names:
        if name != '':
            count = count+1

    nr = (count/3) + 1

    if count <= 3:
        nc = count
    else:
        nc = 3

    i = 1
    for name in names:
        if name != '':
            val = sa.main(name)
            plt.subplot(nr, nc, i)
            plt.pie(val, colors=graph_colors, shadow=True, radius=1.2, labeldistance=0.2)
            i = i+1

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
