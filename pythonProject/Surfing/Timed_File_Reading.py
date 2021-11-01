import logging
import time

# Create Logger
logging.basicConfig(filename="C:\\Users\\DELL\\Desktop\\logs.txt", level=logging.DEBUG)
logger = logging.getLogger()


def read_file_time(path):
    """Return The Contents Of The File At 'path' And Measure Time Taken"""
    start_time = time.time()
    try:
        f = open(path, mode='rb')
        data = f.read()
        return data
    except FileNotFoundError as err:
        logger.error(err)
        raise
    else:
        f.close()
    finally:
        stop_time = time.time()
        execution_time = stop_time - start_time
        logger.info("Time Taken To Execute {file} Is {time}".format(file=path, time=execution_time))


data_result = read_file_time("C:\\Users\\DELL\\Desktop\\Like Incense.mp3")
