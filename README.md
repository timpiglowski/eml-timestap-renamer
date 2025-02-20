# eml-timestamp-renamer
[![CC BY-NC-SA 4.0][cc-by-nc-sa-shield]][cc-by-nc-sa] [![status: hibernate](https://github.com/GIScience/badges/raw/master/status/hibernate.svg)](https://github.com/GIScience/badges#hibernate)

This Python script extracts timestamps from .eml files and renames the files for better chronological organization. This is particularly useful when exporting .eml files from Apple Mail, which lack timestamps and hence are not sorted chronologically.

## Dependencies
- dateutil library

## Usage
To run the script, use the following command:
```bash
python3 eml-timestamp-renamer.py <input_directory> <output_directory>
```

## License
This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png
[cc-by-nc-sa-shield]: https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg
