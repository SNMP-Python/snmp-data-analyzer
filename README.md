# SNMP analyzer tool 🐍

## Installing dependencies and environment 🌲:

### Install git hooks for executing tests and the git commit message
```shell
pip install -r requirements.txt
sudo npm install -g @commitlint/{config-conventional,cli}
pre-commit install && pre-commit autoupdate && pre-commit install --hook-type commit-msg
```
### Set-up trap catcher
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
#### Put trapsh.sh script into /etc/snmp/scripts 
```shell
cd traps
sudo cp trapsh.sh /etc/snmp/scripts
```
#### Run snmpd and snmpdtrap services
```shell
systemctl start snmpd
systemctl start snmpdtrap
```
