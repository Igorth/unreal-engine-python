import unreal

def rename_assets():
    # Instances of unreal classes
    system_lib = unreal.SystemLibrary()
    editor_util = unreal.EditorUtilityLibrary()
    string_lib = unreal.StringLibrary()

    # Get the selected assets
    selected_assets = editor_util.get_selected_assets()
    num_assets = len(selected_assets)
    replaced = 0

    unreal.log(f"Selected {num_assets} assets...")

    # Loop through each selected asset
    for asset in selected_assets:
        # Get the asset name
        asset_name = system_lib.get_object_name(asset)

        unreal.log(f"Processing asset: {asset_name}")


rename_assets()