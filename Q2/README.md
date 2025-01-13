# Question 2

This repository contains a Python script and associated files for monitoring and managing a blockchain test service. The system is designed to automatically restart the service if it fails, log the restart events, and notify the team via Slack.

## Table of Contents
- [Features](#features)
- [Files](#files)
- [Setup and Installation](#setup-and-installation)
- [Configuration](#configuration)
- [Logging](#logging)
- [Error Handling and Resilience](#error-handling-and-resilience)
- [Testing with Dummy Service](#testing-with-dummy-service)
- [License](#license)

## Features

- Continuous monitoring of the blockchain service
- Automatic service restart on failure
- Logging of restart events and failure causes
- Slack notifications for service restarts
- Resource usage tracking (CPU and memory)
- Configurable via environment variables and systemd service file

## Files

1. `monitor.py`: The main Python script that performs the monitoring and management tasks.
2. `blockchain-monitor.service`: A systemd service file for running the monitor script as a system service.
3. `start_service.sh`: A shell script to enable and start the monitoring service.
4. `dummy-blockchain-node.service`: A systemd service file that runs a dummy service for testing purposes.

## Setup and Installation

1. Clone this repository to your local machine or server.

2. Ensure Python 3.7+ is installed on your system.

3. Install the required Python packages:
   ```
   pip install requests
   ```

4. Set up the Slack webhook URL as an environment variable:
   ```
   export SLACK_WEBHOOK_URL=your_webhook_url
   ```

5. Copy the `blockchain-monitor.service` file to the systemd directory:
   ```
   sudo cp blockchain-monitor.service /etc/systemd/system/
   ```

6. Make the `start_service.sh` script executable:
   ```
   chmod +x start_service.sh
   ```

7. Run the `start_service.sh` script to enable and start the monitoring service:
   ```
   ./start_service.sh
   ```

## Configuration

- The blockchain service name can be configured in the `monitor.py` file by changing the `SERVICE_NAME` variable.
- The Slack webhook URL is set via the `SLACK_WEBHOOK_URL` environment variable.
- Logging configuration can be adjusted in the `__init__` method of the `BlockchainServiceMonitor` class in `monitor.py`.

## Logging

Logs are written to `/var/log/blockchain-monitor.log` and also output to stdout. You can view the logs using:

```
sudo journalctl -u blockchain-monitor
```

## Error Handling and Resilience

The script includes basic error handling to catch and log exceptions. The monitoring loop will continue running even if errors occur, with a longer sleep time between checks in case of errors.

To ensure the script stays alive after server restarts or errors, it is set up as a systemd service with the `Restart=always` option. This means the operating system will automatically restart the script if it crashes or if the server reboots.

## Testing with Dummy Service

The repository includes a `dummy-blockchain-node.service` file, which runs a dummy service that prints something every 5 seconds. This can be used to test the monitoring script under different scenarios:

1. Copy the `dummy-blockchain-node.service` file to the systemd directory:
   ```
   sudo cp dummy-blockchain-node.service /etc/systemd/system/
   ```

2. Start the dummy service:
   ```
   sudo systemctl start dummy-blockchain-node
   ```

3. You can now test different scenarios by stopping or killing the dummy service:
   ```
   sudo systemctl stop dummy-blockchain-node
   ```
   or
   ```
   sudo systemctl kill dummy-blockchain-node
   ```

This allows you to verify that the monitoring script correctly detects service failures, restarts the service, and sends notifications as expected.

## License

[MIT License](LICENSE)
