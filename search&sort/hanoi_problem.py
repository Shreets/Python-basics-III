source_disc =[5,4,3,2,1]
spare_disc = []
target_disc = []


def hanoi(n, source, target, spare):
    if n>0:
        hanoi(n-1, source,spare,target)
        target.append(source.pop())
        hanoi(n - 1, spare, target, source)


hanoi(5,source_disc, target_disc, spare_disc)

print('source disc : ', source_disc)
print('spare disc : ', spare_disc)
print('target disc : ', target_disc)

#OUTPUT
# source disc :  []
# spare disc :  []
# target disc :  [5, 4, 3, 2, 1]
