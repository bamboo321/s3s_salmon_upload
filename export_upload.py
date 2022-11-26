import os
import subprocess
import hashlib


def get_file_body(file_path):
    with open(file_path, 'rb') as f:
        return f.read()


def is_identical_file(file1_path, file2_path):
    # First file of exp_dirs
    if file1_path == '':
        return False

    file1_body = get_file_body(file1_path)
    file1_hexdig = hashlib.sha256(file1_body).hexdigest()

    file2_body = get_file_body(file2_path)
    file2_hexdig = hashlib.sha256(file2_body).hexdigest()
    
    if file1_hexdig == file2_hexdig:
        return True
    else:
        return False


exp_dir = './exports/'
exp_dirs = os.listdir(exp_dir)
exp_dirs_sort = exp_dirs.sort(reverse=True)

previous_results_json_dir = ''
for d in exp_dirs:
    results_json_dir = exp_dir + d + '/' + 'coop_results.json'
    overview_json_dir = exp_dir + d + '/' + 'overview.json'

    if is_identical_file(previous_results_json_dir, results_json_dir):
        pass
    else:
        subprocess.run(['python3', 's3s.py', '-i', results_json_dir, overview_json_dir])

    previous_results_json_dir = results_json_dir