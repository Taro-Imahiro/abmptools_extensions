# abmptools_extensions
ABINIT-MP解析支援ツールの入力支援等

## lipid_frag_counter.py -- Python Script for Processing Log Files
This Python script reads files in the format abmp-frag*.log, extracts fragment information from these files, and uses that information to generate a run.sh shell script.

### How the Script Works
The script finds all abmp-frag*.log files in the log_dat directory.

For each log file, the script reads the file line by line. It looks for lines that start with "num_fragment", "TIP", and "infile:", and extracts information from those lines.

The script calculates a result by subtracting the number found in the "TIP" line from the number found in the "num_fragment" line.

### Requirements
Installed Python 3.6 or later

Availability of os and re modules from Python's standard library


### Usage
```
python lipid_frag_counter.py
```