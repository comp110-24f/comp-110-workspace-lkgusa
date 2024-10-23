"""Examples of dictionary syntax with Ice Cream Shop order tallies."""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,  # This comma isn't necessary, jic another item is added
}

# Prints number of flavors in ice_cream
print(len(ice_cream))

# Adds new row to dictionary
ice_cream["mint"] = 10

# Access values by their key using subscription
mint_orders: int = ice_cream["mint"]
print(mint_orders)

# These two lines are identical, adds 1 to mint int
ice_cream["mint"] = ice_cream["mint"] + 1
ice_cream["mint"] += 1

# Remove items by key using .pop method
ice_cream.pop("strawberry")

# Tests if key is in dictionary
print("strawberry" in ice_cream)
print("vanilla" in ice_cream)

# Loop through items using for-in loops

for flavor in ice_cream:
    # Flavor has same datatype as flavors "chocolate", etc in ice_cream
    tally: int = ice_cream[flavor]
    print("f{flavor}: {tally}")

ice_cream["pecan"]
