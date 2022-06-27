import heapq
import sys

heap=[]
max_heap=[]
num=sys.stdin.readline()
for i in range(num):
    n=int(sys.stdin.readline())
    if n!=0:
        heapq.heappush(heap,n)
        heapq.heappush(max_heap, (-item, item))
    else: