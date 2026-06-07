import json
import os


def load_config(config_path='config/config.json'):
    """Load parameters from configuration file."""
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"✗ Ошибка: Файл конфигурации не найден по пути: {config_path}")

    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)

    return config