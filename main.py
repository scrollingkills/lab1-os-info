import platform
import os
import json

# Определяем операционную систему
system = platform.system()

# Собираем информацию
info = {
    "os": system,
    "os_version": platform.version(),
    "os_release": platform.release(),
    "architecture": platform.machine(),
    "processor": platform.processor(),
    "computer_name": platform.node(),
    "python_version": platform.python_version(),
    "cpu_count": os.cpu_count()
}

# Сохраняем результат в JSON
with open("system_info.json", "w", encoding="utf-8") as file:
    json.dump(info, file, indent=4, ensure_ascii=False)

print("Операционная система:", system)
print("Информация сохранена в system_info.json")
