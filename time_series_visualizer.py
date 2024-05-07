import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('datas/fcc-forum-pageviews.csv', 
                 parse_dates=['date'], 
                 index_col=['date'])

# Clean data
df = df[
    (df['value'] >= df['value'].quantile(0.025))&
    (df['value'] <= df['value'].quantile(0.975))
]


def draw_line_plot():
    # Draw line plot
    plt.figure(figsize=(15, 5))
    plt.plot(df['value'])

    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    plt.savefig('line_plot.png')
    return plt

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    ddf_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['year'] = df_bar['date'].dt.year
    df_bar['month'] = df_bar['date'].dt.strftime('%B')
    df_bar = df_bar.groupby(['year', 'month'], as_index=False)['value'].mean()

    # Draw bar plot
    plt.figure(figsize=(8, 8))
    sns.barplot(x='year', y='value', hue='month', 
                data=df_bar, palette='tab20')
    
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', loc='upper left')

    # Save image and return fig (don't change this part)
    plt.savefig('bar_plot.png')
    return plt

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    plt.figure(figsize=(30, 10))
    
    plt.subplot(1, 2, 1)
    sns.boxplot(x='year', y='value', data=df_box, fill=False)
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    
    plt.subplot(1, 2, 2)
    sns.boxplot(x='month', y='value', data=df_box)
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    plt.savefig('box_plot.png')
    return plt
