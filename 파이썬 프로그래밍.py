# 문자열 안에 어떤 값을 삽입 하는 방법
name='han'
print("hello, %s!" % name)

print("hello, %s!" %'han')

print("i'm %d years old." % 22)

print("hello, %10s!" % name)
print("hello, %-10s!" % name)

no=3.141592653
print("pi = %f"% no)
print("pi = %.10f"% no)
print("pi = %10.4f"% no)

print("hello, {}!".format(name))
print("pi = {}".format(no))
print("name={0} pi={1}".format(name,no))
print("name={name} pi={no}".format(name=name,no=no))

print("hello, {:>10}!".format(name))
print("hello, {:<10}!".format(name))


print("pi = {:10.4f}".format(no))
print("pi = {:.4f}".format(no))


print(f'hello, {name}!')
print(f'hello, {name:>10}!')
print(f'hello, {name:<10}!')
print(f'hello, {name:z>10}!')
print(f'hello, {name:*<10}!')

print(f'pi = {no}')
print(f'pi = {no:>.10f}')

str='hello world'
print(str.count('l'))

print('-'.join(name))

print(f'hello {name:.^10}')
print(f'hello {name:.>10}')
print(f'hello {name:.<10}')

list=['hello','world',31,2.7,True,'True','31']

print(list.pop(3))
print(list)
list.remove('hello')
print(list)

dct={'name':'han','birth':['agust',20],'age':24}
print(dct['name'])
print(dct['birth'])
print(dct.get('birth'))

del dct['birth']
print(dct)

dct['birth']=['agust',20]
print(dct['birth'])
print(dct.pop('name'))
print(dct)
print(dct.keys())
print(dct)
dct=dct.items()
print(dct)