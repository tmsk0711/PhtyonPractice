# print(5)
# print(3.14)
# print(10000000000000)
# print('풍선')
# print('풍선 '*2)
# print(not False)

# animal = "dog"
# name = "alex"
# age = 4
# hobby = "walk"
# is_adult = age >= 3
# print("my " + animal + " name is" + name)
# print(name, "age is", age , hobby)
 
# station = "사당"
# station_is = "행 열차가 들어오고 있습니다."

# print(station, station_is)
# print(2.5**3)
# print(10//3)
# print(10%3)

# print((3>0) & (3<5))

# print((3>0) | (3<5))
# number = 16
# print(number)
# number *= 2
# print(number)
# number /= 2
# print(number)
# number %= 2
# print(number)


# print(abs(-5))
# print(pow(4,4))

# from math import *
# from random import *
# print(floor(4.99))
# print(ceil(3.14))
# print(sqrt(256))

# print(random()) # 0.0 ~1.0 미만

# print(int(random()*10)) # 0~10 미만

# print(int(random()*10)+1) # 1~10 이하

# print(randrange(1,46)) # 1~46 미만 

# print(randint(1,45)) # 1~45 이하

# day = randint(4, 28)

# # day_is = "오프라인 스터디 모임 날짜는 매월 ",day"일로 선정되었습니다."
# print("오프라인 스터디 모임 날짜는 매월" + str(day) + "일로 선정되었습니다.")

# sentence3="""
# 나는 소년이고
# 파이썬 사랑
# """
# print(sentence3)

jumin = "940711-1234567"

print("성별 : "+jumin[7])
print("연 : "+jumin[0:2])  # 0부터 2직전까지 ex(0~1)
print("월 : "+jumin[2:4])
print("일 : "+jumin[4:6])

print("생년월일 : "+jumin[:6]) # 처음부터 6직전까지 ex(0~5)
print("뒤7자리 : "+jumin[7:]) # 7부터 끝까지 
print("뒤7자리(뒤에부터) : "+jumin[-7:]) # 맨뒤에서 7번째부터 끝까지 

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) # True
print(len(python)) # 17
print(python.replace("Python","Java"))

print(python.find("n")) # 5
print(python.find("Java")) # -1
# print(python.index("Java")) # ERROR
print(python.count("n")) # 2

# 문자열 포맷

print("나는 %d살입니다." % 20) #d는 정수의미
print("나는 %s을 좋아해요." % "파이썬") #s 문자열 의미
print("Apple 은 %c로 시작해요." % "A") # 한글자
print("나는 %s색과 %s색을 좋아해요." %("파란","빨간"))

print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란","빨간"))

print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20 , color = "red"))

age = 20
color = "red"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 탈출 문자
# \n : 줄바꿈
print("사랑\n하자")
# \
print("우리 \"사랑하자\" ")
#\\ 문장내에서 \ ex(경로)
print("C:\\Users\\82108\\Desktop\\PhytonWorkSpace")
# \r 커서 맨앞 이동
# \b 백스페이스 (한 글자 삭제)
# \t 탭
print("red \t apple")

# 사이트별 비밀번호
# 규칙1 : http://부분 제외 => naver.com
# 규칙 2: 처음 만나는점(.) 이후 부분 제외 => naver
# 규칙 3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자내 'e'갯수 + "!"로 구성

url = "http://youtube.com"
site = url[7:]
site = site[:-4]
site_first = site[0:3]
site_second = len(site) 
site_eNum = site.count("e")
print(str(site_first)+str(site_second)+str(site_eNum)+"!")

url = "http://youtube.com"
my_str = url.replace("http://", "") 
my_str = my_str[:my_str.index(".")]
# print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다.".format(url, password))

