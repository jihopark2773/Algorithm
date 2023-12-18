def seqsearch(n, S, x):
  location = 1
  while (location <= n and S[location] != x):
    location += 1
  if (location > n):
    location = 0
  return location

## Test Case1
seqsearch(5, [1,2,3,4,5], 5)

## Test Case2
S = [1, 11, 13, 14, 15]
x = 14
seqsearch(len(S)-1, S, x)
