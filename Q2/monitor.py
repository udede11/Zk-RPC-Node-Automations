#!/usr/bin/env python3

import subprocess
import time
import logging
import sys
import os
import json
import requests
import re
from datetime import datetime
from typing import Optional, Dict, Any
from dataclasses import dataclass

@dataclass
class ServiceStatus:
    is_running: bool
    error_type: Optional[str]
    pid: Optional[int]
    memory_usage: Optional[float]
    cpu_usage: Optional[float]

class BlockchainServiceMonitor:
    def __init__(self, service_name: str, slack_webhook: str):
        self.service_name = service_name
        self.slack_webhook = slack_webhook
        
        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('/var/log/blockchain-monitor.log', mode='a'),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)

    def check_service_status(self) -> ServiceStatus:
        """Check if the service is running and collect metrics."""
        try:
            # Get service status using systemctl
            result = subprocess.run(
                ['systemctl', 'status', self.service_name],
                capture_output=True,
                text=True,
                check=False
            )
            
            # Log the status check result for debugging
            self.logger.debug(f"This is the status check result: {result.stdout}")
            
            # Parse service status
            is_running = 'active (running)' in result.stdout
            pid = None
            error_type = None
            
            if not is_running:
                if 'Failed to start' in result.stdout:
                    error_type = 'startup_failure'
                elif 'crashed' in result.stdout:
                    error_type = 'service_crash'
                elif 'configuration error' in result.stdout:
                    error_type = 'config_error'
                else:
                    error_type = 'unknown_failure'
                    
            # Get resource usage if service is running
            if is_running:
                pid_match = re.search(r'Main PID: (\d+)', result.stdout)
                if pid_match:
                    pid = int(pid_match.group(1))
                    resource_usage = self.get_resource_usage(pid)
                    return ServiceStatus(
                        is_running=True,
                        error_type=None,
                        pid=pid,
                        memory_usage=resource_usage['memory'],
                        cpu_usage=resource_usage['cpu']
                    )
                else:
                    self.logger.warning("PID not found in systemctl output")
                    
            return ServiceStatus(
                is_running=is_running,
                error_type=error_type,
                pid=pid,
                memory_usage=None,
                cpu_usage=None
            )
            
        except Exception as e:
            self.logger.error(f"Error checking service status: {str(e)}")
            return ServiceStatus(False, 'monitor_error', None, None, None)

    def get_resource_usage(self, pid: int) -> Dict[str, float]:
        """Get memory and CPU usage for a process."""
        try:
            result = subprocess.run(
                ['ps', '-p', str(pid), '-o', '%mem,%cpu'],
                capture_output=True,
                text=True,
                check=True
            )
            mem, cpu = result.stdout.split('\n')[1].strip().split()
            return {'memory': float(mem), 'cpu': float(cpu)}
        except Exception as e:
            self.logger.error(f"Error getting resource usage: {str(e)}")
            return {'memory': 0.0, 'cpu': 0.0}

    def restart_service(self) -> bool:
        """Restart the blockchain service."""
        try:
            subprocess.run(
                ['sudo', 'systemctl', 'restart', self.service_name],
                check=True
            )
            return True
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Failed to restart service: {str(e)}")
            return False

    def notify_team(self, status: ServiceStatus, restart_success: bool):
        """Send notification to Slack."""
        try:
            message = {
                "text": (
                    f"🚨 *Blockchain Service Alert*\n"
                    f"Service: {self.service_name}\n"
                    f"Status: {'Restarted' if restart_success else 'Failed to restart'}\n"
                    f"Error Type: {status.error_type}\n"
                    f"Time: {datetime.now().isoformat()}"
                )
            }
            
            if self.slack_webhook != "test": 
                response = requests.post(self.slack_webhook, json=message)
                response.raise_for_status()
           
            self.logger.info(f"Message sent to slack: ", message)

        except Exception as e:
            self.logger.error(f"Failed to send notification: {str(e)}")

    def run_monitor(self):
        """Main monitoring loop."""
        while True:
            try:
                status = self.check_service_status()
                self.logger.info(f"Service status: Running={status.is_running}, Error={status.error_type}")
                
                if not status.is_running:
                    self.logger.warning(
                        f"Service down. Error type: {status.error_type}"
                    )
                    restart_success = self.restart_service()
                    self.notify_team(status, restart_success)
                    
                    if restart_success:
                        self.logger.info("Service restarted successfully")
                    else:
                        self.logger.error("Failed to restart service")
                
                time.sleep(30)  # Check every 30 seconds
                
            except Exception as e:
                self.logger.error(f"Monitor loop error: {str(e)}")
                time.sleep(60)  # Wait longer on error

if __name__ == "__main__":
    # Configuration should be moved to environment variables or config file
    SERVICE_NAME = "dummy-blockchain-node"
    SLACK_WEBHOOK = os.environ.get('SLACK_WEBHOOK_URL', 'test')
    
    monitor = BlockchainServiceMonitor(SERVICE_NAME, SLACK_WEBHOOK)
    monitor.run_monitor()
