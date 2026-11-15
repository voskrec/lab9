inventory = {}

def add_item(item, count):
    inventory[item] = inventory.get(item, 0) + count

def remove_item(item, count):
    if item in inventory:
        inventory[item] -= count
        if inventory[item] <= 0:
            del inventory[item]

def update_item(item, count):
    inventory[item] = count

# Пример использования
add_item("яблоки", 10)
add_item("бананы", 5)
remove_item("яблоки", 3)
update_item("бананы", 20)
print(inventory)