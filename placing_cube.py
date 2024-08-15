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
    location = unreal.Vector(30,10,400)
    rotation = unreal.Rotator(88,-5,12)
    spawn_cube(location, rotation)    


run()