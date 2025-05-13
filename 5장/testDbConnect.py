import pymysql

#데이터 베이스 접속 관련 변수 초기화
host = "localhost"
port = 3306
database = "madangdb"
username = "madang"
password = "madang"

#접속 상태 확인
conflag=True

try:
    print ('데이터베이스 연결 준비..')
    conn = pymysql.connect(host=host, user=username, passwd=password, db=database, port=port,charset='utf8')
    print ('데이터베이스 연결 성공')
except Exception as e:
    print ('데이터베이스 연결 실패')
    conflag=False
#접속이 성공하면 실행
if conflag== True :
    #커서 생성
    cursor = conn.cursor()

    #SQL 문장 준비
    sqlstring = 'select * from book;'

    #SQL 문장실행
    res = cursor.execute(sqlstring)

    #쿼리 데이터를 가져옴
    data = cursor.fetchall()

    #화면에 출력 
    print ('{0}\t{1:<} \t{2:<} \t{3:>}'.format('BOOK NO','BOOK NAME','PUBLISHER','PRICE'))
    for rowdata in data:
        print ('{0}\t{1:<} \t{2:<} \t{3:>}'.format(rowdata[0],rowdata[1],rowdata[2],rowdata[3]))

    #커서를 닫음
    cursor.close()

    #데이터베이스 연결을 닫음
    conn.close()

