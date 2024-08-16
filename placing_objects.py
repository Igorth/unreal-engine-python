import unreal
import math

def spawn_cube(location = unreal.Vector(0, 0, 0), rotation = unreal.Rotator(0, 0, 0)):
    # Get the system to control the actors
    editor_actor_subs = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    
    # Create a StaticMeshActor
    actor_class = unreal.StaticMeshActor

    # Place it in the level
    static_mesh_actor = editor_actor_subs.spawn_actor_from_class(actor_class, location, rotation)

    # Load and add the mesh (Cube, Cylinder, Sphere)
    static_mesh = unreal.EditorAssetLibrary.load_asset("/Engine/BasicShapes/Cylinder")
    static_mesh_actor.static_mesh_component.set_static_mesh(static_mesh)

def run():

    mesh_count = 30
    circle_radius = 1000
    circle_center = unreal.Vector(0, 0, 0)

    for i in range(mesh_count):
        circle_x_location = circle_radius * math.cos(math.radians(i * 360 / mesh_count))
        circle_y_location = circle_radius * math.sin(math.radians(i * 360 / mesh_count))

        location = unreal.Vector(circle_x_location, circle_y_location, 0)
        # Cubes Orientation
        location_to_circle_center = location - circle_center

        rotation = location_to_circle_center.quaternion().rotator()

        spawn_cube(location, rotation)

run()