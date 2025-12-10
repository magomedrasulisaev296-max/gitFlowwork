from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_name_and_number: str) -> str:
    """функция определяет тип данных (счет или карта) и маскирует их"""
    lower_card_name_and_number = card_name_and_number.lower()
    splited_card_name_and_number = card_name_and_number.split(" ")

    if "счет" in lower_card_name_and_number:
        masked_account_card = get_mask_account(splited_card_name_and_number[-1])
    else:
        masked_account_card = get_mask_card_number(splited_card_name_and_number[-1])

    return f"{' '.join(splited_card_name_and_number[:-1])} {masked_account_card}"





def get_date(date_string: str) -> str:
    """Преобразует дату из формата 'ГГГГ-ММ-ДДT...' в формат 'ДД.ММ.ГГГГ'"""
    try:
        date_part = date_string.split("T")[0]
        year, month, day = date_part.split("-")
        return f"{day}.{month}.{year}"
    except:
        return date_string


