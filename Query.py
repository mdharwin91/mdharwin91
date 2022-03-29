storage = {
    "SCH#DXBIAH" : "DXB-IAH",
    "SCH#MAADXB" : "MAA-DXB",
    "SCH#KOLDXB" : "KOL-DXB",
    "SCH#MAAKOL" : "MAA-KOL",
    "SCH#DELDXB" : "DEL-DXB",
    "SCH#MAABOM" : "MAA-BOM",
    "SCH#HYDDXB" : "HYD-DXB",
    "SCH#MAAHYD" : "MAA-HYD",
    "SCH#MAAJFK" : "MAA-JFK",
    "SCH#DXBJFK" : "DXB-JFK",
    "SCH#DELJFK" : "DEL-JFK",
    "SCH#KOLDEL" : "KOL-DEL"
}
def query(n):
    sol =[]
    for item in storage.keys():
        if item.startswith(n):
            # print(storage[item])
            # return storage[item]
            sol.append(storage[item])
    return sol

def query_ends(n):
    sol=[]
    for item in storage.keys():
        if item.endswith(n):
            # print(storage[item])
            # return storage[item]
            sol.append(storage[item])
    return sol
seg_count = 3
SOLUTION = []
D= "SCH#MAA"
A= "DXB"
# query(D+A)
leg1 =[]
leg_flt = []
#FINDING DIRECT SOLUTIONS
leg1 = query(D+A)
# print("One Leg", leg1)
SOLUTION.append(leg1)
#FINDING THROUGH FLIGHTS
leg_mid = (query(D))
# print(leg_mid)
if seg_count == 2:
    for j in leg_mid:
        leg_tmp =  (query(("SCH#"+str(j[-3:]+A))))
        leg_flt.append(leg_tmp)
else:
    for j in leg_mid:
        leg_tmp =  (query(("SCH#"+str(j[-3:]))))
        leg_flt.append(leg_tmp)
leg_connect = []
#DROPPING EMPTY LISTS
for x in leg_flt:
    if x == []:
        continue
    else:
        for xy in x:
            leg_connect.append(xy)



for l in leg_mid:
    for k in leg_connect:
        if l[-3:] == k[:3]:
            SOLUTION.append(['''{0}|{1}'''.format(l,k)])
print("Solution", SOLUTION)
leg_flt3=[]
print(leg_connect)
if seg_count == 3:
    for d in leg_connect:
        leg_tmp = (query(("SCH#"+str(d[-3:])+A)))
        leg_flt3.append(leg_tmp)

#DROPPING EMPTY LISTS
leg_3=[]
for x in leg_flt3:
    if x == []:
        continue
    else:
        for xy in x:
            leg_3.append(xy)

for c in leg_connect:
    for d in leg_3:
        if c[-3:] == d[:3]:
            SOLUTION.append(['''{0}|{1}|'''.format(c,d)])
# print(leg_3)

# print(leg1)
print("Solution", SOLUTION)

