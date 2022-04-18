#!/usr/bin/env bash

printenv | grep -v 'no_proxy' > /etc/environment  # export env vars for cron
service cron start
cat pull_trends.cron | crontab
python -u app.py
