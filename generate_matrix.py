import os
import subprocess


PACKAGES_PATH = "./packages/"


def check_changes(package_path):
    git_diff_output = subprocess.check_output(['git', 'diff', "--name-only", package_path])
    if git_diff_output:
        return True
    return False

packages_to_build = []

for package_name in os.listdir(PACKAGES_PATH):
    package_path = os.path.join(PACKAGES_PATH, package_name)

    if os.path.isdir(package_path) and check_changes(package_path):
        packages_to_build.append(package_name)

matrix_json = '{"package": ["' + '", "'.join(packages_to_build) + '"]}'

print(matrix_json)
