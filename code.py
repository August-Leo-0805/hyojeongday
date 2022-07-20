import streamlit as st
import time

a1=[]
a2=[]

answer1=['바나나 알러지 원숭이', 'You & I', '길', '2% 채워주는 자두','우린 제법 잘 어울려요', 
         'Say It To Me', '선생님 사랑해요', '오늘도 어제처럼', 'SNS', '사르르']
answer2=['오마이걸 반하나', '효정, 유빈', '효정', '효정', '효정', 
         '효정, 유아, 지호', '효정, 미미, 유빈', '효정', '박명수, 효정', '효정']

lyrics=['ㄱㄹ ㄴㅇㄹ ㅂㅈㄴ ㅁㅇ', 'ㄲㅇㄴ ㅇ ㅅ ㅇㄴ ㄴㅇㅇ ㅎㄲㄹㅁ ㅁㄷ ㄱ ㅎ ㅅ ㅇㅇ', 'ㄴㅇㄹ ㅎㅇ ㄷ ㄱㄹ ㄱ ㅈ ㅇㄷㄱ ㅂ ㅇㄷㄹ', 'ㅅㅋ ㅈㄷㅈㄷㅈㄷ', 'ㅈㅁ ㅅㄷㄹㅈ ㅇㅇ ㄱㅇㅇ',
         'ㅆㅇㅈㄴ ㅂㅉㅇ ㅅ ㄴ ㅂ', 'ㄴㅇ ㅊ ㅅㄹ ㄴㅁ ㅅㅈㅎ', 'ㅇㅈ ㅂㄷ ㄱㄷㄹ ㅅㄹㅎㅈ', 'ㄴ ㅅㄹ ㅂㅇㅈㅇ ㅁㄹㄴ ㅇ ㅎ ㄱ', 'ㅇ ㅇㄹㄲ ㄴㅁ ㅂㅁ ㄴㅇㅇ ㅅㄹㅇㄱ ㅎㄴㅇ ㅂㄱ ㄷㅇ']

name=input('이름 : ')

print('다음 초성을 보고, 노래 제목과 가수를 맞추시오.')

for i in range (10) :
    print(i+1, '번')
    print(lyrics[i])
    ans1=input('제목 : ')
    a1. append(ans1)
    ans2=input('가수 : ')
    a2. append(ans2)
    print('')

time.sleep(0.5)

s1=0
s2=0
for i in range (10) :
    if a1[i]==answer1[i] :
        s1=s1+1
    if a2[i]==answer2[i] :
        s2=s2+1

if  s1==10 and s2==10 : 
    print('축하합니다')
    print(name, '너는 만점 이다.')

else :
    print(name, '너는', s1+s2, '점을 얻었다.')
