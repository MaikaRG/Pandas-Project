import pandas as pd

def stats(st):    
    stats = st.describe().T
    stats['IQR'] = stats['75%'] - stats['25%']
    stats.head()


def outliers(ou):
    outliers = pd.DataFrame(columns=ou.columns)

    for col in stats.index:
        iqr = stats.at[col,'IQR']
        cutoff = iqr * 3
        lower = stats.at[col,'25%'] - cutoff
        upper = stats.at[col,'75%'] + cutoff
        results = ou[(ou[col] < lower) | 
    
                    (ou[col] > upper)].copy()
        results['Outlier'] = col
        outliers = outliers.append(results)


