# Run data prep script first!

import pandas as pd
import matplotlib.ticker as mtick

df = pd.read_pickle('combined_df.pkl')
df['action_date'] = pd.to_datetime(df['Action Date'])

ax = pd.pivot_table(df, values="Action Earnings", index=pd.Grouper(freq='ME', key="action_date"), columns=["source"], aggfunc='sum', fill_value=0)
bx = pd.pivot_table(df, values="Action Earnings", index=pd.Grouper(freq='ME', key="action_date"), columns=["login_status"], aggfunc='sum', fill_value=0)

graph = ax.plot(kind='line')
graph.set_xlabel("Month")
graph.set_ylabel("Total Earnings")
graph.set_title('Monthly earnings from Ticketmaster by platform')
fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
graph.yaxis.set_major_formatter(tick)

fig = graph.get_figure()
fig.set_tight_layout(True)
fig.savefig('ticketmaster-by-source.png')

graph = bx.plot(kind='line')
graph.set_xlabel("Month")
graph.set_ylabel("Total Earnings")
graph.set_title('Monthly earnings from Ticketmaster by user type')
fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
graph.yaxis.set_major_formatter(tick)

fig = graph.get_figure()
fig.set_tight_layout(True)
fig.savefig('ticketmaster-by-user-type.png')

