#primfaktorisering

talTotal= int(input('Skriv in ditt tal: '))
talRest = talTotal

def delning(d):
    global talRest
    while (talRest%d) == 0:
        print (d)
        talRest = talRest//d
    return

delning(2)



talDelare = 3

#delning(talDelare,talRest)

while talDelare < talRest:
    delning(talDelare)
    talDelare = talDelare + 2





if talRest == talTotal:
    print(str(talTotal) + ' är ett primtal')
elif talRest != 1:
    print(talRest)
    print('Färdigt')    
else:
    print('Färdigt')



