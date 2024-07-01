# Directory Tree Visualization Script

This Python script generates a tree structure visualization of a specified directory up to a specified depth. The tree structure is logged and saved to a file. The script utilizes `os`, `sys`, `argparse`, and `logging` modules.

## Features

- **Tree Generation:**
  - Generates a tree structure of a specified directory.
  - Can limit the depth of the tree visualization.
  - Logs the tree structure to a file.

- **Error Handling:**
  - Checks if the specified directory is valid.
  - Ensures the depth is a positive integer.
  - Handles exceptions and logs errors.

## Usage

1. **Setup:**
   - Ensure Python 3.x and necessary modules (`os`, `sys`, `argparse`, `logging`) are installed.

2. **Command Line Arguments:**
   - `--dir`: Directory to visualize (required).
   - `--depth`: Depth of tree visualization (default: 10).
   - `--output`: File to save the tree structure (default: `tree.txt`).

3. **Running the Script:**
   - Execute the script with appropriate command line arguments:
     ```bash
     python dir_tree.py --dir /path/to/directory --depth 5 --output tree.txt
     ```

4. **Output:**
   - Displays and logs actions taken (tree generation).
   - Saves the tree structure to the specified file.

## Example

Assume the following command generates a tree structure for a directory up to a depth of 5 and saves it to `tree.txt`:

```bash
python dir_tree.py --dir /opt/app --depth 5 --output tree.txt
```

## Output
```bash
├── bin
│   ├── script1.sh
│   └── script2.sh
├── config
│   ├── config1.yaml
│   └── config2.yaml
└── logs
    ├── log1.txt
    └── log2.txt
Tree structure saved to: tree.txt
```
