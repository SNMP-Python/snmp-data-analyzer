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
### Copy snmpd.conf file into /usr/share/snmp changing trap2sink interface for receiver interface (trap sender interface).
```shell
trap2sink rocom trap_sender_interface
sudo cp snmpd.conf /usr/share/snmp
```
### Copy snmptrapd.conf file into /etc/snmp
```shell
cd traps
sudo cp snmptrapd.conf /etc/snmp
```
### Copy snmpd.conf file into /usr/share/snmp
```shell
cd traps
sudo cp snmpd.conf /usr/share/snmp
```
### Create scripts folder and copy scripts in /etc/snmp/scripts
```shell
cd /etc/snmp/
sudo mkdir scripts
sudo cp traps_parser /etc/snmp/scripts
sudo cp dictionaries.py /etc/snmp/scripts
sudo cp states_enums.py /etc/snmp/scripts
```
### Run snmpd and snmpdtrap services
```shell
systemctl start snmpd
systemctl start snmptrapd
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
