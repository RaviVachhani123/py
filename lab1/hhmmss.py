sec=int(input("enter second"))
hour = sec//3600
rs=sec%3600
min=rs//60
se=rs%60
print(hour,":",min,":",se)