from math import *

while True:
    x = radians(float(input("x: ")))
    y = radians(float(input("y: ")))
    z = radians(float(input("z: ")))

    # x = roll (ψ)
    # y = pitch (ϕ)
    # z = yaw (θ)
    
    x_final = -sin(x) * cos(z) - cos(x) * sin(y) * sin(z)
    y_final = sin(x) * sin(z) - cos(x) * sin(y) * cos(z)
    z_final = cos(x) * cos(y)

    x_proj = x_final
    y_proj = y_final

    proj_mag = sqrt(x_proj**2 + y_proj**2)

    x_proj /= proj_mag
    y_proj /= proj_mag

    dot = acos(z_final)

    # x, y = (cos(radians(x)) * sin(radians(y))), (sin(radians(y)))
    # z = sqrt(1 - (x**2 + y**2))

    print("x, y, z")
    print(x_final, y_final, z_final, sep=", ")
    print("ang to z:", degrees(dot))
    print("proj x, y:", x_proj, y_proj)
    print()
