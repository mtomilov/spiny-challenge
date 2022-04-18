#!/usr/bin/env bash
service cron start
cat pull_trends.cron | crontab
python -u app.py
