# from sqlalchemy import true
import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time

st.title('入門')
# st.write('DataFrame')

# df=pd.DataFrame(
#     np.random.rand(100,2)/[50,50]+[35.69,139.70],
#     columns=['lat','lon']
# )

# st.table(df.style.highlight_max(axis=0))
# st.bar_chart(df)
# st.map(df)

# if st.checkbox('showImage'):
#     st.write('display Image')
#     img=Image.open('miffy.jpeg')
#     st.image(img,caption='ミッフィー',use_column_width=true)

# option=st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1,11))
# )

# 'あなたの好きな数字は',option,'です'
# text=st.text_input('あなたの趣味を教えてください')
# condition=st.slider('あなたの今の調子は？',0,100,50)
# 'あなたの趣味は',text,'です'
# 'コンディション:',condition

# st.write('Interactive Widgets')

# left_column,right_column=st.columns(2)
# button=left_column.button('右カラムに文字を表示')

# if button:
#     right_column.write('ここは右カラムです')

# expander=st.expander('問い合わせ')
# expander.write('問い合わせ1回答')
# expander2=st.expander('問い合わせ２')
# expander2.write('問い合わせ2回答')
# expander3=st.expander('問い合わせ2')
# expander3.write('問い合わせ3回答')

st.write('プログレスバー')
latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.01)

'Done!!'
expander=st.expander('問い合わせ')
expander.write('問い合わせ1回答')
expander2=st.expander('問い合わせ２')
expander2.write('問い合わせ2回答')
expander3=st.expander('問い合わせ2')
expander3.write('問い合わせ3回答')