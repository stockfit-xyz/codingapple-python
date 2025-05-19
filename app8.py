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
