# 배열을 사용한 방법
n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
result = []
for i in range(n):
    result.append(min(arr[i]))

print(max(result))

# 배열을 사용하지 않는 방법
n, m = map(int, input().split())

result = 0
for i in range(n):
    nums = list(map(int, input().split()))
    min_n = min(nums)
    result = max(result, min_n)

print(result)