import requests
import pandas as pd
import streamlit as st

url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
response = requests.request('GET',url)
if response.status_code == 200:
    print("連線成功")
    all_data = response.json()
    print(type(all_data))
else:
    print(f"連線失敗:{response.status_code}")



dataFrame = pd.DataFrame(data=all_data,columns=['sna','tot','sbi','sarea','mday','ar','bemp','act'])

dataFrame.columns = ["站點名稱","車數","可借","行政區","時間","地址","可還","狀態"]
dataFrame1 = dataFrame.set_index("站點名稱")
areas = dataFrame1['行政區'].unique()

min,max = st.slider(
    '請選擇可借的(<=數量)',
    0, 100, (0, 100))
mask = (dataFrame1['可借'] <= max) & (dataFrame1['可借'] >= min)
mask_dataFrame = dataFrame1[mask]
count = mask_dataFrame["車數"].count()
st.write("符合條件的站點數:",count)
st.dataframe(mask_dataFrame)

option = st.selectbox('行政區域',areas)

st.write('You selected:', option)