import os
import time
import random
import argparse
import re
from bit import Key

def valid_hex_range(option):
    match = re.fullmatch(r'([0-9a-fA-F]+):([0-9a-fA-F]+)', option)
    if match:
        return match.groups()
    raise argparse.ArgumentTypeError(f'Invalid hex range: {option}')

print("Starting program, please wait...")
time.sleep(2)  # wait for 2 seconds

print("Loading Argument parser...")
time.sleep(2)  # wait for 2 seconds

parser = argparse.ArgumentParser(
    description="Puzzle solver  v1 by UFODIA: A tool to generate and search Bitcoin private keys.",
    epilog="Example: Puzzle.exe -k 20000000000000000:3ffffffffffffffff -a 13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so -s 2 10 -f puzzle66.txt",
    formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument("-k", "--keyspace", type=valid_hex_range, help="Specify the range of hex values as start_hex:end_hex.")
parser.add_argument("-a", "--address", type=str, required=True, help="Specify the target Bitcoin address.")
parser.add_argument("-f", "--file", type=str, default="find.txt", help="Specify the output file name for storing found keys. Default is 'find.txt'.")
parser.add_argument("-s", "--scan", nargs='*', default=[0], help="Specify the mode of operation and optionally the number of keys for hybrid mode.0 For sequential search, 1 for random search, 2 for hybrid search. Additional arg: number of keys for hybrid mode (in millions).")

args = parser.parse_args()

print("Loading Kernel...")
time.sleep(2)  # wait for 2 seconds

start_hex, end_hex = args.keyspace
target_address = args.address
output_file = os.path.expanduser(f'~/Desktop/{args.file}')
scan_mode = int(args.scan[0])
scan_count = int(args.scan[1]) * 1000000 if len(args.scan) > 1 else 0

# Descriptive string for the scan mode
scan_str = 'Sequential' if scan_mode == 0 else 'Random' if scan_mode == 1 else f'Hybrid (Base hex changes every {scan_count//1000000}M hexes)'

print(f"\nUFODIA KEYS v1.0\n"
      f"https://millionmac.com\n"
      f"-------------------\n"
      f"Target BTC Address  : {target_address:<}\n"
      f"Hex Range           : {start_hex} - {end_hex}\n"
      f"Scan Mode           : {scan_str:<}\n"
      f"Save to             : {output_file:<}\n")

print("Scanning starts...")
time.sleep(2)  # wait for 2 seconds

start_time = time.perf_counter()
hex_count = 0
start_range = int(start_hex, 16)
end_range = int(end_hex, 16)
current_range = start_range
change_count = 0  # Count for the number of changes in hybrid mode
results = []

while True:
    if scan_mode == 0:  # Sequential scan
        i = current_range
        current_range += 1
        if current_range > end_range:
            break
    elif scan_mode == 1:  # Random scan
        i = random.randint(start_range, end_range)
    elif scan_mode == 2:  # Hybrid scan
        if hex_count % scan_count == 0 or current_range > end_range:
            current_range = random.randint(start_range, end_range)
            change_count += 1
        i = current_range
        current_range += 1
        if current_range > end_range:
            continue

    # Convert i to a private key and derive the associated address
    priv_key_hex = format(i, 'x').zfill(64)
    key = Key.from_hex(priv_key_hex)
    address = key.address

    hex_count += 1

    
    if address == target_address:
        print(f'\nPrivate Key: {priv_key_hex}, Address: {address}')
        result_string = f'Private Key: {priv_key_hex}, Address: {address}\n'
        with open(output_file, 'a') as f:
            f.write(result_string)
            
    def format_keys_per_second(kps):
        if kps < 1e3:
            return f"{kps:.2f}"
        elif kps < 1e6:
            return f"{kps/1e3:.2f}K"
        elif kps < 1e9:
            return f"{kps/1e6:.2f}M"
        else:
            return f"{kps/1e9:.2f}B"
            
    # Print the progress every 20000 keys
    if hex_count % 20000 == 0:
        elapsed_time = time.perf_counter() - start_time
        elapsed_time = elapsed_time if elapsed_time > 0 else 1
        formatted_time = f'{int(elapsed_time // 3600)}:{int((elapsed_time % 3600) // 60):02d}:{int(elapsed_time % 60):02d}'
        formatted_hex_count = f'{hex_count:,}'.replace(',', '.')
        keys_per_second = hex_count / elapsed_time
        formatted_kps = format_keys_per_second(keys_per_second)
        
        # Add the change count to the output if in hybrid mode
        change_count_str = f'R= {int(hex_count/scan_count)}' if scan_mode == 2 else ''

        display_key_hex = priv_key_hex.lstrip('0')
        display_key_hex = display_key_hex if display_key_hex else '0'  # ensure at least one zero remains if all zeros were stripped
        print(f'\r{change_count_str} [Scanned {formatted_hex_count} keys in {formatted_time}] [{formatted_kps} Keys/s.] [Current Hex: {display_key_hex}]', end='')


print("\nSuccessfully finished.")
