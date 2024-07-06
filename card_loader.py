import argparse
import json

def load_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def save_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def edit_json(data, key, value):
    keys = key.split('.')
    d = data
    for k in keys[:-1]:
        if k not in d:
            d[k] = {}
        d = d[k]
    d[keys[-1]] = value
    return data

def add_entry():
    pass

if __name__ == "__main__":
    
    
    parser = argparse.ArgumentParser(description='a simple interface to load flash cards into a json object array')
    parser.add_argument('filename', help='the file to process, should be an array of json objects')
    """ parser.add_argument('edit', help='edit the flashcard')
    parser.add_argument('create', help='create a new entry')
    parser.add_argument('delete', help='remove an object in the array') """
    
    args = parser.parse_args()
    
    data = load_json(args.filename)
    
    while True:
        print('\nCurrent JSON:')
        print(json.dumps(data,indent=2))
        
        action = input("\nEnter 'edit <key>' to make a change, 'add' to make an entry, 'save' to save, or 'exit' to quit without saving.\n\n>")
        action = action.split()
        
        if action[0].lower() == 'edit':
            try:
                print(f"{data[action[1]]}")
                new_action = input('\nGive your new entry for the key:\n\n>')
            except:
                print("key does not exist in this dataset")
            
            
        elif action[0].lower() == 'add':
            keys = data[0].keys()
            new_entry = {}
            for key in keys:
                if key != 'tags':
                    new_action = input(f"\nEnter your entry for {key}.\n\n>")
                    new_entry[key] = new_action
                else:
                    new_action = input("\nEnter the tags separated by commas.\n\n>")
                    new_entry[key] = new_action.split(',')
                
            data.append(new_entry)
            
        elif action[0].lower() == 'save':
            save_json(data, args.filename)
            print(f"Changes saved to {args.filename}")
            
        elif action[0].lower() == 'exit':
            print("Exiting without saving changes")
            break
        else:
            print("Invalid action. Please try again.")
