from argparse import ArgumentParser


def arguments():
    arg = ArgumentParser()
    arg.add_argument('-u', '--url', type=str,
                     required=True, help='Enter the url')

    return arg.parse_args()
