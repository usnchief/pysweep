import subprocess   
import time
import re

#Make a list to store ping sweep results
results = []
network_ip = "172.200.3."
# Make a function to sweep a range of ip's given a network/CIDR
def sweep():
    for ip in range(1, 255):
        ipaddress = network_ip + str(ip)
        ip_list = subprocess.run(["fping", "-C 5", "-q", "-a", ipaddress], capture_output=True, text=True)
        #return sweep reuslts to results list
        print(ip_list)
        
# return results to list above.
#for line in results
   # total_sweeps =+ 1
  #  output = results.stderr
   # split_line = output.split(":")


    











if __name__ == '__main__':
    sweep()