# Performance Issue Report

## Issue Summary
- Operation Type: [e.g., SSTORE, State Trie Access]
- Normal Latency: XX ms
- Current Latency: XX ms
- Environment Details:
  * CDK-Erigon Version: X.X.X
  * OS: Ubuntu 20.04
  * Hardware: 8 CPU, 16GB RAM
  * Disk: SSD, 500GB

## Reproduction
1. Transaction hash: 0x...
2. Block number: XXXXX
3. Steps to reproduce:
   [Specific steps]

## Trace Analysis
```json
{
  "op": "SSTORE",
  "gasCost": 22100,
  "timing": {
    "total_ms": 150,
    "disk_write_ms": 120,
    "other_ms": 30
  }
}
