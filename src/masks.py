def get_mask_card_number(card_number: str) -> str:
    """функция принимает номер карты и шифрует числа находяшийися по центру"""
    card_number_without_spaces = card_number.replace(" ", "")
    if len(card_number_without_spaces) == 16:
        masked_card_number = card_number_without_spaces.replace(card_number[6:12], "******")
        masked_card_number = masked_card_number[:4] + " " + masked_card_number[4:6] + "** **** " + masked_card_number[-4:]
        return masked_card_number
    else:
        return "некоректнные входные данные"


print(get_mask_card_number("2200444435358800"))


def get_mask_account(account_number: str) -> str:
    """Функция принимает номер аккаунта и скрывает первые его две цифры"""
    account_number_without_spaces = account_number.replace(" ", "")
    if len(account_number_without_spaces) == 20:
        replaced_account_number = account_number_without_spaces.replace(account_number_without_spaces[0:-4], "")
        masked_account_number = "**" + replaced_account_number
        return masked_account_number
    else:
        return "некоректнные входные данные"

print(get_mask_account("123456"))

