import pandas as pd
import matplotlib.ticker as mtick

df = pd.read_csv('/home/evan/Documents/development/table/email_stats/daily_digest_tm.csv')
df['action_date'] = pd.to_datetime(df['date'])
df = df.loc[df['action_date'].dt.month == 7]
df = df.set_index('action_date').sort_index()

df.index = pd.to_datetime(df.index).strftime('%m-%Y')

fmt = '{x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)

email_events_year_graph = df.plot(kind='bar')
email_events_year_graph.set_xlabel("Month and year")
email_events_year_graph.set_ylabel("Email events")
email_events_year_graph.set_title('July comparison of email events for Ticketmaster')
email_events_year_graph.yaxis.set_major_formatter(tick)

email_events_year_figure = email_events_year_graph.get_figure()
email_events_year_figure.autofmt_xdate()
email_events_year_figure.set_tight_layout(True)
email_events_year_figure.savefig('ticketmaster-email-events-july.png')

df['conversion_rate'] = df.apply(lambda row: round((row['event_clicks'] / row['email_opens']) * 100, 2), axis=1)
fmt = '{x:,.0f}%'
tick = mtick.StrMethodFormatter(fmt)
df = df.drop(['email_sends', 'email_opens', 'event_clicks'], axis=1)

conversion_rate_graph = df.plot(kind='bar')
conversion_rate_graph.set_xlabel("Month and year")
conversion_rate_graph.set_ylabel("Conversion rate")
conversion_rate_graph.set_title('Conversion rate of email opens to event clicks')
conversion_rate_graph.yaxis.set_major_formatter(tick)

conversion_rate_figure = conversion_rate_graph.get_figure()
conversion_rate_figure.autofmt_xdate()
conversion_rate_figure.set_tight_layout(True)
conversion_rate_figure.savefig('ticketmaster-email-conversion-rate.png')
