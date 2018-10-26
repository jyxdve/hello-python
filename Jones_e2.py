import sys

windintensity= float(sys.argv[1])

if  windintensity >= 220:
    print("Super Typhoon")
elif windintensity >= 118.99 or  windintensity == 219.99:
    print("Typhoon")
elif windintensity >= 89.99 or   windintensity == 117.99:
    print("Severe Tropical Strorm")
elif windintensity >= 62.99 or   windintensity == 88.99:
    print("Tropical Storm")
else:
    print("Tropical Depression")
   

