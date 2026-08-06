import shutil
du=shutil.disk_usage("/")
print(du)
print(du.free/du.total*100)

import psutil
print(psutil.cpu_percent(0.1))