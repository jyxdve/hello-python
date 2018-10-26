import sys

WindIntensity= float(sys.argv[1])

if  WindIntensity >= 220:
    print("Super Typhoon")
elif WindIntensity >= 118 or  WindIntensity == 219.99:
    print("Typhoon")
elif WindIntensity >= 89 or   WindIntensity == 117.99:
    print("Severe Tropical Strorm")
elif WindIntensity >= 62 or   WindIntensity == 88.99:
    print("Tropical Storm")
else:
    print("Tropical Depression")
   

