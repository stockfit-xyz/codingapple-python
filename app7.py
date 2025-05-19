# 파일 입출력 예제
# 엑셀 형식으로 파일 만들기
# 더 쉬운 .csv 파일 형식으로 만들어서 저장

testFile = open('a.csv', 'w')
testFile.write('이름, 나이, 성별\n') # 개행 함.
testFile.write('홍길동, 20, 남자\n')
testFile.write('오쌤, 40, 남자\n')
testFile.close
