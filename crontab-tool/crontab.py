import sys

symbols = {
    "*" : "any value (wildcard)",
    "," : "list separator (0,15,30,45)",
    "-" : "range separator (1-5)",
    "/" : "setp values (1/10)"
}

days = {
    "MON":"Monday",
    "TUE":"Tuesday",
    "WED":"Wednesday",
    "THU":"Thursday",
    "FRI":"Friday",
    "SAT":"Saturday",
    "SUN":"Sunday"
}

def calendar(value):
    if value.upper().strip() == "JAN" or value == 1:
        return "January"
    if value.upper().strip() == "FEB" or value == 2:
        return "February"
    if value.upper().strip() == "MAR" or value == 3:
        return "March"
    if value.upper().strip() == "APR" or value == 4:
            return "April"
    if value.upper().strip() == "MAY" or value == 5:
            return "May"
    if value.upper().strip() == "JUN" or value == 6:
            return "June"
    if value.upper().strip() == "JUL" or value == 7:
            return "July"
    if value.upper().strip() == "AUG" or value == 8:
            return "August"
    if value.upper().strip() == "SEP" or value == 9:
            return "September"
    if value.upper().strip() == "OCT" or value == 10:
            return "October"
    if value.upper().strip() == "NOV" or value == 11:
            return "November"
    if value.upper().strip() == "DEC" or value == 12:
            return "December"
    return None

def timeofday(value):
    if value < 12:
        return "AM"
    elif value == 12:
        return "noon"
    else:
        return "PM"

def validate_time(idx:int,value:str):
    if idx == 0:
        if value.startswith("*"):
            if value == "*":
                return "Every minute"
            else:
                value = value.replace("*/","")
                return f"Every {int(value)} minutes"
        else:
            try:
                value = int(value)
                return f"For {value} minutes"
            except:
                if "-" in value:
                    rng = value.split("-")
                    return f"between {rng[0]} to {rng[1]} minutes"
    elif idx == 1:
        try:
            value = int(value)
            return f"between {value} {timeofday(value)} to {value+1} {timeofday(value)}"
        except:
            if "-" in value:            
                rng = value.split("-")
                return f"between {rng[0]} {timeofday(int(rng[0]))} to {rng[1]} {timeofday(int(rng[1]))}"
    elif idx == 2:
        try:
            value = int(value)
            return f"On {value}"
        except:
            if "-" in value:            
                rng = value.split("-")
                return f"between {rng[0]} to {rng[1]}"
    elif idx == 3:
        try:
            value = int(value)
            return f"In {calendar(value)}"
        except:
            if "-" in value:            
                rng = value.split("-")
                return f"Between {rng[0]} to {rng[1]}"
            elif calendar(value):
                return f"On {calendar(value)}"
    else:
        if "-" in value:
            rng = value.split("-")
            if rng[0].upper() in days and rng[1].upper() in days:
                return f"{days[rng[0].upper()]} through {days[rng[1].upper()]}" 
        elif value.upper() in days.keys():
            return f"Only on {days[value.upper()]}"
    return ""

args = sys.argv
argc = len(args)

dashes = 0

for value in symbols.values():
    dashes = max(dashes, len(value))

dashes += 10
print("-"*dashes)
print("Symbol | Meaning ")
for key,value in symbols.items():
    print(f"{key}      | {value}")
print("-"*dashes)
expression = args[argc-1].split(" ")

if len(expression) < 5:
    print("crontab: Invalid Expression")
else:
    message = []
    for i,value in enumerate(expression):
        response = validate_time(i,value)
        if response:
            message.append(response)
             
    print(", ".join(message))

