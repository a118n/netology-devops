#!/usr/bin/env python3

import json
import yaml
from sys import argv
from os import path

if len(argv) < 2:
    print("You have to provide a path to the file you want to convert. Exiting.")
elif not path.isfile(argv[1]):
    print(f"File {argv[1]} doesn't exist. Exiting.")
else:
    file_path = argv[1]
    try:
        with open(file_path) as f:
            data = json.load(f)
            print("Got JSON, Exporting as YAML...")
            output_file = f"{file_path.split('.')[0]}.yml"
            with open(output_file, "w") as o:
                yaml.dump(data, o)
    except json.JSONDecodeError as e:
        print(f"Error: {e.msg} at line {e.lineno}")
        print("Failed to import JSON, will try YAML next...")
        try:
            with open(file_path) as f:
                data = yaml.safe_load(f)
                print("Got YAML, Exporting as JSON...")
                output_file = f"{file_path.split('.')[0]}.json"
                with open(output_file, "w") as o:
                    json.dump(data, o, indent=4)
        except yaml.parser.ParserError as e:
            print(f"Error: {e.problem} at line {e.problem_mark.line}")
            print(
                "Failed to import file. Check if the file is valid JSON or YAML. Exiting.")
