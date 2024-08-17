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


run()
