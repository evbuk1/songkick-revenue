import pandas as pd
import matplotlib.ticker as mtick

df = pd.read_csv('/home/evan/Documents/development/table/email_stats/daily_digest_tm.csv')
df['action_date'] = pd.to_datetime(df['date'])

fmt = '{x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)

monthly_summary = df.resample('ME', on='action_date').agg({"email_sends":'sum', 'email_opens':'sum', 'event_clicks':'sum'})

email_events_month_graph = monthly_summary.plot(kind='line')
email_events_month_graph.set_xlabel("Month")
email_events_month_graph.set_ylabel("Email events")
email_events_month_graph.set_title('Monthly email events from Ticketmaster')
email_events_month_graph.yaxis.set_major_formatter(tick)

email_events_month_figure = email_events_month_graph.get_figure()
email_events_month_figure.set_tight_layout(True)
email_events_month_figure.savefig('ticketmaster-email-events-by-month.png')
