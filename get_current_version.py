import os

package_to_version = {
     'glad': 'glad/0.1.34@snv/stable',
    'imgui': 'imgui/18410@snv/docking'
}

package_name = os.environ['PACKAGE_NAME']
print(package_to_version[package_name])
