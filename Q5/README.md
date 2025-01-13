Here's the README.md with a table of contents added:

# Question 5 

This repository contains tools and scripts for investigating performance issues in blockchain operations, specifically for the CDK-Erigon client.

## Table of Contents

1. [Contents](#contents)
2. [Usage](#usage)
   - [Performance Issue Report](#performance-issue-report)
   - [Tracing and Performance Measurement](#tracing-and-performance-measurement)
3. [Investigation Steps](#investigation-steps)
4. [Optimization Steps](#optimization-steps)
5. [Reporting to Development Team](#reporting-to-development-team)
6. [Contributing](#contributing)
7. [License](#license)

## Contents

1. `report.md`: A template for reporting performance issues to the development team.
2. `run-and-trace.sh`: A shell script containing commands for tracing and measuring performance of the node.

## Usage

### Performance Issue Report

The `report.md` file provides a structured template for documenting performance issues. It includes sections for:

- Issue Summary
- Reproduction Steps
- Trace Analysis

### Tracing and Performance Measurement

The `run-and-trace.sh` script contains various commands for tracing and measuring performance:

1. Get execution trace with timing:
   ```
   cast rpc debug_traceTransaction <tx-hash> --rpc-url http://localhost:8545
   ```

2. System metrics during execution:
   - Disk I/O: `iostat -x 1`
   - Virtual memory stats: `vmstat 1`
   - CPU usage per thread: `top -H -p <pid>`

3. CPU profiling:
   ```
   perf record -g -p <pid>
   perf report
   ```

4. Memory profiling:
   ```
   heaptrack <process>
   ```

## Investigation Steps

When encountering high latency in a particular blockchain operation:

1. Analyze the execution trace to identify the specific operation causing the delay.
2. Use system monitoring tools to check resource usage during the operation.
3. Profile CPU and memory usage to identify potential bottlenecks.
4. Review node configuration settings that might affect the operation's performance.
5. Examine the client code related to the operation for potential optimizations.

## Optimization Steps

After identifying the bottleneck, consider the following optimization steps:

1. Node Configuration Issues:
   - Adjust cache sizes
   - Modify garbage collection settings
   - Update sync modes
   - Tune transaction pool settings

2. Client Software Issues:
   - Identify specific functions or modules causing the delay
   - Look for inefficient algorithms or data structures
   - Check for unnecessary computations or database operations
   - Consider optimizing critical paths in the code

3. Hardware Constraints:
   - Evaluate if the hardware meets the recommended specifications
   - Consider upgrading CPU, RAM, or storage if necessary

## Reporting to Development Team

When reporting issues to the CDK-Erigon development team:

1. Provide a detailed description of the high-latency operation
2. Include the full execution trace
3. Share system specifications and node configuration
4. Provide profiling results (CPU and memory)
5. Include any relevant logs or error messages
6. Describe steps to reproduce the issue
7. Share any attempted optimizations and their results

## Contributing

If you identify any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

The MIT License (MIT)
