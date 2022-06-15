import requests
import matplotlib.pyplot as plt


url = 'http://221.143.21.56:15695/dataAnalysisAndVisualization/midtermExam/0659315053997499/getData01.do'

# url에서 데이터를 가져와 json형태로 변환
data = requests.post(url)
data_json = data.json()

# 필요한 데이터 나누기
lang = data_json['languages']
popularities = data_json['popularities']

# 각 요소 색깔 설정, 간격 설정
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
explode = [0.1, 0, 0, 0, 0, 0]  # java만 튀어나온 형태가 되게 하기 위함


# 파이차트 그리기 (90도에서 java가 시작하게, 순서대로 시계방향으로 되게 설정, 영역비율 퍼센트 지정, 그림자 그리기)
plt.pie(popularities, explode=explode, labels=lang,
        autopct='%1.1f%%', startangle=90, shadow=True, colors=colors, counterclock=False, textprops={'fontsize': 8}
        )

# 제목 만들고 bbox 문제처럼 조정 (bbox padding 과 색깔 지정)
plt.title(
    'Popularity of Programming Language\nWorldwide, Oct 2017 compared to a year ago', fontsize=9,
    bbox={'facecolor': (0.8, 0.8, 0.8), 'pad': 5})

plt.show()
