init python:
    # Function to add item to inventory
    def add_to_inventory(item_name, item_image):    # INV01
        for i in range(len(inventory_items)):
            if inventory_items[i] is None:  # Find the first empty slot
                inventory_items[i] = (item_name, item_image)    # Add the item to this slot
                break
                
        renpy.restart_interaction() # Refresh the inventory display
    
    # Function to remove an item from the inventory
    def remove_from_inventory(item_name):   # INV02
        global inventory_items

        # Track whether the item was found
        found_item = False

        # Loop through the inventory to find the item by its name
        for i in range(len(inventory_items)):
            if inventory_items[i] is not None and inventory_items[i][0] == item_name:
                inventory_items[i] = None  # Remove the item from the inventory
                found_item = True
                break

        # If we never found it, show a notification
        if not found_item:
            renpy.notify("Item not found in inventory") # N07

        renpy.restart_interaction()  # Refresh the inventory display

    # Function to check if specific items exist in the inventory
    def check_inventory_for_items(required_items):  # INV03
        # Create a set of all item names currently in the inventory
        inventory_set = {item[0] for item in inventory_items if item is not None}
        # Check if all required items are present in the inventory
        return required_items.issubset(inventory_set)