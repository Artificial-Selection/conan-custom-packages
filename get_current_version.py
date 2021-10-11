import os

package_to_version = {
      'entt': 'entt/3.8.1@snv/stable',
      'glad': 'glad/0.1.34@snv/stable',
     'imgui': 'imgui/18410@snv/docking',
    'spdlog': 'spdlog/1.9.2@snv/stable',
       'stb': 'stb/cci.20210713@snv/stable',
}

package_name = os.environ['PACKAGE_NAME']
print(package_to_version[package_name])
