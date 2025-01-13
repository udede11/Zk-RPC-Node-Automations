# Basic Health Checks
docker compose ps
docker compose logs zknode
docker ps --filter "name=zknode" --format "{{.Status}}"

# Check Replicas
docker compose ps zknode | grep "Up" | wc -l

# Resource Usage
docker stats --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}"


