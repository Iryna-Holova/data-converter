import csv
from convertor import distance, temperature
from check_input import get_numeric_input


def split_value_unit(string: str) -> tuple[float, str]:
    for i, char in enumerate(string):
        if not char.isdigit():
            value = float(string[:i])
            unit = string[i:]
            return value, unit


def convert_field(field: str, target: str) -> str:
    convert_to = {
        '°C': temperature.celsius_to_fahrenheit,
        '°F': temperature.fahrenheit_to_celsius,
        'm': distance.meters_to_feet,
        'ft': distance.feet_to_meters
    }
    value, unit = split_value_unit(field)
    if unit != target:
        converted_value = convert_to[unit](value)
        field = f'{converted_value}{target}'
    return field


def convert_data(target_dist: str = None, target_temp: str = None):
    result = []
    with open('data.csv', 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if target_dist:
                row['Distance'] = convert_field(row['Distance'], target_dist)
            if target_temp:
                row['Reading'] = convert_field(row['Reading'], target_temp)
            result.append(row)

    with open('converted_data.csv', 'w', newline='', encoding='utf-8') as file:
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(result)


if __name__ == "__main__":
    dist_options = {
        1: 'm',
        2: 'ft',
        0: None
    }
    temp_options = {
        1: '°C',
        2: '°F',
        0: None
    }

    print("\nSelect options for distance:\n")
    print("1. Convert to meters")
    print("2. Convert to feet")
    print("0. Skip distance conversion")
    target_dist = get_numeric_input("\nEnter option number: ")
    while target_dist not in dist_options:
        print("Invalid option. Please enter a valid option number.")
        target_dist = get_numeric_input("\nEnter option number: ")

    print("\nSelect options for temperature:\n")
    print("1. Convert to Celsius")
    print("2. Convert to Fahrenheit")
    print("0. Skip temperature conversion")
    target_temp = get_numeric_input("\nEnter option number: ")
    while target_temp not in temp_options:
        print("Invalid option. Please enter a valid option number.")
        target_temp = get_numeric_input("\nEnter option number: ")

    convert_data(
        target_dist=dist_options[target_dist],
        target_temp=temp_options[target_temp]
    )
