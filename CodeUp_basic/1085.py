h,b,c,s = input().split()
h=int(h)
b=int(b)
c=int(c)
s=int(s)

bit = h*b*c*s
byte = bit/8
KB = byte/1024
MB = KB/1024

print('{0} MB'.format(round(MB,1)))
