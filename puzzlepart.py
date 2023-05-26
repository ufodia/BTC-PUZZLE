import os

start_hex = int(input("Enter the starting hex value: "), 16)
end_hex = int(input("Enter the ending hex value: "), 16)
parts = int(input("How many parts? "))
address = input("Enter the BTC address: ")
file_name = input("Enter the txt file name: ")
hybrid_count = 0


scan_mode = input("Enter the scan mode (0 for sequential, 1 for random, 2 for hybrid): ")

scan_str = 'Sequential' if scan_mode == '0' else 'Random' if scan_mode == '1' else 'Hybrid'

if scan_mode == '2':
    hybrid_count = int(input("Enter the number of keys per cycle in hybrid mode: (1 for 1M keys)"))

hex_range = end_hex - start_hex
part_range = hex_range // parts

home_dir = os.path.expanduser("~")  # get home directory
startup_dir = os.path.join(home_dir, "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup")  # startup directory path

# Create a directory for .bat files in the current directory
bat_dir = os.path.join(os.getcwd(), "bat_files")
os.makedirs(bat_dir, exist_ok=True)

with open('parts_info.txt', 'w') as f:
    for i in range(parts):
        start_part_hex = format(start_hex + i * part_range, 'x')  # format to hex without '0x'
        end_part_hex = format(start_hex + (i + 1) * part_range - 1, 'x') if i != parts - 1 else format(end_hex, 'x')
        f.write(f"'{i+1}': ('{start_part_hex}', '{end_part_hex}'),\n")
        
        with open(os.path.join(startup_dir, f'{scan_str}_Part{i+1}.bat'), 'w') as startup_bat_file:
            with open(os.path.join(bat_dir, f'{scan_str}_Part{i+1}.bat'), 'w') as bat_file:
                for file in [startup_bat_file, bat_file]:
                    file.write(f"@echo off\n")
                    file.write(f"color 2\n")
                    file.write(f"mode 95,10\n")
                    file.write(f"cd {os.getcwd()}\n")  # Change directory to the script's current directory
                    if scan_mode == '2':
                        file.write(f"puzzle.exe -a {address} -s {scan_mode} {hybrid_count} -f {file_name} -k {start_part_hex}:{end_part_hex}\n")
                    else:
                        file.write(f"puzzle.exe -a {address} -s {scan_mode} -f {file_name} -k {start_part_hex}:{end_part_hex}\n")
