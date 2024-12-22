import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
# 讀取 CSV 文件並指定 'date' 列為日期格式（這樣 pandas 會自動將其解析為 datetime 格式）
df = pd.read_csv('fcc-forum-pageviews.csv',parse_dates=['date'])
df.set_index('date', inplace=True)

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(12, 6)) # 創建一個大小為 12x6 英寸的圖形，並返回圖形 (fig) 和坐標軸 (ax) 物件
    ax.plot(df.index, df['value'], color='tab:blue')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    plt.xticks(rotation=45)
    plt.tight_layout() # 自動調整子圖的間距，以防止標籤或標題重疊

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar.reset_index(inplace=True)
    df_bar['year'] = [d.year for d in df_bar.date] # date 列轉換為年份（d.year）
    df_bar['month'] = [d.strftime('%b') for d in df_bar.date] # 轉換成月份
    df_monthly_avg = df_bar.groupby(['year', 'month'])['value'].mean().unstack() # 計算每組的平均值，並使用 unstack() 轉換為以年份為列索引、月份為行索引的 DataFrame
    # Draw bar plot

    fig, ax = plt.subplots(figsize=(12, 6))
    df_monthly_avg.plot(kind='bar', stacked=False, ax=ax)
    ax.set_title('Average Daily Page Views per Month')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months', labels=['January', 'February', 'March', 'April', 'May', 'June', 
                         'July', 'August', 'September', 'October', 'November', 'December'])
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    df_box['value'] = df_box['value'].astype(int)

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # 1st box plot: Year-wise Box Plot (Trend)
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # 2nd box plot: Month-wise Box Plot (Seasonality)
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    axes[1].set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
