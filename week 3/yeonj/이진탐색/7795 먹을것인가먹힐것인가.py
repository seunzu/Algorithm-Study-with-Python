for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
 
    a.sort()
    b.sort()
    count=0 
    for target in a:
        start = 0
        end = m - 1  
        res = -1     
        #이진탐색
        while start <= end:
            mid = (start + end) // 2            
            if target <= b[mid]:
                end = mid - 1
            elif target > b[mid]:
                res = mid            
                start = mid + 1
                
        count += (res+1)               
    
    print(count)                  