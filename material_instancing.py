import unreal


def get_selected_content_browser_assets():
    editor_utility = unreal.EditorUtilityLibrary()
    selected_assets = editor_utility.get_selected_assets()

    return selected_assets


def log_asset_types(assets):
    for asset in assets:
        unreal.log(f"Asset Name: {asset.get_name()} is a {type(asset)}")


def find_material_in_assets(assets):
    for asset in assets:
        if type(asset) is unreal.Material:
            return asset
        return None


def find_textures2D_in_assets(assets):
    textures = []
    for asset in assets:
        if type(asset) is unreal.Texture2D:
            textures.append(asset)
    return textures


def create_material_instance(parent_material, asset_path, new_asset_name):
    # Create the child material
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    material_factory = unreal.MaterialInstanceConstantFactoryNew()
    new_asset = asset_tools.create_asset(new_asset_name, asset_path, None, material_factory)

    # Assign its parent
    unreal.MaterialEditingLibrary.set_material_instance_parent(new_asset, parent_material)

    return new_asset


def create_material_instances_for_each_texture(material, textures):
    for texture in textures:
        unreal.log(f"Creating material instance for texture: {texture.get_name()}")

        material_asset_path = "/Game/Python"
        material_name = f"{material.get_name()}_{texture.get_name()}"

        material_instance = create_material_instance(material, material_asset_path, material_name)


def run():
    unreal.log("Running create material instances script")

    selected_assets = get_selected_content_browser_assets()
    log_asset_types(selected_assets)

    material = find_material_in_assets(selected_assets)
    textures = find_textures2D_in_assets(selected_assets)

    if not material:
        unreal.log_error("No material selected")
        return

    if not textures:
        unreal.log_error("No textures selected")
        return

    unreal.log(f"Selected material: {material.get_name()}")
    unreal.log(f"{len(textures)} textures selected")

    # create_material_instance(material, "/Game/Python/", "FirstMaterialInstance")
    create_material_instances_for_each_texture(material, textures)


run()
