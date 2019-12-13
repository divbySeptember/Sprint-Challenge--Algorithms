#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I
a) The time complexity of this is O(n) or linear because as the variable n increases, the runtime also increases at the same rate.

b) Because of the nested for loop, the time complexity of this is O(n^2), and will work with smaller n values, but will take siginicantly more time as n grows in value.

c) This algorithm is also O(n) because the runtime will increase proportionally to the value of n.

## Exercise II


Select a floor in the middle to start (len(arr)//2) and throw the egg off to see if it breaks.
If the egg breaks, use the half with smaller numbers to move on; if it doesn't, use the larger half.
Continue to half the results until the remaining results include just two floors.
Out of those two floors, determine which floor the egg would break on, and which it wouldn't.
Because we're using binary search, the time complexity is log(n).