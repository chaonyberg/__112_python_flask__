import requests
url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
response = requests.request('GET',url)
response.status_code
if response.status_code == 200:
    print('連線成功')
    all_data = response.json()
    print(type(all_data))
else:
    print(f"連線失敗:{response.status_code}")



import pandas as pd
dataFrame = pd.DataFrame(data=all_data,columns=['sno','sna','tot','sbi','sarea','mday','ar','bemp','act'])
dataFrame
df2 = dataFrame.rename(columns={'sno':"編號",
                    'sna':'名稱',
                    'tot':'車輛數',
                    'sbi':'可借',
                    'sarea':'行政區',
                    'mday':'日期',
                    'ar':'地址',
                    'bemp':'可還',
                    'act':'狀態'})



#mask = dataFrame['sbi'] <= 3
#print(dataFrame[mask])
min = int(input('請輸入要查詢的可借數量:'))
mask = df2['可借2'] <= min
mask_dataFrame = df2[mask]
mask_dataFrame.to_csv("可借小於3的站點.cvs")
filename = f'可借小於{min}的站點.xlsx'
mask_dataFrame.to_excel(filename)