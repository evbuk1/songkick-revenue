from calendar import month

import pandas as pd
import matplotlib.ticker as mtick

df = pd.read_csv('/home/evan/Documents/development/table/impact/combined.csv')
df['date'] = pd.to_datetime(df['Action Date'])
df = df.loc[df['date'].dt.month == 7]

monthly_summary = df.resample('ME', on='date')['Action Earnings'].sum().loc[lambda x: x!= 0]
monthly_summary.index = pd.to_datetime(monthly_summary.index).strftime('%m-%Y')

ax = monthly_summary.plot(kind='bar')
ax.set_xlabel("Month and year")
ax.set_ylabel("Total Earnings")
ax.set_title('July earnings from Ticketmaster vendors - 2022 to 2024')
fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

fig = ax.get_figure()
fig.autofmt_xdate()
fig.set_tight_layout(True)
fig.savefig('ticketmaster-earnings-by-year-july.png')


