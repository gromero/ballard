import argparse
import os

parser = argparse.ArgumentParser(description='Swap Z Gcode by M3 or M5 Gcode')
parser.add_argument('-d', action='store_true', help="enable debug mode")
parser.add_argument('--file',
        required=True,
        metavar="GCODE_FILE",
        help="specify input file with Z Gcodes")
c = parser.parse_args()
print("Reading", c.file)

filename = c.file
st = os.path.splitext(filename)
output = st[0] + "_output" + st[1]

with open(filename, "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        if "Z" in line:
            if "-" in line:
                if c.d:
                    print("Found Z- at line, patching with M3...", i)
                lines[i] = "M3\n" # Needle down
            else:
                if c.d:
                    print("Found Z at line, patching with M5...", i)
                lines[i] = "M5\n" # Needle up

with open(output, "w") as o:
    for line in lines:
        o.write(line)
