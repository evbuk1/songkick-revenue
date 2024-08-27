# Run data prep script first!

import pandas as pd
import matplotlib.ticker as mtick

df = pd.read_pickle('combined_df_left.pkl')
df['action_date'] = pd.to_datetime(df['Action Date'])
df["login_status"].fillna("unattributable", inplace = True)
df = df.loc[df['action_date'].dt.month == 7]

fmt = '${x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)

earnings_by_user_type = pd.pivot_table(df, values="Action Earnings", index=pd.Grouper(freq='ME', key="action_date"), columns=["login_status"], aggfunc='sum', fill_value=0)

earnings_by_user_type.loc['Total'] = earnings_by_user_type.sum()
earnings_by_user_type = earnings_by_user_type.sort_values('Total', axis=1, ascending=True).drop('Total')
earnings_by_user_type.index = pd.to_datetime(earnings_by_user_type.index).strftime('%m-%Y')

earnings_by_user_type_graph = earnings_by_user_type.plot(kind='bar', stacked=True)
handles, labels = earnings_by_user_type_graph.get_legend_handles_labels()
earnings_by_user_type_graph.legend(reversed(handles), reversed(labels), bbox_to_anchor=(1,1))
earnings_by_user_type_graph.set_xlabel("Year and month")
earnings_by_user_type_graph.set_ylabel("Total Earnings")
earnings_by_user_type_graph.set_title('July earnings from Ticketmaster by user type - 2022 to 2024')
earnings_by_user_type_graph.yaxis.set_major_formatter(tick)

earnings_by_user_type_figure = earnings_by_user_type_graph.get_figure()
earnings_by_user_type_figure.autofmt_xdate()
earnings_by_user_type_figure.set_tight_layout(True)
earnings_by_user_type_figure.savefig('ticketmaster-by-user-type-july.png')