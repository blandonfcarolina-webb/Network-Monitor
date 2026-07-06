# Network-Monitor
Automated network monitoring tool that tracks device availability and response times across a local network. Built with Python, it continuously pings a configurable list of devices every 60 seconds, logs results with timestamps, and stores historical data in CSV format for analysis.


## Technologies Used
- **Python 3.x** — monitoring automation, ping execution, and data logging
- **CSV** — lightweight data storage for historical records
- **Cisco Packet Tracer** — network topology design and simulation

## Requirements

- Python 3.6 or higher
- No external libraries required — uses Python standard library only (`subprocess`, `csv`, `datetime`, `time`)

## Installation & Setup

1. Clone the repository:
```bash
   git clone https://github.com/blandonfcarolina-webb/Network-Monitor.git
   cd Network-Monitor
```

2. Open `network_monitor.py` and edit the `DISP` list with your device IPs and labels:
```python
   DISP = [
       ("Router WiFi", "192.168.1.1"),
       ("PC",          "192.168.1.2"),
       ("Device 1",    "192.168.1.3"),
       ("Device 2",    "192.168.1.4"),
   ]
```

3. Run the script:
```bash
   python network_monitor.py
```

---

## How It Works

The script runs in a continuous loop with the following logic on each cycle:

1. **Ping each device** — sends an ICMP ping using `subprocess` and captures the response.
2. **Parse the result** — determines device status (`UP` / `DOWN`) and extracts response time in milliseconds.
3. **Log to CSV** — appends a new row to `network_log.csv` with a timestamp, device name, IP, status, and response time.
4. **Wait 60 seconds** — then repeats the cycle.

Each function in the script has a single responsibility:
- `ping_device(ip)` — executes the ping and returns raw output
- `parse_response(output)` — extracts status and response time from the ping result
- `log_result(...)` — writes one row to the CSV file
- `main()` — runs the monitoring loop

---
## Output Format

Results are saved to `network_log.csv` in the following format:

| Timestamp           | Device      | IP            | Status | Response Time (ms) |
|---------------------|-------------|---------------|--------|--------------------|
| 2025-06-01 10:00:00 | Router WiFi | 192.168.1.1   | UP     | 4.2                |
| 2025-06-01 10:00:00 | PC          | 192.168.1.2   | UP     | 1.8                |
| 2025-06-01 10:00:00 | Device 1    | 192.168.1.3   | DOWN   | —                  |

- **Timestamp** — date and time of the ping cycle
- **Status** — `UP` if the device responded, `DOWN` if it did not
- **Response Time** — round-trip time in milliseconds; `—` if device is unreachable

---

## Network Topology

The default configuration monitors a home network with 4 devices:

| Device      | IP Address    |
|-------------|---------------|
| Router WiFi | 192.168.1.1   |
| PC          | 192.168.1.2   |
| Device 1    | 192.168.1.3   |
| Device 2    | 192.168.1.4   |

The device list is fully configurable — edit the `DISP` variable to match any network setup.

---

## Use Cases

- Home network uptime monitoring
- Basic infrastructure availability tracking
- Learning tool for network monitoring and Python data logging

---

## Author

Carolina Blandon Falcon  
[linkedin.com/in/c-blandon98](https://linkedin.com/in/c-blandon98)


## Screenshots

![Network Topology - Packet Tracer](screenshots/topologia.PNG)

![CSV Log Data](screenshots/csv_file.PNG)

![Monitor Running](screenshots/network_monitor_working.PNG)
