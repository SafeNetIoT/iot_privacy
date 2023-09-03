# 导入必要的库
import matplotlib.pyplot as plt

devices = ['Apple_tv', 'arlo_camera_pro4', 'blink_doorbell', 'boifun_baby',
           'bose_speaker','echodot4','eufy_robovac','furbo_dog_camera',
           'google_nest_doorbell','google_nest_hub','govee_strip_light','lifx_mini',
           'nest_cam','netatmo_weather_station','nokia_tv',
           'petsafe_feeder','ring_doorbell','ring_indoor_cam','roku_tv_stick',
           'simplicam','sonos_speaker','switchbot_hub_mini','toshiba_tv',
           'weekett_kettle','withings_scale','wiz_smart_bulb','wyze_cam_pan_v2'] 
third_party_dns_counts = [4, 0, 0, 2, 5, 5, 0, 5, 3, 4,3, 0, 0, 0, 32, 2, 2, 2, 4, 5, 0, 2, 39, 0, 0, 0, 10]

# 绘制柱状图
plt.figure(figsize=(15,7))  # 设置图像大小
plt.bar(devices, third_party_dns_counts, color='skyblue')  # 绘制柱状图
plt.title("Number of Third-party DNS Connections by IoT Device")
plt.xlabel("IoT Devices")
plt.ylabel("Number of Third-party DNS")
plt.xticks(rotation=45)  # 旋转X轴标签使其更易读
plt.tight_layout()  # 确保所有标签都适应图形窗口
plt.show()



labels = ['>10 Third-party DNS', '0-10 Third-party DNS', 'No Third-party DNS']
sizes = [2, 15, 10]
colors = ['#ff9999', '#66b2ff', '#ffcc99']
explode = (0.1, 0.1, 0)  # 突出显示前两个切片

plt.figure(figsize=(10,7))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')
plt.title("IoT Devices by Number of Third-party DNS Connections")
plt.show()
