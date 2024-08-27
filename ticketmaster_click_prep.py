import pandas as pd

df = pd.read_csv('/home/evan/Documents/development/table/click view/without_order_link_id/combined/combined.csv')
df['action_date'] = pd.to_datetime(df['date'])
df = df.loc[df['action_date'].dt.month == 7]

df.to_pickle('ticket_clicks.pkl')