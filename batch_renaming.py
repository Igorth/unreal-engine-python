import unreal

def get_selected_content_browser_assets():
    editor_utility = unreal.EditorUtilityLibrary()
    selected_assets = editor_utility.get_selected_assets()
    return selected_assets

def run():
    selected_assets = get_selected_content_browser_assets()
    print("Using a for each loop")
    for asset in selected_assets:
        print(f"Asset: {asset.get_name()}")

    print("\nUsing a list comprehension")
    asset_names = [asset.get_name() for asset in selected_assets]
    print(asset_names)

    print("\nUsing a classic for loop")
    for i in range(len(selected_assets)):
        asset = selected_assets[i]
        print(f"Asset: {asset.get_name()}")


run()