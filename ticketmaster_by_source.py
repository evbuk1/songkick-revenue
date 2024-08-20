import pandas as pd

new_rows = []
impact_df = pd.read_csv('/home/evanbrown/table/impact/combined.csv')
click_df = pd.read_csv('/home/evanbrown/table/click view/uncompressed/combined.csv')

for index, click_row in click_df.iterrows():
    order_link_id = click_row['order_link_id']
    impact_row = impact_df.query('`Sub Id 2` == @order_link_id')
    if impact_row.empty:
        continue
    else:
        new_row = {'date': impact_row['Action Date'], 'earnings': impact_row['Action Earnings']}
        if click_row['device'] == 'ios' and click_row['mobile_or_desktop'] == 'app':
            new_row['source'] = 'ios_app'
        elif click_row['device'] == 'android' and click_row['mobile_or_desktop'] == 'app':
            new_row['source'] = 'android_app'
        elif click_row['device'] == 'android' or click_row['device'] == 'ios':
            new_row['source'] = 'mobile_web'
        elif click_row['device'] == 'skweb' and click_row['mobile_or_desktop'] == 'desktop':
            new_row['source'] = 'skweb_desktop'
        new_rows.append(new_row)

combined_df = pd.DataFrame(new_rows)
combined_df.to_pickle('combined_df.pkl')