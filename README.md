
# Notes

Why mongo?
Great for prototyping, would switch to redis for speed and to postgres for relational data.

Why docker compose?
Just for demonstration purposes. Would switch to docker swarm and possibly k8s.

Avenues for improvement:
- separate container for tasks
- celery or the like for complex task management
- consider using mongo time series
- consider storing documents by keyword
- refactor layout
- add development docker
