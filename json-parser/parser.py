import sys
import ast

path = f"tests/{sys.argv[1]}.json"

def check_value(value):
    try:
        if value == "null":
            return True
        elif value.startswith('"') and value.endswith('"'):
            return True
        elif value == "true" or value == 'false':
            return True
        elif value.startswith('[') and value.endswith(']'):
            if len(value)==2:
                return True
            value = value[1:len(value)-1]
            val_list = value.split(",")
            for val in val_list:
                if(not check_value(val)):
                    raise Exception
            return True
        elif value.startswith('{') and value.endswith('}'):
            return True
        elif int(value):
            return True
        else:
            raise Exception
    except:
        return False
            
def main():
    with open(path, 'r') as file:
        data  = file.read().strip()

        if not data:
            print("Invalid JSON")
            exit(1)
        
    if data[0].__eq__('{') and data[len(data)-1].__eq__('}'):
        data = data[1:len(data)-1]
        if(not data):
            print("Valid JSON")
            return
        values = data.split(',')
        for value in values:
            if not value:
                print("Invalid JSON")
                exit(1)
            pair = value.strip().split(":",1)
            pair[1] = pair[1].strip()
            pair[0] = pair[0].strip()
            if not pair[0].startswith('"') or not pair[0].endswith('"'):
                print("Invalid JSON")
                exit(1)
            if(check_value(pair[1])):
                continue  
            else:
                print("Invalid JSON")
                exit(1)
        print("Valid JSON")
    else:
        print("Invalid JSON")

if __name__ == "__main__":
    main()