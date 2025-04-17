AuthSPEC = {
                         "1": ("name": "Bitmap secondary", "type": "CHAR_FIXED", "length": 16, >,
"2": ("name": "PAN", "type": "LL_CHAR", "length": 19),
"3": ("name": "PROCESSING CODE", "type": "CHAR_FIXED", "length": 6),
"4": ("name": "AMOUNT, TRANSACTION", "type": "CHAR_FIXED", "length": 12),
"5": ("name": "AMOUNT, SETTLEMENT", "type": "CHAR_FIXED", "length": 12),
"6": ("name": "AMOUNT, CARDHOLDER BILLING", "type": "CHAR_FIXED", "length": 12),
"7": ("name":"TRANSACTION DATE AND TIME", "type": "CHAR_FIXED","length":10),
"8": ("name": "AMOUNT, CARDHOLDER BILLING FEE", "type": "CHAR_FIXED", "length": 8),
"9": ("name": "CONVERSION RATE, SETTLEMENT", "type": "CHAR_FIXED", "length": 8),
"10": ("name": "CONVERSION RATE, CARDHOLDER BILLING", "type": "CHAR_FIXED", "Iength": 8),
"11": ("name": "STAN", "type": "CHAR_FIXED", "length": 6),
"12": ("name": "LOCAL TRANSACTION TIME", "type": "CHAR_FIXED", "length": 6),
"13": ("name": "LOCAL TRANSACTION DATE", "type": "CHAR_FIXED", "1ength": 4>,
"14": ("name": "EXPIRY DATE", "type": "CHAR_FIXED", "length": 4)
"15": ("name":"SETTLEMENT DATE", "type":"CHAR_FIXED", "length":4),
"16": ("name":"CONVERSION DATE", "type": "CHAR_FIXED","length":4 ),
"17": ("name": "CAPTURE DATE", "type":"CHAR_FIXED", "length":4),
"18": ("name": "MERCHANT TYPE(MCC)", "type":"CHAR_FIXED","length":4),
"19": ("name":"ACQUIRING INSTITUTION COUNTRY CODE", "type":"CHAR_FIXED","length":3),
"20": ("name":"PAN EXTENDED COUNTRY CODE", "typl: "CHAR_FIXED", "length":3),
"21": ("name": "FORWARDING INSTITUTION COUNTRY CODE", "type": "CHAR_FIXED", "length":3 ),
"22": (["name": "POS ENTRY MODE", "type": "CHAR_FIXED", "length": 4),
"23": <"name": "CARD SEQUENCE NUMBER", "type": "CHAR_FIXED", "length": 3),
"24": ("name": "NETWORK INTERNATIONAL IDENTIFIEER", "type": "CHAR_FIXED", "length": 3>,
"25": ("name": "POINT OF SERVICE CONDITION CODE", "type": "CHAR_FIXED", "length": 2),
"26": ("name": "POINT OF SERVICE PIN CAPTURE CODE",
"type": "CHAR_FIXED", "length": 2),
"27": ("name":"AUTHORIZATION IDENTIFICATION RESP LEN", "type":"CHAR_FIXED","length":1),
"28": ("name":"TRANSACTION FEE AMOUNT","type": "CHAR_FIXED", "length":9),
"29": ("name":"SETTLEMENT FEE AMOUNT", "type": "CHAR_FIXED","length":9),
"30": ("name": "TRANSACTION PROCESSING FEE AMOUNT"
"type": "CHAR_FIXED", "length": 9),
"31": ("name": "SETTLEMENT PROCESSING FEE AMOUNT".
"type": "CHAR_FIXED", "length": 9>>
"32": <"name": "ACQUIRER INST ID CODE"
"type": "LL_CHAR", "length": 11`,
"33": ("name": "FORWARDING INST ID CODE",
"type": "LL_CHAR", "length": 11),
"34": ("name": "PAN EXTENDED", "type":"L_CHAR","length":28 ),
"35": ("name":"TRACK 2 DATA", "type":"LL_CHAR", "length":37 ),
"36": ("name":"TRACK 3 DATA", "type":"LL_CHAR", "length":104 ),
"37": ("name": "RETRIEVAL REFERENCE NUMBER", "type": "CHAR_FIXED", "length": 12),
"38": ("name": "AUTH RESPONSE", "type": "CHAR_FIXED", "length": 6),
"39": ("name": "RESPONSE CODE", "type": "CHAR_FIXED", "length": 2),
"40": ("name": "SERVICE RESTRICTION CODE", "type": "CHAR_FIXED", "length": 3),
"41": ("name": "CARD ACCEPTOR TERMINAL IDENTIFICATION", "type": "CHAR_FIXED", "length": 8),
"42": ("name": "CARD ACCEPTOR ID CODE", "type": "CHAR_FIXED", "length": 15),
"45": ("name": "TRACK 1 DATA", "type":"CHAR_FIXED","length":76, ),
"46": ("name": "ADDITIONAL DATA - ISO", "type":"CHAR_FIXED","length":99, )
"47": ("name": "ADDITIONAL DATA - NATIONAL", "type":"CHAR_FIXED","length":99, ),
"48": ("name": "ADDITIONAL DATA - PRIVATE", "type":"LL_BINARY", "length":99, >
"49": ("name": "TRANSACTION CURRENCY CODE", "type": "CHAR_FIXED", "length": 3, "pad":" ", ),
"50": ("name": "CURRENCY CODE RECONCILIATION", "type": "CHAR_FIXED", "length": 3),
"51": <("name": "CARDHOLDER BILLING CURRENCY CODE", "type": "CHAR_FIXED", "length": 3),
"52": ("name": "PIN DATA","type":"BIN_FIXED", "length":8).
"53": ("name": "SECURITY RELATED CONTROL INFORMATION", "type":"CHAR_FIXED","length":16, >,
"54": ("name": "ADDITIONAL AMOUNTS", "type": "LL_EBC_CHAR", "length": 120),
"55": ("name":"RESERVED ISO", "type":"LL_BINARY","length":255),
"56": ("name":"RESERVED ISO", "type":"LL_EBC_CHAR","length":255),
"57": ("name":"RESERVED NATIONAL", "type":"LL_EBC_CHAR","length":255),
"58": ("name":"RESERVED NATIONAL", "type":"LL_EBC_CHAR","length":255),
"59": ("name": "NATIONAL POS GEOGRAPHIC DATA", "type":"LL_EBC_CHAR","length":14>,
"60": ("name":"RESERVED PRIVATE", "type":"LL_BINARY","length":10),
"62": ("name":"PAYMENT SERVICE FIELDS", "type":"LL_BINARY","length":59 ),
"63": ("name": "SMS PRIVATE-USE FIELDS". "type": "LL_BINARY", "length": 255),
"64": ("name":"MESSAGE AUTHENTICATION CODE FIELD", "type":"BIN_FIXED", "length":8),
"65": ("name":"BITMAP, EXTENDED", "type":"BIN_FIXED", "length":1),
"66": ("name":"SETTLEMENT CODE", "type": "CHAR_FIXED", "length":1),
"67": ("name":"EXTENDED PAYMENT CODE", "type": "CHAR_FIXED","length":2),
"68": ("name":"RECEIVING INSTITUTION COUNTRY CODE", "type":"CHAR_FIXED","length":3),
"69": ("name":"SETTLEMENT INSTITUTION COUNTRY CODE", "type":"CHAR FIXED", "length":3 ),
"70": ("name": "NETWORK MANAGEMENT INFORMATION CODE", "type":"CHAR_FIXED", "length":3),
"71": ("name": "MESSAGE NUMBER",
"type": "CHAR_FIXED", "length": 4),
"72": ("name":"MESSAGE NUMBER LAST","type"; "CHAR_FIXED","length":4, ),
"73": ("name":"DATE ACTION","type": "CHAR_FIXED","length":6, ),
"74": ("name":"CREDITS NUMBER","type": "CHAR_FIXED", "length":10, ),
"75": ("name":"CREDITS REVERSAL NUMBER", "type":"CHAR_FIXED","length":10, )
"76": ("name":"DEBITS NUMBER","type":"CHAR_FIXED"."length";10, )
"77": <("name":"DEBITS REVERSAL NUMBER", "type": "CHAR_FIXED","length":10, >,
"78": ("name":"TRANSFER NUMBER", "type": "CHAR_FIXED","length":10, ),
"79": ("name": "TRANSFER REVERSAL NUMBER","type":"CHAR_FIXED", "length":10, ,
"80": ("name":"INQUIRIES NUMBER", "type": "CHAR_FIXED", "length":10, >,
"81": ["name":"AUTHORIZATION NUMBER", "type": "CHAR_FIXED", "length":10, >
"82": ("name":"CREDITS, PROCESSING FEE AMOUNT", "type":"CHAR_FIXED", "length":12, ),
"83": ("name":"CREDITS, TRANSACTION FEE AMOUNT","type": "CHAR_FIXED", "length":12, >,
"84": ("name":"DEBITS, PROCESSING FEE AMOUNT","type":"CHAR_FIXED", "length":12, >
"85": ("name":"DEBITS, TRANSACTION FEE AMOUNT","type": "CHAR_FIXED","length":12, )
"86": ("name":"CREDITS, AMOUNT","type":"CHAR_FIXED","length":16, >,
"S7": ("name": "CREDITS, REVERSAL AMOUNT", "type": "CHAR_FIXED","length":16, )
"88": "name";"DEBITS, AMOUNT", "type";"CHAR_FIXED", "length":16,
"89": ("name":"DEBITS, REVERSAL AMOUNT","type":"CHAR_FIXED", "length":16, ),
"91": ("name":"FILE UPDATE CODE", "type":"CHAR_FIXED","length":1, ),
"92": ("name":"FILE SECURITY CODE", "type":"CHAR_FIXED","length":2, ),
"93": ("name":"RESPONSE INDICATOR", "type": "CHAR_FIXED", "length":5, )
"94": ("name":"SERVICE INDICATOR", "type": "CHAR_FIXED", "length":7, >,
"96": ("name": "MESSAGE SECURITY CODE", "type": "BIN_FIXED", "length":8, ),
"97": ("name": "AMOUNT, NET SETTLEMENT", "type":"CHAR_FIXED","length":17, >,
"98": ("name":"PAYEE", "type":"CHAR_FIXED","length":25, ,
"99": ("name":"SETTLEMENT INSTITUTION IDENT CODE", "type": "LL_CHAR","length":11,
"100": ("name":"RECEIVING INSTITUTION IDENT CODE", "type":"LL_CHAR","length":11, >
"101": ("name":"FILE NAME", "type":"LL_EBC_CHAR","length":17,),
"102": ("name": "ACCOUNT IDENTIFICATION 1", "type": "LL_EBC_CHAR","length":28,`,
"103": ("name": "ACCOUNT IDENTIFICATION 2", "type":"LL_EBC_CHAR", "length":28,),
"104": ("name";"TRANSACTION DESCRIPTION". "type": "LL_E EBC_ _CHAR", "length" :100,),
"105": ("name": "RESERVED ISO USE", "type":"LL_CHAR", "length":99, ),
"106": ("name": "RESERVED ISO USE", "type":"LL_CHAR","length":99, )
"107": ("name": "RESERVED ISO USE", "type":"LL_CHAR", "length":99,
"108": ("name": "RESERVED ISO USE", "type":"LL_CHAR", "length":99, )
"109": ("name": "RESERVED ISO USE", "type": "LL_CHAR", "length":99, )
"110": <"name":"RESERVED ISO USE", "type":"LL_CHAR", "length":99, ),
"111": ("name" ":"RESERVED IS0 USE", "type":"LL_ CHAR", "length":99,
"112": ("name": "RESERVED NATIONAL USE", "type":"LL_CHAR","length":99, >
"113": ("name":"RESERVED NATIONAL USE", "type":"LL_CHAR","length":99, >,
"114": ("name": "RESERVED NATIONAL USE", "type":"LL_CHAR", "length":99, ),
"115": ("name":"ADDITIONAL TRACE DATA 1", "type":"LL_CHAR","length":24, ),
"116": ("name":"RESERVED NATIONAL USE", "type":"LL_CHAR","length":99, >,
"117": ("name": "RESERVED NATIONAL USE", "type":"LL_CHAR","length":99, >
"118": ("name":"INTRA-COUNTRY DATA", "type":"LL_BINARY","length":99, ),
"119": ("name":"RESERVED NATIONAL USE", "type":"LL_CHAR","length":99, ),
"120": ("name":"RESERVED PRIVATE USE", "type":"LL_CHAR","length":4, ),
"121": ("name":"ISSUING INSTITUTION IDENT CODE", "type":"LL_CHAR","length":11, >.
"122": ("name":"REMAINING OPEN-TO-USE", "type":"LL_CHAR","length":13, >,
"123": ("name":"FIELD 123", "type":"LL_BINARY","length":255, ),
"124": ("name":"FREE-FORM TEXT-JAPAN", "type":"LL_EBC_CHAR","length":135,),
"125": ("name": "SUPPORTING INFORMATION"
"type":"LL_CHAR" "length" :99,
"127": ("name" "File Records", "type": "LL_BINARY". "length" 255, S
".


"128": ("name" "MAC 2"3 "type": :"BIN_FIXED" "length":8,},
"43":
"name":"CARD ACCEPTOR LOCATION", "class": "FIXED_SUBFIELD" "type": "BIN_FIXED", "length":40, "pad":"TRUE",
"fields":
~


"1": ("name":"NAME", "typ@": "CHAR_FIXED", "length":;25, "max_length": 3, )
"length":13, "max_length": 3, >,


"2":
"3":
Phn


("name":"CITY", "type":"CHAR_FIXED"
("name": "COUNTRY", "type":"CHAR_FIXED","length":2, "max_length": 3,


J, "44": (
"name": "ADDITIONAL RESPONSE DATA", "class": "FIXED. _SUBFIELD".
"type": "LL_BINARY","length":65, "pad":"TRUE"
"fields": t


"1": ("name": "RESPONSE SOURCE/REASON CODE", "type":"CHAR_FIXED", "length":1, "max_length": 11, ).
"2": ("name":"AVS RESULT CODE", |"type": "CHAR_FIXED","length":1, "max_length": 11,
"3": ("name": "TVC RESULT CODE", "type": "CHAR_FIXED", "length":1, "maxi length": 11, )
"4": (["name":"CARD PRODUCT TYPE", "type":"CHAR_FIXED", "length":1, "max_length": 11, `,
"5": ("name":"CV RESULT CODE", "type": "CHAR_FIXED", "length":1, "max_length": 11,
"6": ("name": "PACM DIVERSION LEVEL", "type": "CHAR_FIXED","length":2, "max_length": 11, )
"7": ("name":"PACM DIVERSION REASON CODE", "type":"CHAR_FIXED","length":1, "max_length": 11, )
'8": ("name":"CARD AUTHENTICATION RESULT CODE", "type":"CHAR_FIXED","length":l, "max_length": 11,
""": ("name":"LA ADDITIONAL RESPONSE DATA", "type": "CHAR_FIXED","length":1, "max_length": 11, >
"10": ("name":"CVV2 RESULT CODE", "type":"CHAR_FIXED","length";1, "max_length": 11,)
}
"61": (
"name":"OTHER AMOUNTS"
"fields": f
"1":
"2":
"3":


"a"- CARD AYIMENTICATION
("name": "LA ADDITIONAL RESPONSE DATA", "type":"CHAR_FIXED","length":1, "max_length": 11, >,
RESULT CODE", "type": "CHAR_FIXED","length":1, "max_length": 11, >,
("name": "CW2 RESULT CODE", "type":"CHAR_FIXED","length":1, "max_length": 11, )


"class":


"FIXED_SUBFIELD"


"type"": "LL_BINARY","length":19


"pad": "TRUE",


("name": "OTHER AMOUNT, TRANSACTION","type":"CHAR_FIXED","length":12, "max_length": 3, ),
("name": "OTHER AMOUNT, CARDHOLDER BILLING","type":"CHAR_FIXED", "length":12, "max_length": 3, )
["name":"OTHER AMOUNT, REPLACEMENT BILLING","type": "CHAR_FIXED", "length":12, "max_length": 3,


"90":
"name": "ORIGINAL DATA ELEMENTS"
"fields":
"0": ("name":"NOT
"1": ("name":"ORIGINAL
"2": ["name":"ORIGINAL
"3":
("name"
"4":


"class"


"SUBFIELD"


"type":"BIN_FIXED","length": 21


"pad": "TRUE",


PRESENT", "Class": "NOP", "type": "NOP", "length";0, "max_length": 4,
MTI","type": "CHAR_FIXED","length":4, "max_length": 4, ).
STAN","type": "CHAR_FIXED","length":6, "max_length": 4, `.
:"ORIGINAL TRANS DATE/TIME","type":"CHAR_FIXED","length":10, "max_length": 4, ).
["name":"ORIGINAL ACQ ID/FWD INST ID","type":"CHAR_FIXED","length":22, "max_length": 4, )
S "95": (
name": "REPLACEMENT AMOUNTS"
"fields": (
"0": ("nam=": "NOT


"name":"FIELD 126"
"fields": [
"0":
"1":
"2":
"3":
"4":
"5":
"6":
"7":
"8":


("name": "NOT PRESENT", "class": "NOP", "type":"NOP","length":0, "max_length": 4, ),
("name":;"ORIGINAL MTI", "type":"CHAR_FIXED", "length":4, "max_length": 4, ),
("name":;"ORIGINAL STAN","type":"CHAR_FIXED","length":6, "max_length": 4, ).
("name": "ORIGINAL TRANS DATE/TIME","type":"CHAR_FIXED","length":10, "max_length": 4, ),
("name": "ORIGINAL ACQ ID/FWD INST ID","type": "CHAR FIXED","length":22, "max_length": 4,


"class": "SUBFIELD"


"type": "BIN_FIXED", "length":42


"pad":"TRUE"


PRESENT", "class": "NOP", "type": "NOP","length":0, "max_length": 4, ),
("nam=":"ACTUAL AMT -TRANSACTION", "type":"CHAR_FIXED", "length":12, "max_length": 4, )
["name": "UNUSED", "type":"CHAR_FIXED","length":12, "max_length": 4, ]
("name": "UNUSED", "type":"CHAR_FIXED","length":9, "max_length": 4, `,
("name": "UNUSED", "type":"CHAR_FIXED", "length":9, "max_length": 4,`,
}
}, "126": {
"name": "FIELD 126", "class": "SUBFIELD_PACK", "type":"LL_BINARY","length":255, "pad":"TRUE"
"fields": C


""": ("name":"Field 126 Bitmap", "class": "BITMAP", "type":"BITMAP","length":8
"1": ("name":"Customer Name", "type":"CHAR_FIXED","length":25, "max_length": 19, )
"2": ("name":"Customer Address", "type":"CHAR_FIXED","length":57, "max_length": 19,
"3": ("name":"Biller Address", "type":"CHAR_FIXED", "length":57, "max_length": 19, >,
"4": ("name": "Biller Telephone Number", "type": "CHAR_FIXED", "length":16


"max_length": 19,
)
"max_length": 19, )
"5": ("name":"VISA Merchant Identifier", "type":"BIN_FIXED","length":8, "max_length": 19, "
'6": ("name":"Cardholder Cert Serial Number", "type":"BIN_FIXED","length":17, "max_length": 19, )
"7": ("name":"Merchant Cert Serial Number", "type": "BIN_FIXED", "length":17, "max_length": 19, )
"8": ("name":"Transaction ID", "type":"BIN_FIXED", "length":20, "max_length": 19, ),
"9": ("name": "TransStain", "type":"BIN_FIXED","length":20, "max_length": 19, )
"10": ("name":"CW2 Request Data", "type": "CHAR_FIXED","length":6, "max_length": 19)
"11": ("name": "IGOTS Transaction Description", "type": "CHAR_FIXED", "length":2, "max_length": 19, ),
"12": ("name":"Service Deployment Indicator", "type": "BIN_FIXED", "Ìength":3, "max_length": 19, ),
"13": ("name": "Recurring Payment Indicator", "type": "CHAR_FIXED", "length":1, "max_length": 19, ),
'14": ("name": "Payment Guarantee Option Indicator", "type":"CHAR_FIXED", "length":1, "max_length": 19, )
"15":
("name":"MC UCAF Option Indicator", "type":"CHAR_FIXED", "length":1 "max_length": 19, ),
"16": ("name": "MC UCAF Field", "type": "CHAR_FIXED", "length":33, "max_length": 19, ),
"18" :
("name": "Subfield", "type":"BIN_FIXED","length":12, "max_length": 19, ),
"19":
("name":"Subfield", "type":"CHAR_FIXED", "length":1, "max_length": 19, >,
}
}
}
