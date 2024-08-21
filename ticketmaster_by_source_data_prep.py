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
    return 'not-assigned'


impact_df = pd.read_csv('/home/evanbrown/table/impact/combined.csv')
click_df = pd.read_csv('/home/evanbrown/table/click view/uncompressed/combined.csv')

# Change column name in impact csv first from Sub Id 2 to order_link_id otherwise script will fail
combined_df = impact_df.merge(click_df, on=['order_link_id'], how='inner')

combined_df['source'] = combined_df.apply(label_source, axis=1)

combined_df.to_pickle('combined_df.pkl')
