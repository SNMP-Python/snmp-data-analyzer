# SNMP analyzer tool 🐍

## Installing dependencies and environment 🌲:

### Install git hooks for executing tests and the git commit message
```shell
pip install -r requirements.txt
sudo npm install -g @commitlint/{config-conventional,cli}
pre-commit install && pre-commit autoupdate && pre-commit install --hook-type commit-msg
```
### Set-up trap catcher 🥅
#### Copy snmptrapd.conf file into /etc/snmp
```shell
cd traps
sudo cp snmptrapd.conf /etc/snmp
```
#### Create scripts folder in /etc/snmp
```shell
cd /etc/snmp
sudo mkdir scripts
```
#### Change trapsh.sh echo path inside the script
```shell
echo "" >> /home/youruser/logs.txt
```
#### Put trapsh.sh script into /etc/snmp/scripts 
```shell
cd traps
sudo cp trapsh.sh /etc/snmp/scripts
```
#### Run snmpd and snmpdtrap services
```shell
systemctl start snmpd
systemctl start snmptrapd
```
#### Run the script  trapsparser.py located inside /traps
#### With logs.txt in the same folder
```shell
python3 traps_parser.py
```
#### Check the output and see all traps info 🦆
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
