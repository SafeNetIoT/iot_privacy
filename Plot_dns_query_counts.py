import pandas as pd
import matplotlib.pyplot as plt

# 从Excel中读取数据
file_path = '/Users/liujia/Desktop/data/arlo_camera_pro4/dns_query_counts.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

# 计算每个DNS查询次数的标准差，并按标准差降序排序
df['std_dev'] = df.iloc[:, 1:].std(axis=1)
sorted_df = df.sort_values(by='std_dev', ascending=False)

# 选择标准差最大的前5个DNS
top_dns = sorted_df.head(5)

# 绘制折线图
weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4']
for index, row in top_dns.iterrows():
    plt.plot(weeks, row[1:5], label=row[0])

plt.legend(loc='upper right')  # 将图例放在图片的右上方
plt.title('arlo_camera_pro4: Top 5 DNS Query Counts Over 4 Weeks')
plt.xlabel('Weeks')
plt.ylabel('Query Counts')
plt.grid(True)
plt.tight_layout()
plt.show()
