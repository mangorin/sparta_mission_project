#print('hello 정아') #프린트는 개발자가 보라고 만들어 놓은 것

###들어가기 전###
#실행시에는 반드시 오른쪽 키를 누르고 실행할것, 아래의 초록 버튼을 누르면 다른 파일이 실행 될 가능성이 있음.
#파이썬도 모든 걸 다 알 순 없다. 따라서 구글링 하면 된다.
#자바보다 훨씬 직관적

#변수, 자료형, 함수, 조건문, 반복문

###1.변수
#자바는 변수 앞에 let을 붙였어야함

#first_name = 'Jeong ah'
#last_name = 'Seong'
#num = 2

#print(first_name+num)

# 에러보는 법:
# 에러의 가장 마지막 줄-에러가 난 이유
# 에러 마지막 줄의 윗줄-에러가 발생 한 위치
# 에러가 난 이유를 구글링을 통해 이유를 파악 할 수 있다. 대부분 나와 있음

#a_list = ['사과', '배', '감']

#print(a_list[1])

#리스트에 요소를 추가하는 방법: append()
#a_list.append('수박')

##############3딕셔너리
#a_dict = {'name':'bob', 'age':'27'}
#print(a_dict['age'])
#a_dict['height']=178 #추가

################함수
#java에서는 function
#파이썬에서는 알아서 다음 줄맞춤으로 넘어가고, 중괄호를 사용하지 않는다.
#def sum(num1, num2):
#   print('안녕!')
#    return num1+num2

#result = sum(2, 3)
#print(result)



#######################3조건문
age = 25

if age > 20:
    print('성인입니다.')
else:
    print('청소년입니다.')


def is_adult(age):
    if age > 20:
        print('성인입니다.')
    else:
        print('청소년입니다.')

is_adult(30)
is_adult(15)

##################3반복문
#list의 반복문을 하나씩 빼서 쓴다는 느낌

fruits = ['사과', '배', '배', '감', '수박', '귤', '딸기', '사과', '베', '수박']

count=0
for fruit in fruits: #하나씩 돌면서 빼는 느낌
    if fruit == '배':
        count +=1

print(count)

#딕셔너리 예제
people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

for person in people:
    if person['age'] < 20:
        print(person)