# csv 파일을 읽어 극도표로 나타내는 프로그램
# numpy 모듈을 사용하여 csv 파일을 읽고, colors와 count를 분리 후 데이터를 가공하여 극도표로 나타냄


import matplotlib.pyplot as plt
import numpy as np


data = np.loadtxt('problem01_data.csv', dtype='str', delimiter=',')

colors = data[:, 0]  # colors에는 csv파일에서 "Color" 에 해당하는 부분이 들어감
colors = colors[1:]  # 색깔 값들 중 맨 앞의 'color' 제외

d = data[:, 1]  # data csv 파일에서 "Count" 에 해당하는 값들이 들어감
d = d[1:]  # 맨 앞의 "Count" 값 제외
d = list(map(int, d))  # 리스트안의 각 요소를 모두 int형식으로 바꾸기

N = len(d)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)

theta = np.arange(0., 2*np.pi, 2*np.pi/N)  # N간격으로 각도를 이용해 간격을 맞춤
radii = d

bars = ax.bar(theta, radii, bottom=0.0)


for color, bar in zip(colors, bars):
    bar.set_facecolor(color)


plt.xticks(theta, colors)
plt.yticks([0, max(d)/2, max(d)])
plt.show()
