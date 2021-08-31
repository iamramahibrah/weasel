# weasel
<img src="https://user-images.githubusercontent.com/50782324/124796357-bf547a00-df59-11eb-93c6-ecdcdc07756e.png" width="200">

#### Weasel Framework: Vulnerability Scanning and Security Audit Tool

![license](https://img.shields.io/github/license/mashape/apistatus.svg)
![os](https://img.shields.io/badge/OS-Linux-yellow.svg)
![language](https://img.shields.io/badge/bash-5.1.4(1)%2B-blue.svg)
![raccoonver](https://img.shields.io/badge/version-0.1-lightgrey.svg)
[![made-with-bash](https://img.shields.io/badge/Made%20with-bash-1f425f.svg)](http://golang.org)


#### Features

- CSS Injection Vulnerability scanner
- XSS Vulnerability scanner
- CVE Vulnerability Scanner
- Heartbleed Vulnerability Scanner
- Services and Version scan
- Detect WAF
- Hosts Discovery

#### Installation

```
git clone git@github.com:iamramahibrah/weasel.git
cd weasel
python3 install.py
```

#### Usage

````
    ./weasel [options] -Help
             --css-injection  | Scan CSS Injection Vulnerability
             --cve-scanner    |  Scan for Common Vulnerability Exposure *NOTE: scan all vulnerabilities available in target*
             --xss-vuln       |  XSS Vulnerability scanning 
             --heartbleed     |  Scan Heartbleed vulnerability
             --services       |  Scan for Services and Versions 
             --hostdiscover   |  Get Hosts in network 



````

