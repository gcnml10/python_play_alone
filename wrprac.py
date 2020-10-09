from wordcloud import WordCloud
from PIL import Image
import numpy as np

text=''
with open("KakaoTalk_group2.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        if '] [' in line:
            text += line.split('] ')[2].replace('ㅋ','').replace('그거','').replace('이제','').replace('그냥','').replace('너무','').replace('그럼','').replace('내가','').replace('아니','').replace('민수','').replace('진짜','').replace('오늘','').replace('샵검색','').replace('ㅎ','').replace('근데','').replace('나도','').replace('ㅠ','').replace('ㅜ','').replace('ㅇ','').replace('이모티콘\n','').replace('사진\n','').replace('삭제된 메세지 입니다','')

print(text)

mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path='C:/Users/user/AppData/Local/Microsoft/Windows/Fonts/NanumGothic.ttf', background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked2.png")