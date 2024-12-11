init python:
    # Function to add item to inventory
    def add_to_inventory(item_name, item_image):
        for i in range(len(inventory_items)):
            if inventory_items[i] is None:  # Find the first empty slot
                inventory_items[i] = (item_name, item_image)
                break
                
        renpy.restart_interaction()
    
    # Function to remove an item from the inventory
    def remove_from_inventory(item_name):
        global inventory_items
        for i in range(len(inventory_items)):
            if inventory_items[i] is not None and inventory_items[i][0] == item_name:
                inventory_items[i] = None  # Clear the inventory slot
                break
        renpy.restart_interaction()  # Refresh the inventory display

    def check_inventory_for_items(required_items):
        inventory_set = {item[0] for item in inventory_items if item is not None}
        return required_items.issubset(inventory_set)
    
# Inventory icon on the screen
screen inventory_icon():
    imagebutton:
        idle "images/icons/inventory_icon.png"  # Replace with the path to your inventory icon
        xpos 0.95
        ypos 0.05
        xanchor 0.5
        yanchor 0.5
        action Show("inventory_screen")

# Inventory screen
screen inventory_screen():
    modal True
    vbox:
        align (0.5, 0.5)  # Center the inventory field
        spacing 10
        textbutton "Close" action Hide("inventory_screen") align (0.5, 0.05)
        grid 5 2 spacing 10:  # Display 10 slots in a 5x2 grid
            for item in inventory_items:
                frame:
                    background im.Scale("images/icons/inventory_slot.png", 100, 100)
                    xsize 100
                    ysize 100
                    if item is not None:
                        add item[1]  # Show the item image from the tuple
