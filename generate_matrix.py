import os
import subprocess


GITHUB_WORKFLOWS_PATH = "./.github/workflows/"
PACKAGES_PATH = "./packages/"

PREVIOUS_SHA = os.environ['PREVIOUS_SHA']
CURRENT_SHA  = os.environ['CURRENT_SHA']


def check_changes(package_path):
    with open(os.devnull, 'wb') as shutup:
        git_diff_output = subprocess.check_output(['git', 'diff', '--name-only', PREVIOUS_SHA, CURRENT_SHA, '--', package_path], stderr=shutup)
    if git_diff_output:
        return True
    return False


all_packages = []
packages_to_build = []

for package_name in os.listdir(PACKAGES_PATH):
    package_path = os.path.join(PACKAGES_PATH, package_name)

    if os.path.isdir(package_path):
        all_packages.append(package_name)
        if check_changes(package_path):
            packages_to_build.append(package_name)

# if github actions build script changed, rebuild all packages
if check_changes(GITHUB_WORKFLOWS_PATH):
    selected_list = all_packages
else:
    selected_list = packages_to_build

packages_json = '["' + '", "'.join(selected_list) + '"]'

print(packages_json)
