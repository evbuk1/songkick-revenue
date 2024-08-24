import pandas as pd
import matplotlib.ticker as mtick
import numpy as np

df = pd.read_csv('/home/evan/Documents/development/table/impact/combined.csv')
df['date'] = pd.to_datetime(df['Action Date'])

print("Number of rows in CSV:", len(df.index))
order_link_ids = df['order_link_id']
empty = np.where(pd.isnull(order_link_ids))
print('Number of rows without an order_link_id:', empty[0].size)

monthly_summary = df.resample('ME', on='date')['Action Earnings'].sum()

ax = monthly_summary.plot(kind='line')
ax.set_xlabel("Month")
ax.set_ylabel("Total Earnings")
ax.set_title('Monthly earnings from Ticketmaster vendors - 2022 to 2024')
fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

fig = ax.get_figure()
fig.set_tight_layout(True)
fig.savefig('ticketmaster-earnings-by-month-2yr.png')


