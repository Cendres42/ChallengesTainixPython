import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = 5  # the number of temperatures to analyse

result=0
resultP=6000
resultM=-374
for i in range(5):
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(input())
    if t<0 and t>resultM:
        resultM=t
    if t>0 and t<resultP:
        resultP=t
if n==0:
    result=0
elif resultP==abs(resultM):
    result=resultP
elif resultP>abs(resultM):
    result=resultM
else: 
    result=resultP


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(result)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


