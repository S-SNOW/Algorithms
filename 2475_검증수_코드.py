# 코드 (파이썬으로 짰다.)

a=input('').split()
a.append(0)
for i in range(0, 5):
	a[i]=int(a[i])
    a[5]+=a[i]*a[i]
a[5]=a[5]%10
print(a)
