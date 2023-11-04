import sys
import heapq
heap = []
n = int(sys.stdin.readline().strip())
for i in range(n):
    scan = int(sys.stdin.readline().strip())
    if scan == 0:
        if len(heap) < 1:
            print("0")
        else:print(heapq.heappop(heap))
        
    else: heapq.heappush(heap,scan)