input = 'ABCDCDC'
sub ='CDC'
count = 0
a = len(input)
for i in range(0,len(input)):
   if input[i:i+len(sub)]==sub:
       count += 1

print(count)