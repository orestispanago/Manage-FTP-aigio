import logging
import os
import shutil

logger = logging.getLogger(__name__)

def mkdir_if_not_exists(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        logger.info(f"Created local directory: {dir_path}")
        
def save_to_daily_files(df, folder="daily", prefix=""):
    mkdir_if_not_exists(folder)
    days = [group[1] for group in df.groupby(df.index.date)]
    for day in days:
        fpath = f'{folder}/{prefix}{day.index[0].strftime("%Y%m%d")}.csv'
        day.to_csv(fpath, mode="a", header=not os.path.exists(fpath))
        logger.debug(f"Wrote {len(day)} rows in {fpath}")
    logger.info(f"Saved {len(days)} daily files")

def archive_past_days(local_files):
    if len(local_files) > 1:
        for local_file in local_files[:-1]:
            base_name = os.path.basename(local_file)
            year = base_name.split("_")[1][:4]
            dest_folder = f"daily/archive/{year}"
            dest_path = f"{dest_folder}/{base_name}"
            mkdir_if_not_exists(dest_folder)
            os.rename(local_file, dest_path)
            logger.info(f"Renamed local file {local_file} to {dest_path}")


def delete_local_folder(dirname):
    shutil.rmtree(dirname)
    logger.info(f"Deleted local folder: {dirname}")
