def say_hello(n):
    for i in range(n):
        print("hello!")

if __name__ == "__main__":
    print("my.py를 직접 실행 할때만 출력되는 문구")
else:
    print(f"{__name__}.py is imported!")