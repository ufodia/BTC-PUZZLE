# BTC-PUZZLE V1: Bitcoin's puzzle Brute-Force Tool (CPU Version)
Puzzle Solver V1 is a robust, feature-packed Bitcoin private key brute-forcing tool designed to crack specific Bitcoin private keys. It enables users to delve into a specific range of private keys to locate a Bitcoin address of interest.

### Prerequisites
The tool is developed using Python and for its smooth operation, the following Python packages are necessary:


### Usage
Use the following command to run the script:

```
puzzle.exe -k start_hex:end_hex -a target_address -s scan_mode [scan_count] -f output_file
```

### Options:

```
-k, --keyspace start_hex:end_hex 
    Define the range of hex values to be considered for the private keys.

-a, --address target_address 
    Input the target Bitcoin address that you're trying to locate in the given hex range.

-f, --file output_file 
    Specify the name of the output file where the found keys will be stored. Default is find.txt.

-s, --scan scan_mode [scan_count] 
    Choose the mode of operation:
    0 for sequential search - searches the keyspace in an ordered manner,
    1 for random search - searches the keyspace randomly,
    2 for hybrid search - switches between sequential and random search periodically.
    Additional argument: number of keys for hybrid mode (in millions).
   ```
   
### Example
To give you a better understanding of how to use these options, here's an example command (for puzzle 66):
```
puzzle.exe -k 20000000000000000:3ffffffffffffffff -a 13zb1hQbWVsc2S7ZTZnP2G4undNNpdh5so -s 2 10 -f puzzle66.txt
```
#### Note 1: The CUDA and OpenCL versions are under coding.
#### Note 2: The code is Python templated, so you can run as many instances of the code as the number of cores you have. For example, if you have an 8-core processor, you can run the code in 8 separate command prompt windows. The use of a part builder can be helpful for this purpose.
#### Note 3: This tool is meant for educational purposes only. Please ensure you use it responsibly. Misuse of this tool could potentially lead to legal repercussions. The author bears no responsibility for any unlawful activities associated with the misuse of this tool.

# Part Builder: Auxiliary Script for Better Scanning
To assist with the main puzzle solver script, we offer an additional Python script called 'Part Builder'. This script generates .bat files for different parts of a hex range, providing an organized and systematic approach to scan the keyspace.

### Usage
Use the following command to run the script:

```
python puzzlepart.py
```

During the execution, the script will prompt you to provide:

Starting and ending hex values to define the range for each part.

Number of parts you want to divide the range into.

Target Bitcoin address.

File name where to store the found keys.

Scan mode (sequential, random, hybrid).

If hybrid mode is chosen, the number of keys to be scanned per cycle.

### Disclaimer: The Part Builder script generates startup scripts that may consume a significant amount of system resources. It's recommended to monitor your system's performance regularly and use this feature judiciously.

### Support and Contribution
If you find this project useful and wish to support it, consider making a donation. Every contribution, regardless of size, isgreatly appreciated!

**BTC**: 1JKdcuaw289Daf5eSCpuULTam5LnCxCgY3

**Lottery**: https://Millionmac.com

### Contact
For any inquiries or comments, reach out to info@millionmac.com.
  
