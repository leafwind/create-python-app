import argparse
import logging

from app.logger import set_logger


def parse_args():
    parser = argparse.ArgumentParser(description="init")
    parser.add_argument("-i", "--ini", type=str, required=False, help="ini filename")
    parser.add_argument("--dry-run", dest="dry_run", action="store_true")
    parser.add_argument("--no-dry-run", dest="dry_run", action="store_false")
    parser.set_defaults(dry_run=True)
    parser.add_argument("--debug", dest="debug", action="store_true")
    parser.set_defaults(debug=False)
    parser.add_argument("--log-level", type=int, required=False, default=10)
    return parser.parse_args()


def main(args):
    set_logger(args.log_level)
    logging.getLogger(__name__).info(f"dry run: {args.dry_run}")


if __name__ == "__main__":
    main(parse_args())
