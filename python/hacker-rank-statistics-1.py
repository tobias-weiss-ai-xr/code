#!/usr/bin/env python3

str = '64630 11735 14216 99233 14470 4978 73429 38120 51135 67060'
arr = sorted(list(map(int, str.split(' '))))
n = len(arr)
agg = 0.0
cnt = {}
for ele in arr:
    agg += ele
    if ele in cnt:
        cnt[ele] += 1
    else:
        cnt[ele] = 1
# mean
print('{:.1f}'.format(agg/n))
# median
if n % 2 == 0:
    median = (arr[(n-1)//2]+arr[((n-1)//2)+1])/2
else:
    median = arr[len(arr)//2]
print('{:.1f}'.format(median))
# mode
print('{:d}'.format(max(cnt, key=cnt.get)))

