def seqsearch(n, S, x):
  location = 1
  while (location <= n and S[location] != x):
    location += 1
  if (location > n):
    location = 0
  return location

seqsearch(5, [1,2,3,4,5], 5)
