"""
cities=['Hyderabad','Amaravathi','Trivandrum','Chennai','Mumbai','Ahmedabad']

#Bad Way
print('Bad Way')
i=0
for city in cities:
	print(i,city)
	i+=1

#Good Way
print('Good Way')
for (i,city) in enumerate(cities):
    print(i,city)

x_list = [1, 2, 3]
y_list = [5, 6, 7]

# Bad Way
print('Bad Way')
for i in range(len(x_list)):
    x = x_list[i]
    y = y_list[i]
    print(x, y)

# Good Way
print('Good Way')
for (x, y) in zip(x_list, y_list):
    print(x, y)

x=10
y=20
print(f'Before Swap x={x},y={y}')

#Bad Way
tmp=x
x=y
y=tmp
print(f'After Swap x={x},y={y}')

#Good Way

x,y=y,x
print(f'After Swap x={x},y={y}')


ages = {
    'Kiran': 34,
    'Kishore': 45,
    'Hari': 34,
    'Praveen':30
}

# Bad Way
print('Bad Way')
if 'Praveen' in ages:
    age = ages['Praveen']
else:
    age = 'Unknown'

print(f'Praveen is {age} years old')

# Good Way
print('Good Way')

age = ages.get('Praveen','Unknown')
print(f'Praveen is {age} years old')


needle = 'd'
haystick = ['a', 'b', 'c','d']
found = False
# Bad Way
print('Bad Way')
for item in haystick:
    if item == needle:
        print('Found')
        found = True
        break
if not found:
    print('Not Found')

# Good Way
print('Good Way')
for item in haystick:
    if item == needle:
        print('Found')
        break
else:  # if no break statement occured
    print('Not Found')

###############
print('Converting')

try:
	print(int('1'))
except:
	print('Conversion failed')
else:
	print('Conversion Successful')
finally:
	print('Done!!!')

###################
condition=True

if condition:
    x=1
else:
    x=0

print(f'X={x}')

print('Better:')
x=1 if condition else 0
print(f'X={x}')


name_list=['Kiran','Kishore','Ramesh']
age_list=[30,23,34]
sal_list=[30000,400000,500000]

for val in zip(name_list,age_list,sal_list):
	print(val)


# Coconuts problem
bag_content=int(input("Enter the number of coconuts per bag:"))
tot_coc=bag_content*bag_content
toll=bag_content
while toll>=0:
	tot_bags=int(tot_coc//bag_content)
	extra=tot_coc%bag_content
	toll_paid=tot_bags
	if(extra>0):
		toll_paid += 1

	print(f'Toll#{toll}  Total Bags : {tot_bags} Extra:{extra} Toll Paid:{toll_paid} ')
	tot_coc=tot_coc-(tot_bags)
	if(extra>0):
		tot_coc-=1
	toll-=1



def find_next_priosoner(priosoners, nxtPrsnr, step, tprsn):
    cnt = step
    while cnt > 1:
        while (priosoners[nxtPrsnr] == '-'):
            nxtPrsnr += 1
            if (nxtPrsnr == tprsn):
                nxtPrsnr = 0
        cnt -= 1
        nxtPrsnr += 1
    return (nxtPrsnr)



        if (priosoners[nxtPrsnr] == '-'):
            nxtPrsnr += 1
        else:
            cnt -= 1
            nxtPrsnr += 1
        if nxtPrsnr == tprsn:
            nxtPrsnr = 0

    return (nxtPrsnr)



def who_goes_free(nop, step):
    priosoners = list(range(0, nop))
    nxtPrsnr = 0
    tprsn = nop
    while nop > 1:
        nxtPrsnr = find_next_priosoner(priosoners, nxtPrsnr, step, tprsn)
        print(f"Round:{nop}# Kill{priosoners[nxtPrsnr]}@{nxtPrsnr}")
        priosoners[nxtPrsnr] = '-'

        nop -= 1
    for item in priosoners:
        if item != '-':
            break
    print(f"Result: {item}@{priosoners.index(item)}")


# who_goes_free(9,2)
# who_goes_free(9,3)
"""

if __name__ == '__main__':
    who_goes_free(16, 3)
