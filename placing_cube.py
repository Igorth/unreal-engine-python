import unreal

def spawn_cube(location=unreal.Vector(), rotation=unreal.Rotator()):

    # Get the system to control the actors
    editor_actor_subs = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)

    # Create a StaticMeshActor
    actor_class = unreal.StaticMeshActor

    # Place it in the level
    static_mesh_actor = editor_actor_subs.spawn_actor_from_class(actor_class, location, rotation)

    # Load and add the cube to it
    static_mesh = unreal.EditorAssetLibrary.load_asset("/Engine/BasicShapes/Cube")
    static_mesh_actor.static_mesh_component.set_static_mesh(static_mesh)


def run():

    cube_count = 20

    for i in range(cube_count):
        circle_x_location = i * 150
        circle_y_location = 0

        location = unreal.Vector(circle_x_location, circle_y_location, 0)
        spawn_cube(location)


run()