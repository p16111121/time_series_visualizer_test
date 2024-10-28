import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
lower_bound = df['value'].quantile(0.025)
upper_bound = df['value'].quantile(0.975)
df = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)]

def draw_line_plot():
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['value'], color='blue', linewidth=1)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.xticks(rotation=45)
    plt.grid()
    plt.savefig('line_plot.png')
    return plt.gcf()

def draw_bar_plot():
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    monthly_avg = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    
    plt.figure(figsize=(12, 6))
    monthly_avg.plot(kind='bar', ax=plt.gca())
    plt.title('Average Daily Page Views per Month by Year')
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                                         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.xticks(rotation=0)
    plt.savefig('bar_plot.png')
    return plt.gcf()

def draw_box_plot():
    df_box = df.copy()
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.month

    plt.figure(figsize=(14, 6))

    plt.subplot(1, 2, 1)
    sns.boxplot(x='year', y='value', data=df_box)
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')

    plt.subplot(1, 2, 2)
    sns.boxplot(x='month', y='value', data=df_box)
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    plt.xticks(ticks=range(12), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                                         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

    plt.tight_layout()
    plt.savefig('box_plot.png')
    return plt.gcf()
