import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('problem04.csv')

# 가져온 데이터 중 필요한 데이터 뽑기
x = data['longitude']
y = data['latitude']
sizes = data['population'].values/500  # 그래프에 동그라미가 너무 크게 나와서 작게 만듬
colors = data['median_house_value'].values


# 산점도 그리기 위해 각 값 넣기, 컬러맵 문제에서 말한 것 처럼 jet 사용, 라벨 붙이기, 색상 투명도 지정
plt.scatter(x, y, s=sizes, c=colors,
            cmap=plt.get_cmap("jet"), label='Population', alpha=0.4)


# 컬러바에 라벨 붙이고 폰트 크기 조절하기, 컬러바에 표시되는 수치의 폰트크기도 조절
cbar = plt.colorbar()
cbar.set_label('median_house_value', size=8)
cbar.ax.tick_params(labelsize=8)

# x축 y축 label 붙이기
plt.xlabel('Longitude', fontsize=8)
plt.ylabel('Latitude', fontsize=8)

# x축 y축 표현 범위와 값 문제에서처럼 지정하기
plt.axis([-124.35, -114.31, 32.540, 41.950])
plt.xticks([-124.35, -121.84, -119.33, -116.82, -114.31], fontsize=8)
plt.yticks([32.540, 34.892, 37.245, 39.598, 41.950], fontsize=8)

# 그리드 보여주고 범례 표시하기, 범례가 문제에서처럼 그리드의 한 칸안에 들어오도록 크기 조정하고 플롯 보여주기
plt.grid(True)
plt.legend(prop={'size': 6})
plt.show()
