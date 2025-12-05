# Partie 2 : Réplication (Haute disponibilité)

## Architecture
- 3 nœuds MongoDB en ReplicaSet
- 1 Arbiter pour les votes
- Total : 105,858 documents (Paris + Lyon)

## Lancement
```bash
docker-compose up -d
```

## Vérification
```bash
docker exec -it mongo1 mongosh
rs.status()
```
