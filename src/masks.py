import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(f"../logs_output/masks.log")
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)



def get_mask_card_number(card_number: str) -> str:
    """функция принимает номер карты и шифрует числа находяшийися по центру"""
    logger.info("return your masked card number")
    card_number_without_spaces = card_number.replace(" ", "")
    if len(card_number_without_spaces) == 16:
        logger.info("your masked card number is great starting masking process")
        masked_card_number = card_number_without_spaces.replace(card_number[6:12], "******")
        masked_card_number = masked_card_number[:4] + " " + masked_card_number[4:6] + "** **** " + masked_card_number[-4:]
        return masked_card_number
    else:
        logger.warning("check your card number")
        return "некоректнные входные данные"


print(get_mask_card_number("2200444435358800"))


def get_mask_account(account_number: str) -> str:
    """Функция принимает номер аккаунта и скрывает первые его две цифры"""
    logger.info("return your masked account number")
    account_number_without_spaces = account_number.replace(" ", "")
    if len(account_number_without_spaces) == 20:
        logger.info("your masked account number is great starting masking process")
        replaced_account_number = account_number_without_spaces.replace(account_number_without_spaces[0:-4], "")
        masked_account_number = "**" + replaced_account_number
        return masked_account_number
    else:
        logger.warning("check your account number")
        return "некоректнные входные данные"

print(get_mask_account("123456"))

