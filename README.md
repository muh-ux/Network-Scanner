# Network-Port Scanner

A simple Python-based network port scanner that checks a target host for open TCP ports. I built this to practice Python, networking basics, and introductory cybersecurity concepts.

## Features

- Scan a target IP or hostname
- Detect open TCP ports
- Command-line interface
- Beginner-friendly codebase to learn port scanning

## How It Works

The script uses Python and the Nmap library to scan a target and list which ports respond as open. It is meant for learning basic network reconnaissance only.

## Requirements

- Python 3
- [Nmap](https://nmap.org/) installed on your system
- `python-nmap` Python package

Install the Python dependency with:

```bash
pip install python-nmap
```

## Usage

1. Make sure Nmap is installed and added to your system PATH.
2. Run the script from the terminal:

```bash
python Port-Scanner.py
```

If your script takes a target IP or hostname as an argument, you can run:

```bash
python Port-Scanner.py 192.168.1.1
```

## Example Output

```text
Enter target IP: 192.168.1.1
Scanning...

Open ports found:
22/tcp
80/tcp
443/tcp
```

## Why I Built This

I created this project to:

- Practice Python scripting
- Understand how port scanning works
- Learn more about network services and basic security testing

## Disclaimer

This tool is for educational and authorized testing **only**.  
Do not scan systems, networks, or devices that you do not own or do not have explicit permission to test.