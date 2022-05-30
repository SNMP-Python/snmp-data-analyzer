# SNMP analyzer tool 🐍

## Installing dependencies and environment 🌲:

### Install git hooks for executing tests and the git commit message
```shell
pip install -r requirements.txt
sudo npm install -g @commitlint/{config-conventional,cli}
pre-commit install && pre-commit autoupdate && pre-commit install --hook-type commit-msg
```

