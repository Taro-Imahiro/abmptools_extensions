import os
import re

def read_and_create_script():
    log_dir = './log_dat/'
    log_file_pattern = re.compile(r"abmp-frag(\d+)\.log")

    def sort_key(name):
        match = log_file_pattern.match(name)
        return int(match.group(1)) if match else float('inf')

    log_files = sorted(filter(log_file_pattern.match, os.listdir(log_dir)), key=sort_key)

    # Create/overwrite abmp_lipid_protein.sh with the sh shebang
    with open("abmp_lipid_protein.sh", "w") as file:
        file.write("#!/bin/sh\n")

    for log_file in log_files:
        num_frag, num_tip = 0, 0
        prod_file = ''
        with open(os.path.join(log_dir, log_file), "r") as file:
            for line in file:
                if line.startswith("num_fragment"):
                    num_frag = int(next(file))
                elif line.startswith("TIP"):
                    match = re.findall("\[\s*(\d+)\s*\]", line)
                    num_tip = int(match[0]) if match else 0
                elif line.startswith("infile:"):
                    prod_file = line.strip().split()[-1]

        # Subtract num_tip from num_frag
        result = num_frag - num_tip

        # Append new command to abmp_lipid_protein.sh
        with open("abmp_lipid_protein.sh", "a") as file:
            file.write(f"python -m abmptools.getifiepieda --frag 444-{result} 1-442 -i ./fmolog/{prod_file}\n")

read_and_create_script()
