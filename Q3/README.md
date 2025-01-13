# Blockchain Application Docker Configuration

This README provides an overview of the Docker configuration for a blockchain application, including how to modify service configurations and test the modified setup.

## Table of Contents

1. [Modifying Service Configurations](#modifying-service-configurations)
   - [Number of Replicas](#number-of-replicas)
   - [Environment Variables](#environment-variables)
2. [Testing the Modified Setup](#testing-the-modified-setup)
   - [Basic Service Health](#basic-service-health)
   - [Blockchain-Specific Tests](#blockchain-specific-tests)
   - [Network Testing](#network-testing)
   - [Load Testing](#load-testing)
3. [Configuration Files](#configuration-files)
4. [Testing Scripts](#testing-scripts)

## Modifying Service Configurations

### Number of Replicas

To change the number of replicas for a service, modify the `docker-compose.yml` file:

```yaml
services:
  zknode:
    deploy:
      replicas: 3
```

### Environment Variables

Environment variables can be set in multiple ways:

1. Directly in `docker-compose.yml`:

```yaml
services:
  zknode:
    environment:
      - NETWORK_TYPE=testnet
      - ROLLUP_MODE=validium
      - LOG_LEVEL=debug
```

2. Using a `.env` file:

```
NETWORK_TYPE=testnet
RPC_PORT=8545
P2P_PORT=30303
```

3. Using external environment files:

```yaml
services:
  zknode:
    env_file:
      - ./config/node.env
```

## Testing the Modified Setup

### Basic Service Health

Use the `docker-check.sh` script to:
- Check container status and logs
- Verify the correct number of replicas
- Monitor resource usage

### Blockchain-Specific Tests

Use the `blockchain-check.sh` script to:
- Verify RPC endpoint accessibility
- Check network sync status
- Test transaction processing

### Network Testing

- Test P2P connectivity between nodes
- Verify network discovery
- Check block propagation

### Load Testing

The `blockchain-check.sh` script includes examples for:
- Sending test transactions
- Monitoring transaction processing
- Checking system performance under load

## Configuration Files

- `.env`: Environment variables
- `docker-compose.yml`: Service definitions and configurations

## Testing Scripts

- `docker-check.sh`: Basic Docker service health checks
- `blockchain-check.sh`: Blockchain-specific tests and load testing

Refer to these scripts for detailed testing commands and procedures.
