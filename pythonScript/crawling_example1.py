import requests
from bs4 import BeautifulSoup

#호출 url 정의
url = 'http://www.daum.net'
#url 호출
res = requests.get(url)
#html 형식으로 인식
soup = BeautifulSoup(res.content, 'html.parser')
#a 태그 href가 http로 시작하는 대상 추출
links = soup.select('a[href^=http]')
#href 정보만 담음
for i in range(len(links)):
    links[i] = links[i]['href']

#url이 긴 순으로 10개만 추출
top10 = sorted(links, key=len, reverse=True)[:10]
#응답시간 정렬을 위한 dictionary 준비
result_dic={}

for result in top10:
    #길이 순서대로 출력
    print(len(result), result)
    response = requests.get(result)    
    #dictionary에 url과 응답시간을 key:value쌍으로 저장
    result_dic[result] = response.elapsed.total_seconds()

print()
#응답시간 순서로 출력
for key, value in sorted(result_dic.items(), key=lambda t : t[1]):
    print(value, key)




