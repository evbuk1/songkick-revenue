import pandas as pd
import matplotlib.ticker as mtick

df = pd.read_pickle('combined_df.pkl')
df['action_date'] = pd.to_datetime(df['Action Date'])
df.rename(columns={'category': 'number_of_ticket_clicks'}, inplace=True)

monthly_clicks = df.resample('ME', on='action_date').agg({"number_of_ticket_clicks":'count'})

ax = monthly_clicks.plot(kind='line')
ax.set_xlabel("Month")
ax.set_ylabel("Number of ticket clicks")
ax.set_title('Monthly ticket clicks to Ticketmaster vendors - 2022 to 2024')
fmt = '{x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

fig = ax.get_figure()
fig.set_tight_layout(True)
fig.savefig('ticketmaster-ticket-clicks-by-month-2yr.png')