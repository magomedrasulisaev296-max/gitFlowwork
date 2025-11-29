import logging
from logging import Logger

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(f"../logs_output/UTILS.log")
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)



import json
import os
from typing import List, Dict, Any


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """
    Загружает список финансовых транзакций из JSON-файла.
    """
    try:
        # Покажем полный путь для отладки
        full_path = os.path.abspath(file_path)
        print(f"Ищем файл по пути: {full_path}")

        # Проверим существует ли файл
        if not os.path.exists(file_path):
            Logger.warning("file not found, check way to file or file type")
            print(f"❌ Файл НЕ СУЩЕСТВУЕТ: {file_path}")
            print(f"Текущая директория: {os.getcwd()}")
            print(f"Содержимое текущей директории: {os.listdir('.')}")
            if os.path.exists('data'):
                print(f"Содержимое папки data: {os.listdir('data')}")
            else:
                print("❌ Папка data не найдена")
            return []

        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        if isinstance(data, list):
            logger.info("file fonded")
            print(f"✅ Файл загружен успешно: {len(data)} транзакций")
            return data
        else:
            logger.info("check the file for the list contents")
            print("❌ Файл не содержит список")
            return []

    except FileNotFoundError:
        logger.info("check the integrity of the file and its format")
        print(f"❌ Файл {file_path} не найден")
        return []
    except json.JSONDecodeError:
        print(f"❌ Ошибка чтения JSON из файла {file_path}")
        return []
    except Exception as e:
        print(f"❌ Произошла ошибка: {e}")
        return []

# Пример 1: Загрузка всех транзакций
transactions = load_transactions(r"C:\Users\admin\Desktop\gitFlowwork\data\transactions.json")  # Твой файл
print(f"Загружено транзакций: {len(transactions)}")

# Пример 2: Только выполненные транзакции
executed = [tx for tx in transactions if tx.get('state') == 'EXECUTED']
print(f"Выполненных транзакций: {len(executed)}")

# Пример 3: Транзакции в USD
usd_tx = [tx for tx in transactions if tx.get('operationAmount', {}).get('currency', {}).get('code') == 'USD']
print(f"Транзакций в USD: {len(usd_tx)}")