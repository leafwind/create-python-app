import argparse
import logging
import os
import sys
from datetime import datetime


def parse_args():
    parser = argparse.ArgumentParser(description='init')
    parser.add_argument('-i', '--ini', type=str, required=False, help='ini filename')
    parser.add_argument('--dry-run', dest='dry_run', action='store_true')
    parser.add_argument('--no-dry-run', dest='dry_run', action='store_false')
    parser.set_defaults(dry_run=True)
    parser.add_argument('--debug', dest='debug', action='store_true')
    parser.set_defaults(debug=False)
    parser.add_argument('--log-level', type=int, required=False, default=10)
    return parser.parse_args()


def set_logger(log_level):
    my_format = "[%(levelname).4s] %(asctime)s | %(name)s | " \
                "%(filename)+20s | %(lineno)3s | %(message)s"
    date_fmt = '%Y-%m-%d %H:%M:%S'

    if not os.path.isdir('logs'):
        os.makedirs('logs', exist_ok=True)
    date_str = datetime.strftime(datetime.utcnow(), '%Y%m%d')
    logging.basicConfig(level=log_level,
                        format=my_format,
                        datefmt=date_fmt,
                        filename=os.path.join('logs', f'log.{date_str}'))

    formatter = logging.Formatter(my_format, date_fmt)
    h = logging.StreamHandler(sys.stdout)
    h.setFormatter(formatter)
    h.setLevel(log_level)
    logging.getLogger().addHandler(h)
    return


def main(args):
    set_logger(args.log_level)
    logging.info(f'dry run: {args.dry_run}')


if __name__ == '__main__':
    main(parse_args())

