import matplotlib.pyplot as plt
import numpy as np

# 문제에서 주어진 데이터
step = 500
mu = 0.002
sigma = 0.01

# 데이터 만들기
data = np.random.normal(mu, sigma, 500).cumsum()
x = np.arange(0, 500, 1)
lowerBound = mu * x - sigma * np.sqrt(x)
upperBound = mu*x + sigma * np.sqrt(x)

# 그래프 그리기
plt.plot(x, data, color='red', label='Walker position')
plt.plot(x, lowerBound, linestyle='none')
plt.plot(x, upperBound, linestyle='none')
plt.plot(x, (lowerBound+upperBound)/2, color='black',
         linestyle='dashed', label='Population mean')  # 평균 선 그리기, 줄 스타일을 - 로

plt.fill_between(x, lowerBound, upperBound,
                 facecolor='#FDFD96', label='1 sigma range')  # lowerBound와 upperBound 사이 채우기
plt.fill_between(x, upperBound, data, where=data > upperBound, facecolor='darkblue',
                 interpolate=True)  # 범위 벗어나서 큰 경우 darkblue로 채우기
plt.fill_between(x, lowerBound, data, where=data < lowerBound, facecolor='green',
                 interpolate=True)  # 범위 벗어나서 작은 경우 green으로 채우기


# x축 표현할 값 지정
plt.xticks(np.arange(0, 600, step=100))
plt.xlim(0, 500)

# x축, y축 라벨 지정
plt.xlabel('The number of steps', fontsize=10)
plt.ylabel('Position', fontsize=10)

# 그리드 보이기, 범례 표시하고 그래프 보이기
plt.grid(True)
plt.legend()
plt.show()
