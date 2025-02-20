# eml-timestamp-renamer
[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/) [![status: hibernate](https://github.com/GIScience/badges/raw/master/status/hibernate.svg)](https://github.com/GIScience/badges#hibernate)

This Python script extracts timestamps from .eml files and renames the files for better chronological organization. This is particularly useful when exporting .eml files from Apple Mail, which lack timestamps and hence are not sorted chronologically.

## Dependencies
- dateutil library

## Usage
To run the script, use the following command:
```bash
python3 eml-timestamp-renamer.py <input_directory> <output_directory>
```
