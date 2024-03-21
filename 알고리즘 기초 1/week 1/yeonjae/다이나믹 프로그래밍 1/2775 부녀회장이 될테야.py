t = int(input())  # 테스트 케이스의 수

for _ in range(t):
    k = int(input())  # 층 수
    n = int(input())  # 호 수
    
    # 0층 리스트 초기화
    residents = [i for i in range(1, n+1)]    
    # k층
    for _ in range(k):
        for j in range(1, n):
            residents[j] += residents[j-1]
    
    print(residents[-1])  # 가장 마지막 호수 출력
