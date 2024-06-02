import argparse
from utils.csv_reader import read_csv
from utils.json_writer import write_json

def main():
    parser = argparse.ArgumentParser(description="Convert CSV file to JSON format.")
    parser.add_argument("input_csv", help="Path to the input CSV file")
    parser.add_argument("output_json", help="Path to the output JSON file")
    parser.add_argument("--pretty", action="store_true", help="Pretty print JSON output")
    
    args = parser.parse_args()
    
    try:
        data = read_csv(args.input_csv)
        write_json(data, args.output_json, args.pretty)
        print(f"Successfully converted {args.input_csv} to {args.output_json}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
