# Run data prep script first!

import pandas as pd
import matplotlib.ticker as mtick

df = pd.read_csv('/home/evan/Documents/development/table/impact/combined.csv')
df['action_date'] = pd.to_datetime(df['Action Date'])

fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)

dff = df.groupby(["Brand"])['Action Earnings'].sum().reset_index()
sorted_df = dff.sort_values('Action Earnings', ascending=False)
top_five_countries = sorted_df.head(5)['Brand'].to_list()

df = df[df['Brand'].isin(top_five_countries)]

earnings_by_country = pd.pivot_table(df, values="Action Earnings", index=pd.Grouper(freq='ME', key="action_date"), columns=["Brand"], aggfunc='sum', fill_value=0)

earnings_by_country_graph = earnings_by_country.plot(kind='line')
earnings_by_country_graph.set_xlabel("Month")
earnings_by_country_graph.set_ylabel("Total Earnings")
earnings_by_country_graph.set_title('Ticketmaster Monthly Earnings - top 5 countries')
earnings_by_country_graph.yaxis.set_major_formatter(tick)
handles, labels = earnings_by_country_graph.get_legend_handles_labels()
earnings_by_country_graph.legend(reversed(handles), reversed(labels), bbox_to_anchor=(1,1))

earnings_by_country_figure = earnings_by_country_graph.get_figure()
earnings_by_country_figure.set_tight_layout(True)
earnings_by_country_figure.savefig('ticketmaster-monthly-earnings-by-country.png')
