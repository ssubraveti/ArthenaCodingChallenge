import argparse

from ArtParser import ArtParser

if __name__ == '__main__':
    # Take paths to data directories as command line arguments
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--paths', nargs='+', default=[])
    args = arg_parser.parse_args()
    paths = args.paths
    parser = ArtParser(paths)

    # Get painters mentioned in the webpages
    art_info = parser.get_artwork_info()

    print art_info
