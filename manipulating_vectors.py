import unreal

# Prints the cross product of 0, 1, 0 and 1, 0, 1
vector_a = unreal.Vector(0, 1, 0)
vector_b = unreal.Vector(1, 0, 1)
cross_product = vector_a.cross(vector_b)
unreal.log(f"Cross product: {cross_product}")


# Prints the distance between 103, 32, 0.1 and 0, 0, 0
distance_a = unreal.Vector(103, 32, 0.1)
distance_b = unreal.Vector(0, 0, 0)
distance_two_points = distance_a.distance(distance_b)
unreal.log(f"Distance: {distance_two_points}")


# Prints the quaternion created from euler angles 0, 90, 75
vector_euler = unreal.Vector(0, 90, 75)
quartenion = unreal.Quat()
quartenion.set_from_euler(vector_euler)
unreal.log(f"Euler angles: {vector_euler}, quartenion: {quartenion}")