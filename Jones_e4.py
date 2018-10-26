import geometry

input = input("Enter the side lenghts of a triangle:")

(a,b,c) = (float(x) for x in line.split(","))

P = geometry.triangle_perimeter(a,b,c)
A = geometry.triangle_heronsarea(a,b,c)

print ("Perimeter: {:.2f} .format(geometry.triangle_perimeter(a,b,c)))
print ("Area: {:.2f} .format(geometry.triangle_heronsarea(a,b,c)))