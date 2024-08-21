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

df.rename(columns={'category': 'number_of_ticket_clicks'}, inplace=True)
yearly_clicks = df.resample('Y', on='action_date').agg({"number_of_ticket_clicks":'count'})
yearly_clicks = yearly_clicks.iloc[1:]
yearly_clicks['date'] = yearly_clicks.index.strftime('%Y')
ax = yearly_clicks.plot(kind='bar')
ax.set_title('Yearly drop in ticket click numbers - 2023 to 2024')
ax.set_xticklabels(yearly_clicks['date'])
fmt = '{x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)
ax.set_xlabel("Year")
ax.set_ylabel("Total ticket clicks")
fig = ax.get_figure()
fig.autofmt_xdate()
fig.set_tight_layout(True)
fig.savefig('ticketmaster-ticket-clicks-2023-to-2024.png')