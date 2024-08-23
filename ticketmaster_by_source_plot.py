# Run data prep script first!

import pandas as pd
import matplotlib.ticker as mtick

df = pd.read_pickle('combined_df.pkl')
df['action_date'] = pd.to_datetime(df['Action Date'])

fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)

earnings_by_source = pd.pivot_table(df, values="Action Earnings", index=pd.Grouper(freq='ME', key="action_date"), columns=["source"], aggfunc='sum', fill_value=0)
earnings_by_user_type = pd.pivot_table(df, values="Action Earnings", index=pd.Grouper(freq='ME', key="action_date"), columns=["login_status"], aggfunc='sum', fill_value=0)
earnings_by_source_year = pd.pivot_table(df, values="Action Earnings", index=pd.Grouper(freq='Y', key="action_date"), columns=["source"], aggfunc='size', fill_value=0)
earnings_by_source_year.loc['Total'] = earnings_by_source_year.sum()
earnings_by_source_year = earnings_by_source_year.sort_values('Total', axis=1, ascending=True).drop('Total')
earnings_by_source_year.index = pd.to_datetime(earnings_by_source_year.index).strftime('%Y')
print(earnings_by_source_year.head(10))

earnings_bu_source_graph = earnings_by_source.plot(kind='line')
earnings_bu_source_graph.set_xlabel("Month")
earnings_bu_source_graph.set_ylabel("Total Earnings")
earnings_bu_source_graph.set_title('Monthly earnings from Ticketmaster by platform')
earnings_bu_source_graph.yaxis.set_major_formatter(tick)

earnings_by_source_figure = earnings_bu_source_graph.get_figure()
earnings_by_source_figure.set_tight_layout(True)
earnings_by_source_figure.savefig('ticketmaster-by-source.png')

earnings_by_user_type_graph = earnings_by_user_type.plot(kind='line')
earnings_by_user_type_graph.set_xlabel("Month")
earnings_by_user_type_graph.set_ylabel("Total Earnings")
earnings_by_user_type_graph.set_title('Monthly earnings from Ticketmaster by user type')
earnings_by_user_type_graph.yaxis.set_major_formatter(tick)

earnings_by_user_type_figure = earnings_by_user_type_graph.get_figure()
earnings_by_source_figure.set_tight_layout(True)
earnings_by_user_type_figure.savefig('ticketmaster-by-user-type.png')

earnings_by_source_year_graph = earnings_by_source_year.plot(kind='bar', stacked=True)
handles, labels = earnings_by_source_year_graph.get_legend_handles_labels()
earnings_by_source_year_graph.legend(reversed(handles), reversed(labels), bbox_to_anchor=(1,1))
earnings_by_source_year_graph.set_xlabel("Year")
earnings_by_source_year_graph.set_ylabel("Total Earnings")
earnings_by_source_year_graph.set_title('Yearly earnings from Ticketmaster by source')
earnings_by_source_year_graph.yaxis.set_major_formatter(tick)

earnings_by_source_year_figure = earnings_by_source_year_graph.get_figure()
earnings_by_source_year_figure.set_tight_layout(True)
earnings_by_source_year_figure.savefig('ticketmaster-by-source-year.png')
