# Data Converter

This command-line tool converts data from a CSV file, specifically designed for converting distance and temperature values.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Iryna-Holova/data-converter.git
```

2. Navigate to the project directory:

```bash
cd data-converter
```

## Usage

Run the script `main.py` and follow the prompts to select the conversion options for distance and temperature.

### Options for Distance:

- 1: Convert to meters
- 2: Convert to feet
- 0: Skip distance conversion

### Options for Temperature:

- 1: Convert to Celsius
- 2: Convert to Fahrenheit
- 0: Skip temperature conversion

Example usage:

```bash
python main.py
```

Example output:

```csv
`cat converted_data.csv`
```

## File Structure

- `main.py`: Main script to convert data.
- `convertor/`: Package containing conversion functions.
  - `distance.py`: Functions for converting distance values.
  - `temperature.py`: Functions for converting temperature values.
- `data.csv`: Sample CSV file with data to convert.
- `converted_data.csv`: Output file with converted data.
- `check_input.py`: Helper module for handling user input.

## Requirements

- Python 3.x
- csv module
