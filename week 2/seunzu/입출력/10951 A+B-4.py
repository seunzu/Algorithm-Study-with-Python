while True:
    try: # 예외처리
        a, b = map(int, input().split())
        print(a + b)
    except:
        break