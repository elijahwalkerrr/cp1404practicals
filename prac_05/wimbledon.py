def line_extraction(line, champion_countries):
    file_parts = line.split(",")
    champions = file_parts[2]
    countries = file_parts[3]
    champion_countries[countries] = champions
    return champions, champion_countries


def count_champions(champion_count, champions):
    if champions in champion_count:
        champion_count[champions] += 1
    else:
        champion_count[champions] = 1
    return champion_count


def print_countries_and_champions(champion_count, champion_countries):
    for champions, count in champion_count.items():
        print(f"{champions}, {count}")
    winning_countries = list(champion_countries.keys())
    print(f"\nThese {len(winning_countries)} Countries have won Wimbledon:")
    print(", ".join(winning_countries))


def main():
    filename = "wimbledon.csv"
    champion_count = {}
    champion_countries = {}
    file_number = 0

    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            file_number += 1
            if file_number == 1:
                continue
            champions, champion_countries = line_extraction(line, champion_countries)
            champion_count = count_champions(champion_count, champions)

    print_countries_and_champions(champion_count, champion_countries)


main()



