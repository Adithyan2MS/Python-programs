import datetime

x=datetime.datetime.now()
print(x.strftime("%d-%m-%Y"))
print(datetime.date.today().month)
y=datetime.datetime(year=2021,month=2,day=12)
z=datetime.datetime(2021,2,11)
dif=y-z
print(dif)
end=datetime.datetime.now()
difference=end-x
print(difference)