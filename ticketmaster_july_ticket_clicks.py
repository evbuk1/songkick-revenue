import pandas as pd
import matplotlib.ticker as mtick

df = pd.read_pickle('ticket_clicks.pkl')
# df is already limited to July by preparation script in ticketmaster_click_prep.py

df.rename(columns={'category': 'number_of_ticket_clicks'}, inplace=True)
monthly_clicks = df.resample('ME', on='action_date').agg({'number_of_ticket_clicks': 'count'})
monthly_clicks = monthly_clicks.loc[~(monthly_clicks==0).all(axis=1)]
monthly_clicks.index = pd.to_datetime(monthly_clicks.index).strftime('%m-%Y')

ax = monthly_clicks.plot(kind='bar')


ax.set_xlabel("Month and year")
ax.set_ylabel("Total ticket clicks")
ax.set_title('July ticket clicks to Ticketmaster vendors - 2022 to 2024')
ax.get_yaxis().get_major_formatter().set_scientific(False)
fmt = '{x:,.0f}'
tick = mtick.StrMethodFormatter(fmt)
ax.yaxis.set_major_formatter(tick)

fig = ax.get_figure()
fig.autofmt_xdate()
fig.set_tight_layout(True)
fig.savefig('ticketmaster-july-ticket-clicks-2022-to-2024.png')