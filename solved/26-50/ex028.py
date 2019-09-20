#Solved 669171001


som = 1
for x in range(1,501):
    RB = ((2*x)+1)**2
    som = som + RB #Rechtsboven
    print(RB)

    LB = (((2 * x)**2) + 1)
    som = som + LB #LinksOnder
    print(LB)


    RO = (((2 * x)**2) + 1) - (2 * x + 1) + 1
    som = som + RO #Rechtsonder
    print(RO)

    LB = (((2 * x)**2) + 1) + (2 * x)
    som = som + LB #Linksboven
    print(LB)
    print("")
print(som)
