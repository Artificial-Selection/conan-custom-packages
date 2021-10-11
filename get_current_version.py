import os

package_to_version = {
      'glad': 'glad/0.1.34@snv/stable',
     'imgui': 'imgui/18410@snv/docking',
    'spdlog': 'spdlog/1.9.2@snv/stable'
}

package_name = os.environ['PACKAGE_NAME']
print(package_to_version[package_name])
