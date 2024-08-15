import unreal
from datetime import date

unreal.EditorDialog.show_message("The title", "The message", unreal.AppMsgType.YES_NO)

today = date.today()
print(f"Today is {today}")


print(unreal.EditorUtilityLibrary().get_selected_assets())


def create_shopping_item(price, name):
    return {
        "name": name,
        "price": price
    }
    
shopping_list = []

shopping_list.append(create_shopping_item(10, "rice"))
shopping_list.append(create_shopping_item(20, "beans"))

print(shopping_list)