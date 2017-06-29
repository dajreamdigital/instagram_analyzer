import matplotlib.pyplot as plt


def instagram_graph(instagram_scraped):
    '''
    Displays all the graphs
    '''

    fig = plt.figure(figsize=(8, 6))

    # axis 1
    plt.subplot2grid((3, 3), (0, 0), colspan=3, rowspan=1)
    instagram_scraped['Comments Count'].plot(kind='bar', alpha=.55)
    plt.title("Total Comments Count")

    # axis 2
    plt.subplot2grid((3, 3), (1, 0), colspan=3, rowspan=1)
    instagram_scraped['Likes Count'].plot(kind='bar', alpha=.55)
    plt.title("Total Likes Count")

    # axis 3
    plt.subplot2grid((3, 3), (2, 0), colspan=3, rowspan=1)
    plt.hist(instagram_scraped['Likes Count'])
    plt.title('Distribution of Likes on Instagram Posts', fontsize=20)
    plt.xlabel('Amount of Posts', fontsize=18)
    plt.ylabel('Likes', fontsize=16)
    plt.rcParams["figure.figsize"]

    fig.tight_layout()