import os
import sys
import argparse
import logging

def setup_logging(log_file):
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename=log_file)

def generate_tree(directory, depth, level=0, prefix=""):
    if level > depth:
        return
    try:
        items = os.listdir(directory)
        pointers = ['├── '] * (len(items) - 1) + ['└── ']

        for pointer, item in zip(pointers, items):
            path = os.path.join(directory, item)
            print(prefix + pointer + item)
            logging.info(prefix + pointer + item)

            if os.path.isdir(path):
                extension = '│   ' if pointer == '├── ' else '    '
                generate_tree(path, depth, level + 1, prefix + extension)
    except Exception as e:
        print(f"Error found: {e}")
        logging.error(f"Error found: {e}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, required=True, help="Directory to visualize")
    parser.add_argument('--depth', type=int, default=10, help="Depth of tree visualization")
    parser.add_argument('--output', type=str, default="tree.txt", help="File to save the tree structure")

    args = parser.parse_args()

    log_file = "dir_tree.log"
    setup_logging(log_file)

    if not os.path.isdir(args.dir):
        print(f"Error: {args.dir} is not a valid directory.")
        logging.error(f"Error: {args.dir} is not a valid directory.")
        sys.exit(1)

    if args.depth <= 0:
        print("Error: depth must be a positive integer.")
        logging.error("Error: depth must be a positive integer.")
        sys.exit(1)

    original_stdout = sys.stdout

    try:
        with open(args.output, 'w', encoding='utf-8') as f:
            sys.stdout = f
            generate_tree(args.dir, args.depth)
    except Exception as e:
        error_message = f"Error writing to file {args.output}: {e}"
        print(error_message)
        logging.error(error_message)
    finally:
        sys.stdout = original_stdout

    print(f"Tree structure saved to: {args.output}")
    logging.info(f"Tree structure saved to: {args.output}")

if __name__ == "__main__":
    main()
