# abmptools_extensions
ABINIT-MP解析支援ツールの入力支援等

## 1. lipid_frag_counter.py -- Python Script for Processing Log Files
This Python script reads files in the format abmp-frag*.log, which are output during fragment creation, extracts fragment information from these files, and uses that information to generate a abmp_lipid_protein.sh.

### 1-1. How this Script Works
The script finds all abmp-frag*.log files in the log_dat directory.

For each log file, the script reads the file line by line. It looks for lines that start with "num_fragment", "TIP", and "infile:", and extracts information from those lines.

The script calculates a result by subtracting the number found in the "TIP" line from the number found in the "num_fragment" line.

### 1-2. Requirements
- Installed Python 3.6 or later

- Availability of os and re modules from Python's standard library


### 1-3. Usage
**Please change the directory names and log file names in the program as needed.**
```
python lipid_frag_counter.py
```

### 1-4. Output Example
Example content of abmp_lipid_protein.sh
```{bash}
#!/bin/sh
python -m abmptools.getifiepieda --frag 444-1009 1-442 -i ./fmolog/Snapshot0-fmo.log
python -m abmptools.getifiepieda --frag 444-1045 1-442 -i ./fmolog/Snapshot1-fmo.log
python -m abmptools.getifiepieda --frag 444-1085 1-442 -i ./fmolog/Snapshot2-fmo.log
python -m abmptools.getifiepieda --frag 444-1030 1-442 -i ./fmolog/Snapshot3-fmo.log
python -m abmptools.getifiepieda --frag 444-1079 1-442 -i ./fmolog/Snapshot4-fmo.log
python -m abmptools.getifiepieda --frag 444-1052 1-442 -i ./fmolog/Snapshot5-fmo.log
...
```