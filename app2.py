중고차 = ['K5', 'white', 5000] # 한 변수에서 여러 개 선언 가능
중고차[1] = 'black'
print(중고차)
print(중고차[1]) # 중고차[1] = 'black' 이라고 하면 중고차[1] 의 값이 black 으로 변경됨

# 중고차2 = {'BMW', 'black', 10000}  # 잘못된 형식 (집합)
중고차2 = {'brand': 'BMW', 'color': 'black', 'price': 10000}  # 딕셔너리 형식
print(중고차2['brand'])

중고차2['brand'] = 'Benz' # 딕셔너리 값 수정
print(중고차2['brand']) # Benz 출력

