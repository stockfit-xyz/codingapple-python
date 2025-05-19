# 파이썬으로 파일 입출력
# 파일 입출력은 파일을 읽거나 쓰거나 하는 것을 의미합니다.

# 파일 열기기
# open('경로(파일이름)', 'w')
# 파일이름은 파일의 이름을 적어주고, w는 쓰기 모드입니다.
testFile = open('a.txt', 'w')

# 파일 쓰기
testFile.write('안녕하세요')

# 파일 닫기
testFile.close()

# 파일 추가 쓰기
testFile = open('a.txt', 'a')
testFile.write('반갑습니다')
testFile.close()
# append 모드는 파일이 없으면 생성하고, 있으면 파일 끝에 추가합니다. 갈아치우는 게 아님님
# 안녕하세요반갑습니다 이렇게 출력됨

# 만약 줄바꿈을 하고 싶다면?
testFile = open('a.txt', 'a')
testFile.write('\n진짜로 매우매우 반갑습니다')
testFile.close()
# 이렇게 줄바꿈을 하고 싶다면 줄바꿈 문자를 넣어주면 됩니다.
# 줄바꿈 문자는 \n 입니다.
# 안녕하세요반갑습니다
# 진짜로 매우매우 반갑습니다 이렇게 출력됨.

# 파일 읽기
testFile = open('a.txt', 'r') # 파일을 read 모드로 열기 : open('파일이름(경로로)', 'r')
print(testFile.read()) # 파일 내용 출력 : 파일 내용을 읽어오는 함수
# testFile.read() 이렇게 쓰면 파일 내용을 모두 읽어오고, 파일 포인터는 파일 끝에 있게 됩니다.

# 파일 닫기
testFile.close()

# 위에서 보면 a.txt는 덮어쓰기됨(재생성 반복)
# 파일 쓰기 모드는 파일이 없으면 생성하고, 있으면 덮어쓰기합니다.
