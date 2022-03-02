#!/usr/bin/python3

import subprocess as sp
import sys
import os

def main(): 
    # All commands, you need to have cert.sh in the same folder as this script
    find = sp.getoutput('./crt.sh {} > certsh-all.txt'.format(sys.argv[1])) # find all subdomains and put them in all.txt
    count = sp.getoutput("./crt.sh {} | wc -l".format(sys.argv[1]))  # find all subdomains and count them
    probe = sp.getoutput("./crt.sh {} | ~/go/bin/httprobe > certsh-alive.txt".format(sys.argv[1])) # find all subdomains and probe them(filter the alive ones)
    countProbe = sp.getoutput("./crt.sh {} | ~/go/bin/httprobe | wc -l".format(sys.argv[1])) # find all alive subdomains and count them

    # Outputting all the results
    print("Found: \n", sp.getoutput("cat certsh-all.txt"))
    print("Subdomain count: " + str(count) + ".\n")
    print("Alive: \n", sp.getoutput("cat certsh-alive.txt"))
    print("Alive domain count: " + str(countProbe) + ".")

    # Write the total subdomain count in all.txt
    domain_file = open("certsh-all.txt", 'a')
    domain_file.write("Subdomain count: {}\n".format(str(count)))
    domain_file.close()
    
    # Write alive subdomain count in alive.txt
    alive_file = open("certsh-alive.txt", 'a')
    alive_file.write("Alive domain count: {}\n".format(str(countProbe)))
    alive_file.close()

if __name__ == "__main__":
    main()