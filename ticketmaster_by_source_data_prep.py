import pandas as pd


def label_source(row):
    if row['device'] == 'ios' and row['mobile_or_desktop'] == 'app':
        return 'ios_app'
    elif row['device'] == 'android' and row['mobile_or_desktop'] == 'app':
        return 'android_app'
    elif row['device'] == 'skweb' and row['mobile_or_desktop'] == 'mobile':
        return 'mobile_web'
    elif row['device'] == 'skweb' and row['mobile_or_desktop'] == 'desktop':
        return 'skweb_desktop'
    return 'unattributable'


impact_df = pd.read_csv('/home/evan/Documents/development/table/impact/combined.csv')
click_df = pd.read_csv('/home/evan/Documents/development/table/click view/without_order_link_id/combined/combined.csv')
impact_df.rename(columns={'Sub Id 2': 'order_link_id'}, inplace=True)

combined_df = impact_df.merge(click_df, on=['order_link_id'], how='left')

combined_df['source'] = combined_df.apply(label_source, axis=1)

combined_df.to_pickle('combined_df_left.pkl')
