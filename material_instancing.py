import unreal


def get_selected_content_browser_assets():
    editor_utility = unreal.EditorUtilityLibrary()
    selected_assets = editor_utility.get_selected_assets()

    return selected_assets


def run():
    unreal.log("Running create material instances script")


run()
