
# Notes

## Why mongo?

Great for prototyping, would switch to redis for speed and to postgres for relational data.

## Why this format?

`{"date": ..., "keyword": ..., "interest": ..., "is_partial": ...}`

For simplicity and provided we have proper indices in place, might just be fine.

## Why cron?

Thought it would be simpler in this context, but regretting it already. :)
Should've gone for separate cron (or celery) container from the get go.

## Why docker compose?

Just for demonstration purposes. Would switch to docker swarm with multiple stages and possibly k8s.
Possible stages:
- build
- tests
- deploy stage
- deploy prod

The first two would run automatically. Deploy stage too if our workflow allows for it.
Deploy prod would be run manually if everything is fine on stage.

## Avenues for improvement:

- separate container for tasks
- celery or the like for complex task management
- consider using mongo time series
- consider storing documents by keyword
- refactor layout
- do not install dev deps by default
- set up proper limit rates
