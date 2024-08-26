# Run data prep script first!

import pandas as pd
import matplotlib.ticker as mtick

df = pd.read_pickle('combined_df_left.pkl')
df['action_date'] = pd.to_datetime(df['Action Date'])

fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)

earnings_by_source_year = pd.pivot_table(df, values="Action Earnings", index=pd.Grouper(freq='YE', key="action_date"), columns=["source"], aggfunc='sum', fill_value=0)

earnings_by_source_year.loc['Total'] = earnings_by_source_year.sum()
earnings_by_source_year = earnings_by_source_year.sort_values('Total', axis=1, ascending=True).drop('Total')
earnings_by_source_year.index = pd.to_datetime(earnings_by_source_year.index).strftime('%Y')

earnings_by_source_year_graph = earnings_by_source_year.plot(kind='bar', stacked=True)
handles, labels = earnings_by_source_year_graph.get_legend_handles_labels()
earnings_by_source_year_graph.legend(reversed(handles), reversed(labels), bbox_to_anchor=(1,1))
earnings_by_source_year_graph.set_xlabel("Year")
earnings_by_source_year_graph.set_ylabel("Total Earnings")
earnings_by_source_year_graph.set_title('Yearly earnings from Ticketmaster by source')
earnings_by_source_year_graph.yaxis.set_major_formatter(tick)

earnings_by_source_year_figure = earnings_by_source_year_graph.get_figure()
earnings_by_source_year_figure.set_tight_layout(True)
earnings_by_source_year_figure.savefig('ticketmaster-by-source-year-left.png')