# txt로 하려면.
workFile = open('homework.txt', 'w', encoding='utf-8')
workFile.write('삼성전자,카카오,네이버,다음')
workFile.close()
# workFile = open('homework.csv', 'w')
# workFile.write('삼성전자', '\n카카오', '\n네이버', '\n다음') 이거 틀림 ㄷㄷㄷ

# CSV 파일로 저장
# with open('homework.csv', 'w', encoding='utf-8') as workFile:
#     workFile.write('삼성전자')
#     workFile.write('\n카카오')
#     workFile.write('\n네이버')
#     workFile.write('\n다음')
# workFile.close()

workFile2 = open('homework.csv', 'w', encoding='utf-8')
workFile2.write('삼성전자')
workFile2.write('\n카카오')
workFile2.write('\n네이버')
workFile2.write('\n다음')
workFile2.close()

# workFile = open('homework.csv', 'w')
# workFile.write('삼성전자', '\n카카오', '\n네이버', '\n다음') 이거 틀림 ㄷㄷㄷ

# 예시답안
리스트 = ['삼성전자', '카카오', '네이버', '다음']

f = open('b.txt', 'w')
f.write( 리스트[0] + '\n')
f.write( 리스트[1] + '\n')
f.write( 리스트[2] + '\n')
f.write( 리스트[3] + '\n')
f.close()


# 예시답안2 : 반복문 사용
리스트 = ['삼성전자', '카카오', '네이버', '다음']

f = open('c.txt', 'w')
for i in 리스트:
    f.write(i + '\n')
f.close()


# 예시답안3 : 반복문 사용 - 또 다른 형태
리스트 = ['삼성전자', '카카오', '네이버', '다음']

f = open('d.txt', 'w', encoding='utf-8')
for i in range(len(리스트)):
    f.write(리스트[i] + '\n')
f.close()

# 예시답안4 : 반복문 사용 - 또 다른 형태 3
f = open('e.txt', 'w', encoding='utf-8')
for i in range(0, 4):
    f.write(리스트[i] + '\n')
f.close()

# 과제 2 : 구구단 9단까지 출력
print(2)
print(2*2)
print(2*3)
print(2*4)
print(2*5)
print(2*6)
print(2*7)
print(2*8)

# 이거를 우선 반복문으로 축약
for i in range(1, 10):
    print(2*i)
    # 이게 2단

print('\n3단')
for i in range(1, 10):
    print(3*i)
    # 이게 3단

print('--------------------------------')
# 이걸 9단까지 반복
# 구구단은 2중 반복문

# 1. 무식하게 1~9단이 일렬로 출력되는 코드
for i in range(1, 10):
    for j in range(1, 10):
        print(i*j)

print('\n--------------------------------')

# 2. i X j = 계산값 이렇게 출력되는 코드
for i in range(2, 10):
    print('\n' + str(i) + '단')
    for j in range(1, 10):
        print(str(i) + ' x ' + str(j) + ' = ' + str(i*j))

print('\n--------------------------------')

# 3. f-string으로 정리한 코드
for i in range(2, 10):
    print(f'\n{i}단')
    for j in range(1, 10):
        print(f'{i} x {j} = {i*j}')