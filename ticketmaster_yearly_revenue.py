import pandas as pd
import matplotlib.ticker as mtick
import numpy as np

df = pd.read_csv('/home/evan/Documents/development/table/impact/combined.csv')
df['date'] = pd.to_datetime(df['Action Date'])

yearly_summary = df.resample('Y', on='date')['Action Earnings'].sum()
yearly_summary.index = pd.to_datetime(yearly_summary.index).strftime('%Y')

ax = yearly_summary.plot(kind='bar')
ax.set_xlabel("Year")
ax.set_ylabel("Total Earnings")
ax.set_title('Yearly earnings from Ticketmaster vendors - 2022 to 2024')
fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

fig = ax.get_figure()
fig.set_tight_layout(True)
fig.savefig('ticketmaster-earnings-by-year-2022-2024.png')


