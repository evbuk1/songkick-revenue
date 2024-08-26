import pandas as pd
import matplotlib.ticker as mtick

df = pd.read_csv('/home/evan/Documents/development/table/click view/without_order_link_id/combined/combined.csv')
df['action_date'] = pd.to_datetime(df['date'])

df.rename(columns={'category': 'number_of_ticket_clicks'}, inplace=True)
yearly_clicks = df.resample('Y', on='action_date').agg({"number_of_ticket_clicks":'count'})

yearly_clicks['date'] = yearly_clicks.index.strftime('%Y')

ax = yearly_clicks.plot(kind='bar')

ax.set_xlabel("Year")
ax.set_ylabel("Total ticket clicks")
ax.set_title('Yearly ticket clicks to Ticketmaster vendors - 2022 to 2024')
ax.set_xticklabels(yearly_clicks['date'])
fmt = '{x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

fig = ax.get_figure()
fig.autofmt_xdate()
fig.set_tight_layout(True)
fig.savefig('ticketmaster-ticket-clicks-2022-to-2024.png')