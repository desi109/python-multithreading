import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s',)

def start_thread():
    logging.debug('Starting')
    logging.debug('Exiting')

def start_daemon():
    logging.debug('Starting')
    time.sleep(5)
    logging.debug('Exiting')

if __name__ == '__main__':

	thread = threading.Thread(name='non-daemon', target=start_thread)

	daemon = threading.Thread(name='daemon', target=start_daemon)
	daemon.setDaemon(True)

	daemon.start()
	thread.start()