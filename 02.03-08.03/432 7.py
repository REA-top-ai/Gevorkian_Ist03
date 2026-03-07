a = open('student.txt').read().split()
correct = ['a', 'c', 'a', 'a', 'd', 'b', 'c', 'a', 'c', 'b', 'a', 'd', 'c', 'a', 'd', 'c', 'b', 'b', 'd', 'a']
count = 0
s = []
if len(a) == len(correct):
    for i in range(0,len(correct)):
        if correct[i] == a[i]:
            count += 1
        if correct[i] != a[i]:
            s.append(i+1)
else:
    print('error < 20 questions answered')

if count >= 15:
    print('good job')
else:
    print('bad job')

negative_count = 20 - count
print(count)
print(negative_count)
print(s)

