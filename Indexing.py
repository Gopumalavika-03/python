Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# Indexing
# Positive Indexing
a = "vijayawada"
a[0]
'v'
a[5]
'a'
a[6]
'w'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'vijaya'
b = "I am in class"
b[1]
' '
b[2]+b[3]
'am'
b[1]+b[4]+b[7]
'   '
>>> c = "I am learning python"
>>> c[14]+c[15]+c[16]+c[17]+c[18]+c[19]
'python'
>>> c[5]+c[6]+c[7]+c[8]+c[9]
'learn'
>>> d = "I love codegnan"
>>> d[7]+d[8]+d[9]+d[10]
'code'
>>> d[2]+d[3]+d[4]+d[5]
'love'
>>> d[11]+d[12]+d[13]+d[14]
'gnan'
>>> # Negative Indexing
>>> x = "Vijayawada"
>>> x[-1]
'a'
>>> A = "Vijayawada is a royal city"
>>> A[-10]+A[-9]+A[-8]+A[-7]+A[-6]
'royal'
>>> A[-4]+A[-3]+A[-2]+A[-1]
'city'
>>> A[-15]+A[-14]
'is'
>>> B= "Vizag is a city of destiny"
>>> B[-7]+B[-6]+B[-5]+B[-4]+B[-3]+B[-2]+B[-1]
'destiny'
>>> B[-26]+B[-25]+B[-24]+B[-23]+B[-22]
'Vizag'
