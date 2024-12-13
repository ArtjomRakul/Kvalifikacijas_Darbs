init python:
    # Function to add item to inventory
    def add_to_inventory(item_name, item_image):
        for i in range(len(inventory_items)):
            if inventory_items[i] is None:  # Find the first empty slot
                inventory_items[i] = (item_name, item_image)    # Add the item to this slot
                break
                
        renpy.restart_interaction() # Refresh the inventory display
    
    # Function to remove an item from the inventory
    def remove_from_inventory(item_name):
        global inventory_items
        # Loop through the inventory to find the item by its name
        for i in range(len(inventory_items)):
            if inventory_items[i] is not None and inventory_items[i][0] == item_name:
                inventory_items[i] = None  # Remove the item from the inventory
                break

        renpy.restart_interaction()  # Refresh the inventory display

    # Function to check if specific items exist in the inventory
    def check_inventory_for_items(required_items):
        # Create a set of all item names currently in the inventory
        inventory_set = {item[0] for item in inventory_items if item is not None}
        # Check if all required items are present in the inventory
        return required_items.issubset(inventory_set)
    
# Screen to display the inventory icon
screen inventory_icon():
    # A button to open the inventory screen
    imagebutton:
        idle "images/icons/inventory_icon.png" 
        xpos 0.95
        ypos 0.05
        xanchor 0.5 # Align the icon to its center
        yanchor 0.5
        action Show("inventory_screen") # Action to display the inventory screen

# Screen to display the full inventory
screen inventory_screen():
    modal True  # Prevent interaction with other elements while this screen is open
    vbox:
        align (0.5, 0.5)  # Center the inventory field on the screen
        spacing 10  # Add space between inventory elements
        textbutton "Close" action Hide("inventory_screen") align (0.5, 0.05)
        # Grid layout to display inventory items in a 5x2 grid
        grid 5 2 spacing 10:    # 5 columns and 2 rows with spacing
            for item in inventory_items:
                frame:
                    # Display a default inventory slot background
                    background im.Scale("images/icons/inventory_slot.png", 100, 100)
                    xsize 100
                    ysize 100
                    if item is not None:    # Check if there is an item in this slot
                        add item[1]  # Show the item image from the tuple
