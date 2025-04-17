def panMask(card_number: str, mask_char: str = 's") -> str:

"""
returns a masked version of a card number
Format is First 6, last 4 digits


:param card_number: the card number to mask
:param mask_char: the character to use in masking


:return: masked card number
"""

return card_number[0:6] + mask_char * (len(card_number)-10) + card_number[-4:]
