nums = [1,2,3,4]
res = []
S = 0
for ele in nums:
    S += ele
    res.append(S)
print(res) 

ans = []
for i in range(1,len(nums)+1):
    ans.append(sum(nums[:i]))
print(ans)

res1 = [sum(nums[:i]) for i in range(1, len(nums)+1)]
print(res1)