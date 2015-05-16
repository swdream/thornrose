import argparse

import thornrose


def parse_args():
    parser = argparser.ArgumentPaser(description=thornrose.__doc__)
    sparsers = parser.add_subparsers(dest='subparser_name')
    subcmds = [('create', 'Let\'s start to manage your money in this month'),
               ('update', 'Update your spending in this month'),
               ('show', 'Show everything about your spending in this month'),
               ('status', 'Show your spending status'),
               ('undo', 'Back a step')]

    for subcmd, helps in subcmds:
        sub_parser = sparsers.add_parser(subcmd,
                                         help=helps)

        sub_parser.set_defaults(func=getattr(thorrose, subcmd))
        sub_parser.add_argument('monthname')

    args = parser.parse_args()


if __name__ == "__main__":
    parse_args()


