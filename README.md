# zytel-dsl
Retrieve JSON formatted WAN information from a Zytel PK5001Z modem

I use this to get information about my DSL modem into Home Assistant

usage: GetWANDSLInfo.py [-h] [-v] host user pw

Retrieve JSON formatted WAN information from a Zytel PK5001Z modem

positional arguments:
  host           DSL modem hostname/IP address
  user           DSL modem user name
  pw             DSL modem password

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  verbose prints debug information

Return data:
{"download": "1.792", "upload": "0.605", "dslStatus": "CONNECTED", "internetStatus": "CONNECTED", "modemIP": "xx.xx.xx.xx", "RemoteIP": "xx.xx.xx.xx"}


## Home assistant
### configuration.yaml
```yaml
sensor:
  - platform: command_line
    name: DSL download
    unit_of_measurement: Mbps
    scan_interval: 300
    command: !secret dsl_command
    value_template: '{{ value_json.download }}'
  - platform: command_line
    name: DSL upload
    unit_of_measurement: Mbps
    scan_interval: 300
    command: !secret dsl_command
    value_template: '{{ value_json.upload }}'
```

### secerts.yaml
```yaml
dsl_command: '/usr/src/dsl/GetWANDSLInfo.py x.x.x.x user password'
```
