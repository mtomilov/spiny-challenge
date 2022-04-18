
# Notes

## Commands

From the top directory  
Run:  
`$ docker-compose up -d`  
Debug:  
`$ docker-compose -f docker-compose.yml -f docker-compose-dev.yml up`  
Inspect cron logs:  
`$ docker-compose exec app tail -F /var/log/pull_trends.log`  
Invoke pull trends:  
`$ docker-compose exec app python -m tasks.pull_trends`  

## Apis

`/apis/search_interest/<keyword>`  
`/ping`  

## Why mongo?

Great for prototyping, would switch to redis for speed and to postgres for relational data.

## Why flask?

I think it's perfect for lightweight apis. We certainly don't want to pull all of django if we end up using 10% of it.

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
