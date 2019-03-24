# Psuedorandom Password Generator

Generate a psuedorandom password using either /dev/urandom or /dev/random for extra security.

<strong>Note: This is not for professional use. I make no guarantees or promises about the security of passwords generated using this tool.</strong>

## Installation:
1. Ensure you have Python 3.6 installed
2. Add ./getpwd to your `/usr/local/bin`: `sudo cp ./getpwd /usr/local/bin`
3. Ensure that the file is executable: `sudo chmod 755 /usr/local/bin/getpwd`
4. Generate a psuedorandom password!: `getpwd 10`

## Command Line Usage
```
usage: getpwd [-h] [-e] length

positional arguments:
  length              Desired length of randomly generated password

optional arguments:
  -h, --help          show this help message and exit
  -e, --extra_secure  Uses /dev/random instead of /dev/urandom for extra
                      security (may take longer)
```

