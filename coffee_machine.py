import argparse

if __name__ == '__main__':
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument('file_path', type=str, help='Input File Path')
    args = parser.parse_args()

    print(args.file_path)
