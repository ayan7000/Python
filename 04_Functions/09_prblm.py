
def even_gen(limit):
    # li=[]
    for i in range(2,limit+1,2):
        # li.append[i]
        yield i
    
# print(even_gen(10))
for num in even_gen(10):
    print(num)
