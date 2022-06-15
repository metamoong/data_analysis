# args로 파일 또는 폴더와 변환하고자하는 파일 형식을 받아 그 형식으로 바꾸는 프로그램
# sys 모듈을 이용해 args 에 접근하여 그 값에 따라 파일들의 형식을 변환하도록 했다.
# args에 들어온 값이 폴더인지 파일인지를 나눠서 폴더인 경우에는 폴더안의 파일들을 순회하면서 하나씩 형식을 변환한다.

from PIL import Image
import sys
import os


# launch.json의 args의 첫번째, 두번째 값 넣어주기
folder = sys.argv[1]
type = sys.argv[2]


if os.path.isdir(folder):
    files = os.listdir(folder)  # 폴더 안의 파일 리스트
    for file in files:
        im = Image.open(folder+'/'+file).convert('RGB')  # 이미지 모드를 RGB로
        filename, filetype = os.path.splitext(file)  # 파일명 과 파일 형식 분리
        im.save(filename+'.'+type, type)  # 파일을 원하는 형식으로 변환하여 저장
else:
    im = Image.open(folder).convert('RGB')  # 위의 설명과 동일
    filename, filetype = os.path.splitext(folder)
    im.save(filename+'.'+type, type)
