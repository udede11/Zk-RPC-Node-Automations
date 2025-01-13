# Get execution trace with timing
cast rpc debug_traceTransaction <tx-hash> \
    --rpc-url http://localhost:8545

# System metrics during execution
iostat -x 1     # Disk I/O
vmstat 1        # Virtual memory stats
top -H -p <pid> # CPU usage per thread


# CPU profiling
perf record -g -p <pid>
perf report

# Memory profiling
heaptrack <process>
