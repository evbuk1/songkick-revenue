import pandas as pd
import matplotlib.ticker as mtick

df = pd.read_csv('/home/evan/Documents/development/table/email_stats/daily_digest_tm.csv')
df['action_date'] = pd.to_datetime(df['date'])

fmt = '{x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)

yearly_summary = df.resample('YE', on='action_date').agg({"email_sends":'sum', 'email_opens':'sum', 'event_clicks':'sum'})
yearly_summary.index = pd.to_datetime(yearly_summary.index).strftime('%Y')
yearly_summary.loc['Total'] = yearly_summary.sum()
yearly_summary = yearly_summary.sort_values('Total', axis=1, ascending=True).drop('Total')

email_events_year_graph = yearly_summary.plot(kind='bar', stacked=True)
handles, labels = email_events_year_graph.get_legend_handles_labels()
email_events_year_graph.legend(reversed(handles), reversed(labels), bbox_to_anchor=(1,1))
email_events_year_graph.set_xlabel("Year")
email_events_year_graph.set_ylabel("Email events")
email_events_year_graph.set_title('Yearly email events from Ticketmaster')
email_events_year_graph.yaxis.set_major_formatter(tick)

email_events_year_figure = email_events_year_graph.get_figure()
email_events_year_figure.set_tight_layout(True)
email_events_year_figure.savefig('ticketmaster-email-events-by-year.png')