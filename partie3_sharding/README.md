# Partie 3 : Sharding 

## Architecture
- 1 Config Server
- 2 Shards (Parisx3 / Lyonx3)
- 1 Mongos (routeur)

CONFIG SERVER (ReplicaSet)
    ↓
MONGOS (Routeur)
    ↓
    ├─→ SHARD 1 (ReplicaSet Paris)
    │   ├─ shard1_node1 (PRIMARY)
    │   ├─ shard1_node2 (SECONDARY)
    │   └─ shard1_node3 (SECONDARY)
    │
    └─→ SHARD 2 (ReplicaSet Lyon)
        ├─ shard2_node1 (PRIMARY)
        ├─ shard2_node2 (SECONDARY)
        └─ shard2_node3 (SECONDARY)



## Lancement
```bash
docker-compose up -d
```

## Vérification
```bash
docker exec -it mongos mongosh
sh.status()
```
