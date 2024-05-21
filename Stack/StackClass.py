# 스택 클래스의 정의와 생성자 함수
class ArrayStack :
    def __init__(self, capacity): # 생성자 정의(생성자: 클래스의 객체가 만들어질 때마다 자동으로 호출되는 함수)
        self.capacity = capacity # 용량(고정)
        self.array = [None] * self.capacity	# 요소들을 저장할 배열
        self.top = -1 # 스택 상단의 인덱스

    # 스택 클래스의 연산들
    def isEmpty(self) : return self.top == -1
    def isFull(self) : return self.top == self.capacity - 1

    def push(self, item):
        if not self.isFull() :
            self.top += 1
            self.array[self.top] = item
        else: pass # overflow 예외는 처리하지 않았음

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top + 1]
        else: pass # underflow 예외는 처리하지 않았음

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else: pass # underflow 예외는 처리하지 않았음

    def size(self) : return self.top + 1


# 스택 클래스의 사용: 문자열 역순 출력 프로그램
# 이 파일이 직접 실행될 때에는 다음 문장들을 실행함
# 다른 파일에서 모듈로 불려지는 경우는 실행되지 않음

if __name__ == "__main__":
    s = ArrayStack(100) # 스택 객체를 생성

    msg = input("문자열 입력: ") # 문자열을 입력받음
    for c in msg: # 문자열의 각 문자 c에 대해
        s.push(c) # c를 스택에 삽입

    print("문자열 출력: ", end='')
    while not s.isEmpty():  # 스택이 공백상태가 아니라면
        print(s.pop(), end='') # 하나의 요소를 꺼내서 출력
    print()

