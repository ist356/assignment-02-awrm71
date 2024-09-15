'''
This is a module for parsing packging data
'''

def parse_packaging(packaging_data: str) -> list[dict]:
    result = []
    seen_units = set() 

    parts = packaging_data.split(' / ')

    for part in parts:
        quantity_item = part.split(' in ', 1)
        quantity_part = quantity_item[0].strip()  
        unit_part = quantity_item[1].strip() 


        quantity, item = quantity_part.split(maxsplit=1)
        quantity = int(quantity)  

        if item not in seen_units:
            result.append({item: quantity})
            seen_units.add(item)

        container_quantity, container = unit_part.split(maxsplit=1)
        container_quantity = int(container_quantity) 

        if container not in seen_units:
            result.append({container: container_quantity})
            seen_units.add(container)

    return result






def calc_total_units(package: list[dict]) -> int:
    total = 1
    for item in package:
        total *= list(item.values())[0] 
    return total



def get_unit(package: list[dict]) -> str:
    return list(package[0].keys())[0] 

# This will only run from here, not when imported
# # Use this for testing / debugging cases with the debugger
if __name__ == '__main__':
    
    text = "25 balls in 1 bucket / 4 buckets in 1 bin"
    package = parse_packaging(text)
    print(package)

    package_total = calc_total_units(package)
    unit = get_unit(package)
    print(f"{package_total} {unit} total")