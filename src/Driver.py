import argparse

from ArtParser import ArtParser

if __name__ == '__main__':
    # Take path to data directory as command line argument
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--path', type=str)
    args = arg_parser.parse_args()
    path = args.path
    parser = ArtParser(path)

    # Get painters mentioned in the webpages
    tag_list = parser.get_painter_names()

    print tag_list
