import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def plot_relations(dataset, main):
    # plot Google UL (Bytes) to number if xdr sessions, session duration, total download and upload
    title = str(main)+' vs Total DL and UL'
    fig = plt.figure(figsize=(15,5))
    
    # plt.subplot(1,4,1)
    # sns.scatterplot(data=dataset[['Dur. (ms).1',main]], x='Dur. (ms).1', y=main)

    # plt.subplot(1,4,2)
    # sns.scatterplot(data=dataset[['Dur. (ms)',main]], x='Dur. (ms)', y=main)

    plt.subplot(1,2,1)
    sns.scatterplot(data=dataset[['Total DL (Bytes)',main]], x='Total DL (Bytes)', y=main)

    plt.subplot(1,2,2)
    sns.scatterplot(data=dataset[['Total UL (Bytes)',main]], x='Total UL (Bytes)', y=main)
    
    plt.suptitle(title)
    return fig