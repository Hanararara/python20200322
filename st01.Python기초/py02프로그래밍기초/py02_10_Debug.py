# py02_10_Debug.py

# 버그(bug) : 프로그램이 원하지 않는 방향으로 동작하는 것
# 디버그(debug) : 버그를 잡는 행위

# breakpoint 지정  <-- 빨간점. stop 위치 지정
# F5  : 디버깅 시작
# F10 : 한 줄씩 이동
# F11 : 함수 안으로 이동

# visual studio code에 디버깅 설정하는 방법을 배운다.
# 디버깅 시작하는 방법을 배운다.
# 단계별 디버깅 방법을 배운다.
# watch에 변수 등록하는 방법을 배운다. 

# x값의 변화 관찰
 # 첫번째 방법 :  마우스를 변수 위에 올림
 # 두번째 방법 : watch에 변수를 등록

x = 100
x=x+1 #101
x=x+1 #102
print("x=", x) # x=102