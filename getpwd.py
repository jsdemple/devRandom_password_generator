#!/usr/bin/python3.6
# GENERATE A PASSWORD USING /dev/random ON A LINUX/UNIX MACHINE

import argparse


parser = argparse.ArgumentParser()
parser.add_argument('length', type=int,
                    help='Desired length of randomly generated password')
parser.add_argument('-e', '--extra_secure', action='store_true',
                    help='Uses /dev/random instead of /dev/urandom for extra security (may take longer)')
#parser.add_argument('--extra_secure', action='store_true',
#                    help='Uses /dev/random instead of /dev/urandom for extra security (may take longer)')
args = parser.parse_args()
requested_len = args.length
use_devrand = args.extra_secure

# Unicodes for commonly valid password characters
codes = ['\u0021', '\u0022', '\u0023', '\u0024', '\u0025', '\u0026', '\u0027', '\u0028', '\u0029', '\u002A', '\u002B', '\u002C', '\u002D', '\u002E', '\u002F', '\u0030', '\u0031', '\u0032', '\u0033', '\u0034', '\u0035', '\u0036', '\u0037', '\u0038', '\u0039', '\u003A', '\u003B', '\u003C', '\u003D', '\u003E', '\u003F', '\u0040', '\u0041', '\u0042', '\u0043', '\u0044', '\u0045', '\u0046', '\u0047', '\u0048', '\u0049', '\u004A', '\u004B', '\u004C', '\u004D', '\u004E', '\u004F', '\u0050', '\u0051', '\u0052', '\u0053', '\u0054', '\u0055', '\u0056', '\u0057', '\u0058', '\u0059', '\u005A', '\u005B', '\u005C', '\u005D', '\u005E', '\u005F', '\u0060', '\u0061', '\u0062', '\u0063', '\u0064', '\u0065', '\u0066', '\u0067', '\u0068', '\u0069', '\u006A', '\u006B', '\u006C', '\u006D', '\u006E', '\u006F', '\u0070', '\u0071', '\u0072', '\u0073', '\u0074', '\u0075', '\u0076', '\u0077', '\u0078', '\u0079', '\u007A', '\u007B', '\u007C', '\u007D', '\u007E']



def get_random_pwd(length, source='/dev/urandom'):
    pwd = ''
    print('Generating random password with the help of {0}...'.format(source))
    while length > 0:
        with open(source, 'rb') as f:
            rand_bytes = (f.read(2))
        #random integer used to pick unicode by index
        rand_integer = int.from_bytes(rand_bytes, byteorder='big')
        ind = (rand_integer % 94) -1 
        pwd += codes[ind]
        length -= 1
    return pwd
    

if __name__ == "__main__":
    if use_devrand is True:
        pwd = get_random_pwd(requested_len, source='/dev/random')
    else:
        pwd = get_random_pwd(requested_len, source='/dev/urandom')
    print('Your suggested password is:\t{0}'.format(pwd))

