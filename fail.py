import sys
import json

my_dict = {
    "object1": {"id": 1464, "value": 12435},
    "object2": {"id": 245, "value": 20046},
    "object3": {"id": 345, "value": 3008566},
    "object4": {"id": 45689, "value": 40078},
    "object5": {"id": 54946, "value": 50464}
}

new_dict = {}

for key, value in my_dict.items():
    # Check if the length of the "value" key is not equal to 5 digits
    if len(str(value["value"])) != 5:
        print(f'Error: {key} has a "value" with length not equal to 5: {value["value"]}')
        print("Final state of new_dict:", new_dict)
        
        # Save the current state of new_dict to output.json before exiting
        with open('output.json', 'w') as f:
            json.dump(new_dict, f, indent=4)
        
        sys.exit(1)
    
    # Add the current item to the new dictionary
    new_dict[key] = value

# If all checks pass, save the final new_dict to output.json
with open('output.json', 'w') as f:
    json.dump(new_dict, f, indent=4)

print("All 'value' lengths are 5 digits.")
print("Final new_dict saved to output.json")
