from typing import Any, Dict

import requests

from src.logs import logger

API_KEY = "your_api_key_here"


def get_transaction_amount_in_rub(transaction: Dict[str, Any]) -> float:
    currency = transaction.get('currency', 'RUB').upper()
    amount = float(transaction.get('amount', 0))
    logger.info(f"Getting transaction amount in RUB from {currency}: {amount}")
    if currency == 'RUB':
        return amount
    if currency in ['USD', 'EUR']:
        try:
            response = requests.get(
                "https://api.apilayer.com/exchangerates_data/convert",
                headers={"apikey": API_KEY},
                params={"from": currency, "to": "RUB", "amount": amount},
                timeout=10
            )
            data = response.json()
            return float(data['result']) if data.get('success') else amount
        except:
            return amount

    return amount

