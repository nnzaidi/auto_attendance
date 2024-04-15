import pandas as pd
import numpy as np

def create_df(month):

    if month == 'march':
        first = '3/1/2024'
        last = '3/31/2024'
    if month == 'april':
        first = '4/1/2024'
        last = '4/30/2024'
    if month == 'may':
        first = '5/1/2024'
        last = '5/31/2024'

    df = pd.DataFrame(columns = ['Tarikh','Hari','Masuk','Keluar','Tandatangan','Catatan'], dtype=None)

    df['Tarikh'] = pd.date_range(start=first, end=last)
    df['Hari'] = df['Tarikh'].dt.day_of_week
    df['Tarikh'] = df['Tarikh'].dt.strftime('%d-%m-%Y')

    df['Hari'] = df['Hari'].map({
        0   :   'Isnin',
        1   :   'Selasa',
        2   :   'Rabu',
        3   :   'Khamis',
        4   :   'Jumaat',
        5   :   'Sabtu',
        6   :   'Ahad'
    })

    df = df[~df['Hari'].isin(['Jumaat','Sabtu'])]
    df.index = np.arange(1, len(df)+1)

    return df