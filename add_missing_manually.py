import glob
import pandas as pd
from utils import save_to_daily_files
from ftp import upload_files

def read_datalogger_file(fname, from_date=None):
    """ Reads .dat file downloaded directly from the datalogger.
        Use from_date argument to select from a desired date and on.
    """
    df = pd.read_csv(fname, 
                     skiprows=4, 
                     names=[
                            "Datetime_UTC",
                            "RECORD",
                            "Tair",
                            "RH",
                            "WS",
                            "WDir",
                            "Rain",
                            "PAR",
                            "LowWaveUp",
                            "LowWaveDn",
                            "HighWaveUp",
                            "HighWaveDn",
                            "LowReflect",
                            "HighReflect",
                            "NDVI",
                            "Tsoil_A_10cm",
                            "Tsoil_A_25cm",
                            "Tsoil_B_45cm",
                            "Tsoil_B_60cm",
                            "RHsoil_A_10cm",
                            "RHsoil_A_25cm",
                            "RHsoil_B_45cm",
                            "RHsoil_B_60cm",
                            "CSI_temp",
                            "CSI_batt",
                            ], 
                     parse_dates=True, 
                     index_col="Datetime_UTC")
    df = df.drop(labels=["RECORD"], axis=1) # Datalogger files have an extra "RECORD" column
    if from_date:
        df = df.loc[from_date:]
    return df

# Example usage:
# fname = "raw/UPatras_GoL_Gol_Eg_Pyrg_10min_2025_07_17_14_34_52.dat"
# df = read_datalogger_file(fname, from_date="2025-05-19 22:10:00")
# save_to_daily_files(df, folder="daily", prefix="aigio10min_")

""" Be carefull! upload overrides existing files at the FTP """
# daily_files = sorted(glob.glob("daily/*.csv"))
# upload_files(daily_files)