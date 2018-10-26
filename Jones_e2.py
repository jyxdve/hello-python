import sys

windintensity = float(sys.argv[1])

if  windintensity >= 220:
    print("Super Typhoon")
elif windintensity >= 118 or windintensity == 219:
    print("Typhoon")
elif windintensity >= 89 or windintensity == 117:
    print("Severe Tropical Storm")
elif windintensity >= 62 or windintensity == 88:
    print("Tropical Storm")
else:
    print("Tropical Depression")
   

