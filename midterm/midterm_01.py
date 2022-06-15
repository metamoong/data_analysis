import numpy as np
import matplotlib.pyplot as plt
import imageio

# 이미지 읽고 rgb 성분을 나누기 위해 3열로 데이터 가공
img = imageio.imread('problem01.jpg')
reshapeImg = img.reshape(-1, 3)

# 이미지의 rgb 성분을 각각 나누기
red = reshapeImg[:, 0]
green = reshapeImg[:, 1]
blue = reshapeImg[:, 2]

# 사진 (왼쪽 위 plot)
plt.subplot(221)
plt.title('Image', fontsize=7, fontweight='bold')  # 제목 지정, 폰트 사이즈와 굵기 지정
plt.xticks(np.arange(0, 1200, step=200), fontsize=6)  # x축 표시할 값 지정, 폰트 사이즈 조절
plt.yticks(np.arange(0, 800, step=100), fontsize=6)  # y축 표시할 값 지정, 폰트 사이즈 조절
plt.imshow(img)  # 이미지 plot에 표시

# 축의 최솟값, 최댓값, 표시 할 x축 값 정하기
minmax = [0, 255, 0.00, 0.05]
x = [0, 50, 100, 150, 200, 255]


# red channel (오른쪽 위 plot)
plt.subplot(222)  # 2X2 중 2번째
plt.title('Red channel', fontsize=7, fontweight='bold')  # 제목 붙이고 폰트사이즈와 굵기 조절
plt.axis(minmax)  # x축 y축 최대, 최솟값 지정
plt.xticks(x, fontsize=6)  # x축 표시할 값 지정, 폰트 사이즈 조절
plt.yticks(fontsize=6)  # y축 표시할 값 지정, 폰트 사이즈 조절
plt.grid(True, axis='y')  # 가로 격자만 표시하기
# 히스토그램 가로축 개수, 확률 밀도로 나타내기, 색깔 지정
plt.hist(red, color='r', bins=255, density=True)

# green channel (왼쪽 아래 plot)
plt.subplot(223)
plt.title('Green channel', fontsize=7, fontweight='bold')
plt.axis(minmax)
plt.xticks(x, fontsize=6)
plt.yticks(fontsize=6)
plt.grid(True, axis='y')
plt.hist(green, color='g', bins=255, density=True)


# blue channel (오른쪽 아래 plot)
plt.subplot(224)
plt.title('Blue channel', fontsize=7, fontweight='bold')
plt.axis(minmax)
plt.xticks(x, fontsize=6)
plt.yticks(fontsize=6)
plt.grid(True, axis='y')
plt.hist(blue, color='b', bins=255, density=True)


plt.show()
