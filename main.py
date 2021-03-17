import json, csv, sys, bz2

print("loading files...")
with open(sys.argv[1]) as file:
    data = json.load(file)


with open(sys.argv[2], "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    
    headers = next(csv_reader)
    print("writing data...")
    for line in csv_reader:

        for header, entry in zip(headers, line):
            if header == "" or header == 'ignoreme':
                continue
            if header == "categoryPath":
                data[header] = [entry]
            elif header == "mass":
                data[header] = float(entry)
            else:
                data[header.strip("ï»¿")] = entry

        prefix = ""
        if  len(sys.argv) >= 4:
            prefix = sys.argv[3] + "/"

        file = open(prefix + "Item_Weapon_" + line[0] + ".json", "w")
        json.dump(data, file, indent=2)
        file.close() 
