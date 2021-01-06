w,h,b=input().split()
w=int(w)
h=int(h)
b=int(b)

bit = w*h*b
byte = bit / 8
kb = byte/1024
mb = kb/1024

print('{0:0.2f} MB'.format(round(mb,2)))