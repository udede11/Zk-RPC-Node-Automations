# Basic Health Checks
docker compose ps
docker compose logs zknode
docker ps --filter "name=zknode" --format "{{.Status}}"

# Check Replicas
docker compose ps zknode | grep "Up" | wc -l

# Resource Usage
docker compose stats --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}"

#Network connectivity
docker exec <container1_name> ping -c 4 <container2_name>


