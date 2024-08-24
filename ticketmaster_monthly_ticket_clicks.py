import pandas as pd
import matplotlib.ticker as mtick

df = pd.read_csv('/home/evan/Documents/development/table/click view/without_order_link_id/combined/combined.csv')
df['action_date'] = pd.to_datetime(df['date'])
df.rename(columns={'category': 'number_of_ticket_clicks'}, inplace=True)

monthly_clicks = df.resample('ME', on='action_date').agg({"number_of_ticket_clicks":'count'})

monthly_clicks_graph = monthly_clicks.plot(kind='line')
monthly_clicks_graph.set_xlabel("Month")
monthly_clicks_graph.set_ylabel("Number of ticket clicks")
monthly_clicks_graph.set_title('Monthly ticket clicks to Ticketmaster vendors - 2022 to 2024')
fmt = '{x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
monthly_clicks_graph.yaxis.set_major_formatter(tick)

fig = monthly_clicks_graph.get_figure()
fig.set_tight_layout(True)
fig.savefig('ticketmaster-ticket-clicks-by-month.png')