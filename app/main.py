import logging

from app.core.cfg import cfg

__author__ = 'kclark'

logger = logging.getLogger(__name__)


def run_app():
    logger.info('App Script Running')

    # Replace with application process logic
    logger.info(f'App Env {cfg.app_env}, App Start Time {cfg.app_start_time}')

    logger.info('App Script Finished')


if __name__ == '__main__':
    run_app()
