def get_mask_card_number(card_number: str) -> str:
    '''функция принимает номер карты и шифрует числа находяшийися по центру'''
    masked_card_number = card_number.replace(card_number[7:15], "*** **** ")
    return masked_card_number


print(get_mask_card_number("2200 4444 3535 8800"))


def get_mask_account(account_number: str) -> str:
    '''Функция принимает номер аккаунта и скрывает первые его две цифры'''
    replaced_account_number = account_number.replace(account_number[0:-4], "")
    masked_account_number = "**" + replaced_account_number

    return masked_account_number


print(get_mask_account("123456"))
