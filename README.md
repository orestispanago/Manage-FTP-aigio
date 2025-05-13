# Manage-FTP-aigio

Aigio weather station uploads a ```.dat``` file every 10 minutes to the FTP server.

Each ```.dat``` file contains 1 10-min measurements.

This script downloads the ```.dat``` files locally, and organizes them to daily ```.csv``` files using the filename format: `YYYY/aigio10min_YYYYMMDD.csv`

The generated ```.csv``` files are uploaded to the FTP server and archived locally.

Both the remote and the loca raw ```.dat``` files are deleted after the ```.csv``` upload.



## Instructions

Edit the FTP parameters in ```ftp.py```. 

To run every hour, add the following line in crontab:

```
0 * * * * python3 ~/Manage-FTP-aigio/main.py
```

To check if your cron job is running:

```
grep CRON /var/log/syslog
```
