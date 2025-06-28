# Filename:  file_line_counter.py
def count_lines(filepath):
    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        return 0