## Usage 📕
# SNMP analyzer tool 🐍

## Summary
- [Installing the dependencies](#installing-dependencies-and-environment-for-the-snmp-analyzer)
- [Set Up the Trap Catcher](#set-up-the-trap-catcher-)
- [Usage](#usage-)
- [License](#license-)

## Installing dependencies and environment for the snmp analyzer🌲:

### Install the development and build dependencies 📦
```shell
pip install -r requirements.txt
```

### Install the git hooks for following the development standards 🧍
```shell
sudo npm install -g @commitlint/{config-conventional,cli}
pre-commit install && pre-commit autoupdate && pre-commit install --hook-type commit-msg
```
## Set up the trap catcher 🥅
### Copy the trap configuration and parser files
```shell
cd traps
# copy configuration files
sudo cp snmptrapd.conf /etc/snmp
sudo cp snmpd.conf /usr/share/snmp

# copy parser files
sudo mkdir /etc/snmp/scripts
sudo cp traps_parser /etc/snmp/scripts
sudo cp *.py /etc/snmp/scripts
```

### Start the snmpd and snmpdtrap services
```shell
sudo systemctl start snmpd
sudo systemctl start snmptrapd
```
### Give executable permissions to the traps_parser script in case it doesn't have permissions
```shell
cd /etc/snmp/scripts
sudo chmod +x traps_parser
```
### Check output and see traps info in /var/log/logs_parsed.txt 🦆
```shell
----------------------------------------------------
IF STATE CHANGE
ROUTER ID:  12.0.0.1
INTERFACE ID:  12.0.0.1
INTERFACE STATE: BACKUP_DESIGNATED_ROUTER
----------------------------------------------------
IF STATE CHANGE
ROUTER ID:  12.0.0.1
INTERFACE ID:  11.0.0.2
INTERFACE STATE: BACKUP_DESIGNATED_ROUTER
----------------------------------------------------
NEIGHBOR STATE CHANGE
ROUTER ID:  13.0.0.1
OSPF ROUTER STATE: FULL
----------------------------------------------------
```
## Usage 📕
In this section you'll find some examples about how to use the python-snmp-analyzer tool. Be aware that you have to install
the dependencies before you run the tool.

### Execute the tool with the default values
```shell
python main.py
```

### Execute the tool and add directly an ip address
```shell
python main.py --ip 10.0.0.4
```

### Execute the tool and save the output to a file
```shell
python main.py --output output.txt
```

### Execute the tool and save the routes that the program discovers to your routing table
```shell
python main.py --add-routes
```

### Search for help
```shell
python main.py --help
```

## License 👮
The project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for more information.
