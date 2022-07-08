def solution(array):
  maxSequence = 0
  counter = 0
  for i in array:
    if i == 1:
      counter += 1
      if counter > maxSequence:
        maxSequence = counter
    else:
      counter = 0
  return maxSequence
