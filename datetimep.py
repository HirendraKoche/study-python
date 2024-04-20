# Study datetime module

from datetime import *
import logging
import setupLog

setupLog.setupLog()

logger = logging.getLogger("datetimep")

# Get the current day, month, year, hour, minute and timestamp from datetime module
def get_all_current_dt():
    logger.debug("Inside get_all_current_dt()")
    try:
        c_dt = datetime.now()
        logger.info(f"datetime.now() return {c_dt}")
        print("Day = ", c_dt.day)
        logger.info(f"c_dt.day return {c_dt.day}")
        print("Month = ", c_dt.month)
        logger.info(f"c_dt.month return {c_dt.month}")
        print("Year = ", c_dt.year)
        logger.info(f"c_dt.year return {c_dt.year}")
        print("Hour = ", c_dt.hour)
        logger.info(f"c_dt.hour return {c_dt.hour}")
        print("Min = ", c_dt.minute)
        logger.info(f"c_dt.min return {c_dt.minute}")
        c_dt_tp = c_dt.timestamp()
        print(f"Timestamp = {c_dt_tp: .2f}")
        logger.info(f"c_dt.timestamp() return {c_dt_tp: .2f}")
    except Exception as e:
        logger.exception(e, exc_info=True)
    finally:
        logger.debug("Exit get_all_current_dt()")

def diff_date(dt: datetime):
    logger.debug("Inside diff_date()")
    diff = timedelta()
    try:
        c_dt = datetime.now()
        diff = c_dt - dt
        return diff
    except Exception as e:
        logger.exception(e, exc_info=True)
    finally:
        logger.info(f"diff_date() return {diff}")
        logger.debug("Exit diff_date()")

if __name__ == '__main__':
    logger.debug("Inside main()")
    try:
        get_all_current_dt()
        dt = datetime(year=1970, month=1, day=1)
        print(diff_date(dt))
    except Exception as e:
        logger.exception(e, exc_info=True)
    finally:
        logger.debug("Exit main()")