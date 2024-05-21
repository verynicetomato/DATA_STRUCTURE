# 스택: 마지막에 들어간 자료가 가장 먼저 나오는 자료구조
# LIFO: Last-In-First-Out(다른 위치에서 삽입과 삭제 X)
# 스택의 활용 예: 웹 브라우저의 이전 페이지로 이동
# 스택은 숫자와 문자열을 포함한 어떤 자료든지 저장할 수 있음(큐나 트리와 같은 다른 자료구조들도 마찬가지)
# 자료구조를 구현하는 방법은 크게 배열 구조와 연결된 구조로 나눌 수 있음
# 자료구조는 함수를 기반으로 하는 절차적 프로그래밍보다는 클래스를 기반으로 하는 객체 지향 프로그램 기법을 이용해 구현하는 것이 훨씬 좋음

'''
스택의 연산
push(e): 새로운 요소 e를 스택의 맨 위에 추가
pop(): 스택의 맨 위에 있는 요소를 꺼내서 반환
isEmpty(): 스택이 비어 있으면 True를, 아니면 False를 반환
isFull(): 스택이 가득 차있으면 True를, 아니면 False를 반환
peek(): 스택의 맨 위에 있는 항목을 삭제하기 않고 반환
size(): 스택에 들어 있는 전체 요소의 수를 반환
'''

# 스택을 위한 데이터
capacity = 10 # 스택 용량을 10으로 지정
array = [None] * capacity # 요소 배열: [None, ..., None] (길이가 capacity)
top = -1 # 상단의 인덱스: 공백상태(-1)로 초기화 함

# 스택의 공백상태와 포화상태 검사
def isEmpty( ):
    if top == -1 : return True # 공백이면 True 반환
    else: return False # 아니면 False 반환

def isFull( ): return top == capacity - 1 # 비교 연산 결과를 바로 반환

# 스택의 삽입 연산
def push(e):
    global top
    if not isFull(): # 포화상태가 아닌 경우
        top += 1 # top 증가(global top 선언 필요)
        array[top] = e
    else: # 포화상태: overflow 
        print("stack overflow")
        exit()

# 스택의 삭제 연산
def pop( ):
    global top
    if not isEmpty(): # 공백상태가 아닌 경우
        top -= 1 # top 감소(global top 선언 필요)
        return array[top + 1]
    else: # 공백상태: underflow 
        print("stack underflow")
        exit()

# 스택의 peek() 연산
def peek( ):
    if not isEmpty(): # 공백상태가 아닌 경우
        return array[top]
    else: pass # underflow 예외는 처리하지 않았음

# 스택의 size() 연산
def size( ): return top + 1 # 현재 요소의 수는 top+1


# 이 파일이 직접 실행될 때에는 다음 문장들을 실행함
# 다른 파일에서 모듈로 불려지는 경우는 실행되지 않음

if __name__ == "__main__":
    msg = input("문자열 입력: ")   # 문자열을 입력받음
    for c in msg:                # 문자열의 각 문자 c에 대해
        push(c)                   # c를 스택에 삽입

    print("문자열 출력: ", end='')
    while not isEmpty():          # 스택이 공백상태가 아니라면
        print(pop(), end='')      # 하나의 요소를 꺼내서 출력
    print()


