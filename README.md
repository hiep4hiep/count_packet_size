# count_packet_size
Count PAN packet size based on exported log

My customers want a report of transaction size per destination IP address because it will affect network security performance of NGFW, LB especially with SSL decryption enabled.
This script helps parse traffic log (csv format) to get transaction size (from 0-100byte, 100-500byte... upto 10MB) in number of packets. These number can be input
to excel and report percentage of transaction size. IT admin can get back to software development team to fine tune their code/transaction method to optimize performance.

Usage:
1. Export traffic log from Palo Alto Networks NGFW
2. Name it traffic_log_filter.csv
3. Put the file in same folder with script
4. Run python count_packet.py
5. Input your IP address you want to check. The script will return dictionary format or json with number of transaction per size.
