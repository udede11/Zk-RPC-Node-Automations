# Basic node checks
cast block-number --rpc-url http://localhost:8545
cast chain --rpc-url http://localhost:8545
cast chain-id --rpc-url http://localhost:8545

# Check node sync status
cast sync --rpc-url http://localhost:8545

# Get peer count (returns hex)
cast peers --rpc-url http://localhost:8545

# Load testing examples
# Send batch of transactions
export SENDER_KEY=your_private_key
export RECIPIENT=target_address

for i in {1..50}; do
  cast send --private-key $SENDER_KEY \
    --rpc-url http://localhost:8545 \
    $RECIPIENT \
    --value 0.01ether
done

# Monitor block information during load
cast block latest --rpc-url http://localhost:8545

# Check gas prices
cast gas-price --rpc-url http://localhost:8545

# Check transaction status
cast receipt <TX_HASH> --rpc-url http://localhost:8545
