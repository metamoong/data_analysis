# csv 파일에서 읽은 도시들의 위도, 경도값을 가지고 basemap 을 이용해 우리나라 지도에 도시를 표시하는 프로그램
# 데이터를 가공한 후 문제에서 보이는 것처럼 위도, 경도를 이용해 12개의 구간으로 나눈 후 각 구간에 맞는 숫자를 반환하는 함수를 만들었다.
# 그리고 그 함수와 colormap을 이용해 각 구간에 맞게 글씨의 색이 바뀌도록 했다.

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.cm as cm


data = np.loadtxt('problem04_data.csv', dtype='str', delimiter=',')

# csv파일에서 읽은 데이터를 city, longtitude, latitude로 나누고 원하는 데이터 타입(float)으로 변환
city = data[:, 0][1:]
longtitude = data[:, 1][1:]
longtitude = list(map(float, longtitude))
latitude = data[:, 2][1:]
latitude = list(map(float, latitude))


plt.figure(figsize=(7, 7))

# basemap과 대한민국의 위도, 경도를 이용해 지도 그리기
map = Basemap(projection='merc', urcrnrlat=39, llcrnrlat=34,
              llcrnrlon=126, urcrnrlon=130)

# 위도, 경도를 맵의 좌표계로 변환하고 위치를 마커로 나타내기
x, y = map(longtitude, latitude)
map.scatter(x, y, 25, marker='o', zorder=10, color='r')


longtitude_line = np.linspace(34, 39, 4)  # 그림에서 보이는 것 처럼 3구간으로 분할하기 위해 4개로 나눔
latitude_line = np.linspace(126, 130, 5)  # 그림에서 보이는 것 처럼 4구간으로 분할하기 위해 5개로 나눔


# colormap 함수 : paired 컬러맵에 따른 색 반환 / 파라미터 k : 0~11사이의 정수
def colormap(k): return cm.Paired(k)


# location 함수 : 나눈 구역에 따라 적당한 정수 반환 / 파라미터 a :latitude 값 b:longtitude 값
def location(a, b):
    if a >= longtitude_line[0] and a < longtitude_line[1]:
        if b >= latitude_line[0] and b < latitude_line[1]:
            return 0
        elif b >= latitude_line[1] and b < latitude_line[2]:
            return 1
        elif b >= latitude_line[2] and b < latitude_line[3]:
            return 2
        else:
            return 3

    elif (a >= longtitude_line[1] and a < longtitude_line[2]):
        if b >= latitude_line[0] and b < latitude_line[1]:
            return 4
        elif b >= latitude_line[1] and b < latitude_line[2]:
            return 5
        elif b >= latitude_line[2] and b < latitude_line[3]:
            return 6
        else:
            return 7

    else:
        if b >= latitude_line[0] and b < latitude_line[1]:
            return 8
        elif b >= latitude_line[1] and b < latitude_line[2]:
            return 9
        elif b >= latitude_line[2] and b < latitude_line[3]:
            return 10
        else:
            return 11


labels = city
for label, xpt, ypt, a, b in zip(labels, x, y, longtitude, latitude):
    plt.text(xpt, ypt, label, color=colormap(location(b, a)))


# 지도 그리기/ 색 등 지정
map.drawcoastlines()
map.drawcountries()
map.fillcontinents(color='white')
map.drawmapboundary(fill_color='aqua')

map.drawparallels(longtitude_line)
map.drawmeridians(latitude_line)

plt.title('Cities in South Korea')
plt.show()
