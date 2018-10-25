import sys

WindIntensity=(sys.argv[1])
WindIntensity = float(WindIntensity)

if  WindIntensity >=220.0:
    print("Super Typhoon")
elif WindIntensity >=118.o:
    print("Typhoon")
elif WindIntensity >=89.0:
    print("Severe Tropical Strorm")
elif WindIntensity >=62.0:
    print("Tropical Storm")
else:
    print("Tropical Depression")
   

