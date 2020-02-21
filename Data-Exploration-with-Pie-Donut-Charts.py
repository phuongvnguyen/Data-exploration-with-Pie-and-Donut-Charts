#!/usr/bin/env python
# coding: utf-8

# $$\Large \color{green}{\textbf{Khai phá dữ liệu bằng Đồ thị hình Miếng và Donut}}$$
# 
# 
# 
# $$\large \color{blue}{\textbf{Phuong Van Nguyen}}$$
# $$\small \color{red}{\textbf{ phuong.nguyen@summer.barcelonagse.eu}}$$
# 
# 
# Chương trình phân tích dữ liệu này thưc hiện bởi Nguyễn Văn Phương, dựa trên nền tảng $\textbf{Anacoda 1.9.7}$ và $\textbf{Python 3.7}$.
# 
# 
# 
# Toàn bộ Mã chương trình, bao gồm (.py,.ipynb, .html), có thể tải tại Kho trên trang Github của tôi theo đường dẫn dưới đây
# 
# https://github.com/phuongvnguyen/Data-exploration-with-Pie-and-Donut-Charts
# 
# 
# 
# 
# 
# # Gọi các thư viện thuật toán cần thiết
# 
# 
# 
# ## Cho xư lý và phân tích dữ liệu thô
# 

# In[2]:


import os
import numpy as np
import pandas as pd
#from scipy import stats
from pandas import set_option
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# ##  Định nghia biến cho in kết quá

# In[3]:


Purple= '\033[95m'
Cyan= '\033[96m'
Darkcyan= '\033[36m'
Blue = '\033[94m'
Green = '\033[92m'
Yellow = '\033[93m'
Red = '\033[91m'
Bold = "\033[1m"
Reset = "\033[0;0m"
Underline= '\033[4m'
End = '\033[0m'


# # Nhập dự liệu
# 
# Trước khi nhập dữ liệu, bạn chắc chắn rằng thư mục làm việc của bạn có chứa tập tin bạn cần nhập

# In[4]:


print(Bold + Blue + 'Thư mục làm việc hiện tại của bạn:' + End)
print(os.getcwd())


# In[5]:


mydata=pd.read_csv('ptest.csv')


# # Xử lỹ tiền dữ liệu
# 
# 
# 
# 

# In[50]:


print(Bold + Green+  'Mẫu dữ liệu:'+ End)
print(mydata.head(10))
print(Bold + Green+  'Kích thước dữ liệu:'+ End)
print(mydata.shape)
print(Bold + Green+  'Dạng dữ liệu:'+ End)
print(mydata.dtypes)
print(Bold + Green+  'Số dữ liệu thiếu:'+ End)
print(mydata.isnull().sum() )


# In[12]:


mydat=mydata.drop('Level 1', axis=1)
mydat.head(5)


# In[13]:


level2_mydat=mydat.groupby('Level 2')


# In[20]:


record_level2 = pd.DataFrame(columns = ['Nhóm_hàng_level_2', 'Số_lượng_tuyệt_đối',
                                        'Số_lượng_tương_đối'])

for i, colum in enumerate(mydata['Level 2'].unique()):
    Nhóm_hàng_level_2=colum
    Số_lượng_tuyệt_đối=len(level2_mydat.get_group(colum))
    Số_lượng_tương_đối=round(100*len(level2_mydat.get_group(colum))/len(mydata['Tên sản phẩm'].unique()),
                             2)
                             
    temp_df= pd.DataFrame.from_dict({'Nhóm_hàng_level_2': [Nhóm_hàng_level_2],
                                   'Số_lượng_tuyệt_đối': [Số_lượng_tuyệt_đối],
                                   'Số_lượng_tương_đối': [Số_lượng_tương_đối]})
    #print(Nhóm_hàng_level_2,Số_lượng_tuyệt_đối,Số_lượng_tương_đối)
    record_level2=record_level2.append(temp_df,ignore_index=True)
record_level2.sort_values('Số_lượng_tuyệt_đối',ascending=False)


# In[43]:


level3_mydata=mydat.groupby('Level 3')


record_level3 = pd.DataFrame(columns = ['Nhóm_hàng_level_3', 'Số_lượng_tuyệt_đối',
                                        'Số_lượng_tương_đối'])

for i, colum in enumerate(mydata['Level 3'].unique()):
    Nhóm_hàng_level_3=colum
    Số_lượng_tuyệt_đối=len(level3_mydata.get_group(colum))
    Số_lượng_tương_đối=round(100*len(level3_mydata.get_group(colum))/len(mydata['Tên sản phẩm'].unique()),
                             2)
                             
    temp_df= pd.DataFrame.from_dict({'Nhóm_hàng_level_3': [Nhóm_hàng_level_3],
                                   'Số_lượng_tuyệt_đối': [Số_lượng_tuyệt_đối],
                                   'Số_lượng_tương_đối': [Số_lượng_tương_đối]})
    record_level3=record_level3.append(temp_df,ignore_index=True)
record_level3.sort_values('Số_lượng_tuyệt_đối',ascending=False)




# # Khai phá dữ liệu thô bằng đồ thị
# 
# ## Đồ thị miếng (Pie)
# 
# ### Level 2

# In[26]:


record_level22=record_level2.set_index(['Nhóm_hàng_level_2'])
labels=record_level22.index
fig = plt.figure()
#fig1, ax1 = plt.subplots(figsize=(6, 7))
ax = fig.add_axes([0,0,1,1])
ax.axis('equal')
ax.pie(record_level22['Số_lượng_tuyệt_đối'],
         labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
#ax1.axis('equal')  
plt.title('Thị phần 6 nhóm sản phẩm phân theo Level 2',fontsize=14, fontweight='bold')
plt.show()


# $$\textbf{Nhận xét:}$$
# 
# Chúng ta có thể tạo ghi chú bên ngoài Đồ thị như đoạn Mã dưới đây, cách vẽ này đặc biệt hữu dụng khi số lượng nhóm lớn như Level 3

# In[27]:


sizes = record_level22['Số_lượng_tuyệt_đối']
labels=record_level22.index
NUM_COLORS = len(record_level22['Số_lượng_tuyệt_đối'])

fig1, ax1 = plt.subplots(figsize=(6, 5))
fig1.subplots_adjust(0.1,0,1,1)

theme = plt.get_cmap('Dark2') #  'prism'
ax1.set_prop_cycle("color", [theme(1. * i / len(sizes)) for i in range(len(sizes))])

_, _ = ax1.pie(sizes, startangle=90)

ax1.axis('equal')

total = sum(sizes)
plt.legend(
    loc='upper left',
    labels=['%s, %1.1f%%' % (
        l, (float(s) / total) * 100) for l, s in zip(labels, sizes)],
    prop={'size': 11},
    bbox_to_anchor=(0.0, 1),
    bbox_transform=fig1.transFigure
)
plt.title('Thị phần 6 nhóm sản phẩm Level 2',fontsize=14, fontweight='bold')
plt.show()


# $$\textbf{Nhận xét:}$$
# Có vẻ như các cách xây dựng Đồ thị miếng ở trên, ở khía cạnh nào đó, chưa rõ ràng về mặt trực quan, chúng ta hãy thử Câu lệnh dưới đây để xây dựng dạng Đồ thị miếng rõ ràng về trực quan

# In[28]:


fig = px.pie(record_level22, values='Số_lượng_tuyệt_đối', 
             names=record_level22.index, title='Thị phần 6 nhóm sản phẩm Level 2')
fig.show()


# ### Level 3

# In[29]:


record_level32=record_level3.set_index(['Nhóm_hàng_level_3'])
labels3=record_level32['Số_lượng_tuyệt_đối'].index
fig1, ax1 = plt.subplots(figsize=(6, 10))
#fig1, ax1 = plt.subplots()
ax1.pie(record_level32['Số_lượng_tuyệt_đối'],
         labels=labels3, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


# In[30]:


sizes = record_level32['Số_lượng_tuyệt_đối']
labels=record_level32.index
NUM_COLORS = len(record_level22['Số_lượng_tuyệt_đối'])

fig1, ax1 = plt.subplots(figsize=(6, 10))
fig1.subplots_adjust(0.1,0,1,1)

theme = plt.get_cmap('prism')
ax1.set_prop_cycle("color", [theme(1. * i / len(sizes)) for i in range(len(sizes))])

_, _ = ax1.pie(sizes, startangle=90)

ax1.axis('equal')

total = sum(sizes)
plt.legend(
    loc='upper left',
    labels=['%s, %1.1f%%' % (
        l, (float(s) / total) * 100) for l, s in zip(labels, sizes)],
    prop={'size': 11},
    bbox_to_anchor=(0.0, 1),
    bbox_transform=fig1.transFigure
)

plt.show()


# In[31]:


fig = px.pie(record_level32, values='Số_lượng_tuyệt_đối', 
              names=record_level32.index,
             title='Thị phần 39 nhóm sản phẩm Level 3')
#fig.update_traces(textposition='inside', textinfo=record_level32.index)
fig.show()


# $$\textbf{Nhận Xét:}$$
# 
# Chúng ta thấy về mặt trực quan phần ghi chú đã che mất phần số liệu, dó đó, chúng ta dùng Đoạn mã dưới đây để giải quyết việc đó. Kết quả, người dùng chỉ cần di chuột tới phần muốn xem, số liệu sẽ hiện ra

# In[32]:


fig = px.pie(record_level32, values='Số_lượng_tương_đối', 
              names=record_level32.index,
             title='Thị phần 39 nhóm sản phẩm Level 3')
fig.show()


# 
# 
# ## Đồ thị dang Donut
# 

# In[33]:


fig = go.Figure(data=[go.Pie(labels=record_level22.index, 
                             values=record_level22['Số_lượng_tuyệt_đối'],
                             hole=.3)])
#fig.update(layout_title_text='Thị phần 6 nhóm sản phẩm phân theo Level 2',
 #          layout_showlegend=True)

fig.update_layout(
    title_text='Thị phần 6 nhóm sản phẩm phân theo Level 2',
    annotations=[dict(text='Level 2', x=0.5, y=0.5, font_size=20, showarrow=False)])
fig.show()


# ### Level 3

# In[34]:


fig = go.Figure(data=[go.Pie(labels=record_level32.index, 
                             values=record_level32['Số_lượng_tương_đối'],
                             hole=.3)])
fig.update_layout(title_text='Thị phần 39 nhóm sản phẩm (Level 3)',
    annotations=[dict(text='Level 3', x=0.5, y=0.5, font_size=20, showarrow=False)])
fig.show()


# ### Kết hợp 
# Để có được cái nhìn tổng quan nhất về sự phân phối của 12,966 Mặt hàng vào trong các Nhóm hàng khác nhau, bao gồm tất cả các mức độ phân loại nhóm từ Level 1, Level 2, và Level 3, chúng ta sẽ tiến hành xây dựng Đồ thị dạng hình bánh Donut, theo các tuần tự các bước như sau.
# 
# ##### Nhóm toàn bộ Mặt hàng
# 
# 

# In[38]:


#citigo_data.head(5)
level123_mydata=mydata.groupby(['Level 1','Level 2','Level 3'])
print(Bold + Blue + 'Sản phẩn đầu tiên trong từng nhóm hàng:'+ End)

level123=level123_mydata.size()  #agg(['count'])


level23_pan=level123.reset_index() 
level23_pan=level23_pan.rename(columns={0: "Số mặt hàng"})
#print(Bold + Blue + 'Tên các cột trong bảng dữ liệu:'+ End)
#print(level23_pan.columns)
#print(Bold + Blue + 'Dữ liệu của 5 quan sát đầu tiên:'+ End)
print(level23_pan.head(5))

fig = px.sunburst(level23_pan, path=['Level 1', 'Level 2', 'Level 3'], values='Số mặt hàng')
fig.update_layout(title_text='Thị phần tuyệt đối của 12,966 Mặt hàng phân theo các Cấp Nhóm hàng')
fig.show()


# 
# ###### Tính thị phần các mặt hàng theo tỷ lệ phần trăm

# In[39]:


relative=level23_pan['Số mặt hàng']/level23_pan['Số mặt hàng'].sum(axis = 0, skipna = True) 

relative=round(100*relative,2)
#relative

level23_pan['Thị phần (%)']=relative
level23_pan.head(5)

##### Dựng đồ thị

fig = px.sunburst(level23_pan, path=['Level 1', 'Level 2', 'Level 3'], values='Thị phần (%)')
fig.update_layout(title_text='Thị phần tương đối (%) của 12,966 Mặt hàng phân theo các Cấp Nhóm hàng')
fig.show()


# # Kết luận
# 
# 
# 
# Xin cảm ơn các bạn đã dành thời gian đọc và xem toàn bộ quy trình thực hiện. Mọi chi tiết câu hỏi, nhận xét và đóng góp xin các bạn vui lòng gửi về theo địa chỉ thư điện tử dưới đây.
# 
# 
# 
# $$\small \color{red}{\textbf{ phuong.nguyen@summer.barcelonagse.eu}}$$
# 
# $\Large \color{Blue}{\textbf{ --------------------------------------------------------------------------------------}}$
# 
# $$\small \color{red}{\textbf{The End}}$$
# 
# 
# $\Large \color{Blue}{\textbf{ --------------------------------------------------------------------------------------}}$

# In[ ]:




