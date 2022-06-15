# x , y, z를 이용해 3차원 도표를 그리는 프로그램
# x값을 먼저 만들고 z값을 구한 후에 projection = '3d'와 plot_surface를 사용해 3차원으로 나타냄

import numpy as np
import matplotlib.pyplot as plt
import matplotlib


x = np.linspace(1, -1, 100)  # 1~-1 를 같은 간격으로 100개로 나눔
y = np.linspace(1, -1, 100)
x1, y1 = np.meshgrid(x, y)  # x,y 의 좌표를 이용해 2차원 그리드 좌표 생성

z = (np.sign(-0.65-x1) + np.sign(-0.35-x1) +
     np.sign(-0.05-x1) + np.sign(0.25-x1) + np.sign(0.55-x1)) / 7

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


graph = ax.plot_surface(x1, y1, z, rstride=4, cstride=4,
                        cmap=matplotlib.cm.Set1, linewidth=0.4, antialiased=True)


fig.colorbar(graph, shrink=0.5, aspect=5,
             ticks=np.arange(-0.6, 0.8, 0.2))

ax.set_xlabel('x')
ax.set_ylabel('y')

for i in range(6):  # 적당한 위치에 text가 표시되도록 조절함
    index = 0 + 100//6*i
    ax.text(0.75-0.35*i, -0.2, -0.6+0.25*i,
            f'{i+1}F', fontsize=15, color='b')
plt.show()
