import func,os,time,sys
import pandas as pd
from datetime import date

args = [arg for arg in sys.argv[1:]]

month = args[0]

if '-in' in args:
    wkt = 'Masuk'
elif '-out' in args:
    wkt = 'Keluar'

fname = r'attendance_{}.csv'.format(month)

if not os.path.isfile(fname):
    data = func.create_df(month)
else:
    with open(fname,"a") as f:
        print("\nFile exists! Filepath is {}\nReading...\n".format(fname))
        data = pd.read_csv(fname)
        
dt = date.today().strftime('%d-%m-%Y')
print('Today is ',dt)

if dt in data['Tarikh'].values:

    data.loc[data['Tarikh']==dt, wkt] = data['Tarikh'].astype(str)
    data.loc[data['Tarikh']==dt, wkt] = time.strftime("%H:%M", time.localtime())
    print("\nTime recorded.\n")
else:
    print("\nCannot find date.\n")

print(data)
data.to_csv(fname, mode='w', index=False)