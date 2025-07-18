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

## Add missing data manually

Sometimes the datalogger does not upload files to the FTP server.
In this case `add_missing_manually.py` script is provided.

**WARNING:** Be very carefull when uploading data to the FTP.
This action will override existing files.
Uploading smaller files than those at the FTP will result in data gaps.

To add the missing data:

1. Make sure that the main script execution is stopped from crontab

2. Download the data from the datalogger to the `raw` folder. 
It will be a single `.dat` file.
e.g. `raw/UPatras_GoL_Gol_Eg_Pyrg_10min_2025_07_17_14_34_52.dat`.
The raw datalogger file contains headers and one extra column `"RECORD"` 
compared to the raw files arriving at the FTP

3. Add your last daily file in "daily" folder e.g. `aigio10min_20250519.csv` 
with last record atv

4. In`add_missing_manually.py` edit `fname` variable to use the datalogger file name
and `from_date` to select the missing records.
E.g. 
`fname = "raw/UPatras_GoL_Gol_Eg_Pyrg_10min_2025_07_17_14_34_52.dat"`
`df = read_datalogger_file(fname, from_date="2025-05-19 22:10:00")`
Note that `from_date` must be after the last record in the daily file,
in our case 10 minutes after `2025-05-19 22:10:00`

5. Split the datalogger `.dat` file to daily `.csv` files using
`save_to_daily_files()` from `utils.py`

6. Upload the daily files to the FTP