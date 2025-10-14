FILENAME = "wimbledon.csv"


with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
    champion_count = {}
    champion_countries ={}
    for line in in_file:
        file_parts = line.split(",")
        champions = file_parts[2]
        countries = file_parts[3]
        champion_countries[champions] = countries
        if champions in champion_count:
                champion_count[champions] += 1
        else:
                champion_count[champions] = 1
    print(f"{champions},{champion_count}")
    print(champion_countries.items())

in_file.close()
