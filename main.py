import csv
from communities import *
from collections import Counter
from terminaltables import AsciiTable


def load_csv():
    with open('malopolska.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter='\t')
        for row in readCSV:
            region_type = row[5]
            if region_type == "województwo":
                Wojewodztwo(row[0], row[1], row[2], row[3], row[4], row[5])
            elif region_type == "powiat":
                new_powiat = Powiat(row[0], row[1], row[2], row[3], row[4], row[5])
                Wojewodztwo.add_powiat(new_powiat)
            elif region_type == "miasto na prawach powiatu":
                new_powiat = MiastoNaPrawachPowiatu(row[0], row[1], row[2], row[3], row[4], row[5])
                Wojewodztwo.add_powiat(new_powiat)
            else:
                new_region = None
                if region_type == "gmina miejska":
                    new_region = GminaMiejska(row[0], row[1], row[2], row[3], row[4], row[5])
                elif region_type == "gmina wiejska":
                    new_region = GminaWiejska(row[0], row[1], row[2], row[3], row[4], row[5])
                elif region_type == "gmina miejsko-wiejska":
                    new_region = GminaMiejskoWiejska(row[0], row[1], row[2], row[3], row[4], row[5])
                elif region_type == "obszar wiejski":
                    new_region = ObszarWiejski(row[0], row[1], row[2], row[3], row[4], row[5])
                elif region_type == "miasto":
                    new_region = Miasto(row[0], row[1], row[2], row[3], row[4], row[5])
                elif region_type == "delegatura":
                    new_region = Delegatura(row[0], row[1], row[2], row[3], row[4], row[5])
                if new_region:
                    Powiat.add_community(new_region)


def list_statistics():
    table_data = [
    ['Count', 'Type'],
    [(len(Wojewodztwo.get_list())), 'województwo'],
    [len(Powiat.get_list()), 'powiaty'],
    [len(GminaMiejska.get_list()), 'gminy miejskie'],
    [len(GminaWiejska.get_list()), 'gminy wiejskie'],
    [len(GminaMiejskoWiejska.get_list()), 'gminy miejsko-wiejskie'],
    [len(ObszarWiejski.get_list()), 'obszary wiejskie'],
    [len(Miasto.get_list()), 'miasta'],
    [len(MiastoNaPrawachPowiatu.get_list()), 'miasta na prawach powiatu'],
    [len(Delegatura.get_list()), 'delegatury']
    ]
    table = AsciiTable(table_data)
    print(table.table)


def display_three_cities_with_longest_names():
    list_of_city_names = [city.get_name() for city in MiastoNaPrawachPowiatu.get_list() + Miasto.get_list()]
    list_of_city_names.sort(key=len, reverse=True)
    print("Three cities with longest names: \n" + '\n'.join(list_of_city_names[:3]))  # 3- how many cities you want display


def display_county_name_with_the_largetst_number_of_communities():
    county_with_largest_communities = None

    for county in Powiat.get_list() + MiastoNaPrawachPowiatu.get_list():
        if county > county_with_largest_communities:
            county_with_largest_communities = county

    print("County with the largest number of communities: {} \nCommunities: {}".format(
        county_with_largest_communities.get_name(),
        len(county_with_largest_communities.get_communities_list()),
    ))


def display_locations_that_belong_to_more_than_one_category():
    locations = [region.get_powiat_id() + region.get_name() for region in Region.get_list_of_all_locations()]
    locations = Counter(locations)  # Create dictionary: key: uniqie region, value: how many is that region
    locations = [id_and_community_name[2:]
                 for id_and_community_name, types_count in locations.items() if types_count > 1]
    print('\n'.join(locations))
    print("There is: {} locations that belong to more than one category.".format(len(locations)))


def advanced_search():
    """
    Create list of locations that have user input in their names.
    """
    user_input = input("Searching for: ")
    locations = [[region.get_name(), region.get_region_type()]
                 for region in Region.get_list_of_all_locations() if user_input.lower() in region.get_name().lower()]
    locations = sorted(locations, key=lambda x: (x[0], x[1]))
    if locations:
        table_data = [['Location', 'Type']] + locations
        table = AsciiTable(table_data)
        print(table.table)
    else:
        print('There is no locations.')


def main():
    load_csv()
    print("""
    What would you like to do:
    (1) List statistics
    (2) Display 3 cities with longest names
    (3) Display county's name with the largest number of communities 
    (4) Display locations, that belong to more than one category
    (5) Advanced search
    (0) Exit program""")
    while True:
        user_option = input("Option: ")
        if user_option == "1":
            list_statistics()
        elif user_option == "2":
            display_three_cities_with_longest_names()
        elif user_option == "3":
            display_county_name_with_the_largetst_number_of_communities()
        elif user_option == "4":
            display_locations_that_belong_to_more_than_one_category()
        elif user_option == "5":
            advanced_search()
        elif user_option == "0":
            quit()
        else:
            print("Bad input, enter correct value.")


if __name__ == "__main__":
    main()
