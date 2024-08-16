import unreal

def get_selected_content_browser_assets():
    editor_utility = unreal.EditorUtilityLibrary()
    selected_assets = editor_utility.get_selected_assets()
    return selected_assets

def generate_new_name_for_asset(asset):
    # Log to see the type of the asset
    # print(f"Asset {asset.get_name()} is a {type(asset)}")

    # Is asset a MaterialInstance
    if isinstance(asset, unreal.MaterialInstance):
        return "MI_" + asset.get_name()
    
    # Is asset a Material
    if isinstance(asset, unreal.Material):
        return "M_" + asset.get_name()
    
    # Is asset a Texture
    if isinstance(asset, unreal.Texture):
        return "T_" + asset.get_name()
    
    # Is asset a NiagaraSystem
    if isinstance(asset, unreal.NiagaraSystem):
        return "NS_" + asset.get_name()
    
    return asset.get_name()

def run():
    selected_assets = get_selected_content_browser_assets()

    for i in range(len(selected_assets)):
        asset = selected_assets[i]

        old_name = asset.get_name()
        new_name = generate_new_name_for_asset(asset)

        print(f"Renaming {old_name} to {new_name}")


run()