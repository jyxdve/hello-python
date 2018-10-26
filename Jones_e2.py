import sys

windintensity = float(sys.argv[1])

if  windintensity >= 220:
    print("Category: Super Typhoon")
elif windintensity >= 118 or windintensity == 219:
    print("Category: Typhoon")
elif windintensity >= 89 or windintensity == 117:
    print("Category: Severe Tropical Storm")
elif windintensity >= 62 or windintensity == 88:
    print("Category: Tropical Storm")
else:
    print("Category: Tropical Depression")
   

