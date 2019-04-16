import sys

print(len([1, 2, 3]))

print([1, 2, 3] + [4, 5, 6])
curr_list = [1, 2, 3]
curr_list.append([4, 5, 6])
print(curr_list)

print(['Hi!'] * 4)

print(3 in [1, 2, 3])

for x in [1, 2, 3]:
    print(x, end=" ")

print('------------------------------')

list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
 
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
