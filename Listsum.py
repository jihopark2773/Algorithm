def listsum(n, S):
  result = 0
  for i in range(1,n+1):
    result = result + S[i]
  return result

## Test Case1
n = 6
S = [-1, 10, 7, 11, 5, 13, 8]
listsum(n, S)
