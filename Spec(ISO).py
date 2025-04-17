NFISOConfigSpec
"l
"1": ("field_name": "Bitmap secondary", "field_type": "FIXED", "field_length": 16, )
Raw
Blame
"2": ("wf":True, "field_name": "PAN", "class"; "LLHNUN", "field_type": "LLHNUM", "field_length": 19, "pad":""", ),
"3": ("wf":True, "field_name": "PROCESSING CODE", "class": "NUMERIC", "field_type": "FIXED", "field_length": 6, "pad":""", ),
"4": ("wf":True, "field_name": "AMOUNT, TRANSACTION", "class": "NUMERIC", "field_type": "FIXED", "field_length": 12, "pad":"", >,
"5": ("wf":True, "field_name": "AMOUNT, SETTLEMENT", "class": "NUMERIC", "field_type": "FIXED", "field_length": 12, "pad":""", )
"6": (""wf":True, "field_name": "AMOUNT, CARDHOLDER BILLING", "class": "NUMERIC", "field_type": "FIXED", "field_length": 12, "pad":""", ),
"7": ("wf":True, "field_name": "TRANSACTION DATE AND TIME", "class": "NUMERIC", "field_type": "FIXED", "field_length": 10, "pad":""", >
'8": ("field_name": "AMOUNT, CARDHOLDER BILLING FEE", "class": "NUMERIC", "field_type": "FIXED", "field_length": 8, "pad":""", >,
"9": ("field_name": "CONVERSION RATE, SETTLEMENT", "class": "NUMERIC", "field_type": "FIXED", "field_length": 8, "pad":""", )
"10": ("wf":True, "field_name": "CONVERSION RATE, CARDHOLDER BILLING", "class": "NUMERIC", "field_type": "FIXED", "field_length": 8, "pad":"0", )
"11": ("wf":True, "field_name": "STAN", "class": "NUMERIC", "field_type": "FIXED", "field_length": 6, "pad":"0", t
"12": (""wf":True, "field_name": "LOCAL TRANSACTION TIME", "class": "NUMERIC", "field_type": "FIXED", ""ield_length": 6, "pad":", ),
"13": ("wf":True, "field_name": "LOCAL TRANSACTION DATE", "class": "NUMERIC", "field_type": "FIXED", "field_length": 4, "pad":""", )
"14": ("wf":True, "field_name": "EXPIRY DATE", "class": "NUMERIC", "field_type": "FIXED", "field_length": 4, "pad":"""> )
"15": ("field_name": "SETTLEMENT DATE", "Class": "NUMERIC", "field_type": "FIXED", "field_length": 4, "pad":"""> ),
"16": ("field_name": "CONVERSION DATE", "Class": "NUMERIC", "field_type": "FIXED", "field_length": 4, "pad":""", ),
"17": <("field_name": "CAPTURE DATE", "Class": "NUMERIC", "field_type": "FIXED", "field length": 4, "pad": """, >
18": ("wf":True, "field_name": "MERCHANT TYPE(MCC)", "class": "NUMERIC", "field_type": "FIXED", "field_length": 4, "pad":""", )
"19": ("wf":True, "field_name": "ACQUIRING INSTITUTION COUNTRY CODE", "class": "NUMERIC", "field_type": "FIXED", "field_length": 4, "pad":""", }
"20": ("field_name": "PAN EXTENDED COUNTRY CODE", "class": "NUMERIC", "field_type": "FIXED", "field_length": 4, "pad":""", ),# Changed length 3 to 4
"21": ("field_name": "FORWARDING INSTITUTION COUNTRY CODE", "class": "NUMERIC", "field_type": "FIXED", "field_length": 4, "pad":""", ),# Changed 1ength 3 to
'22": ("wf":True, "field_name": "POS ENTRY MODE", "class": "NUMERIC", "field_type": "FIXED", "field_length": 4, "pad":""", )
"23": ("field_name": "CARD SEQUENCE NUMBER", "class": "NUMERIC", "field_type": "FIXED", "field_length": 4, "pad":""", ),# Changed length 3 to 4
24": ("field_name": "NETWORK INTERNATIONAL IDENTIFIEER", "class": "NUMERIC", "field_type": "FIXED", "field_length": 3, "pad":""", ),
25": (""f":True, "field_name": "POINT OF SERVICE CONDITION CODE", "Class": "NUMERIC", "field_type": "FIXED", "field_length": 2, "pad":""", ),
'26": ("field_name": "POINT OF SERVICE PIN CAPTURE CODE", "class": "NUMERIC", "field_type": "FIXED", "field_length": 2, "pad":""", )
"27": ("field_name": "AUTHORIZATION IDENTIFICATION RESP LEN", "class": "NUMERIC", "field_type": "FIXED", "field_length": 1, "pad":""", ),
28": ("field_name": "TRANSACTION FEE AMOUNT", "class": "AMOUNT", "field_type": "FIXED", "field_length": 9, "pad":""", )
'29": ("field_name": "SETTLEMENT FEE AMOUNT", "class": "AMOUNT", "field_type": "FIXED", "field_length": 9, "pad":""", >
30": ("field_name": "TRANSACTION PROCESSING FEE AMOUNT", "class": "AMOUNT", "field_type": "FIXED", "field_length": 9, "pad":"""> ),
'31": ("field_name": "SETTLEMENT PROCESSING FEE AMOUNT", "class": "AMOUNT", "field_type": "FIXED", "field_length": 9, "pad":""", ),
'32": ("wf":True, "field_name": "ACQUIRER INST ID CODE", "class": "LLHNUM", "field_type": "LLHNUM", "field_length": 11, "pad": """> >
"33": ("wf":True, "field_name": "FORWARDING INST ID CODE", "class": "LLHNUM", "field_type": "LLHNUM", "field_length": 11, "pad":"0", >.
"34": ("wf":True, "field_name": "PAN EXTENDED", "Class": "LLHNUM", "field_type": "LLHNUM", "field_length": 28, "pad":""", ),
'35": ("field_name": "TRACK 2 DATA", "class": "LLHNUM", "field_type": "LLHNUM", "field_length": 37, "pad":""", >
'36": ("field_name": "TRACK 3 DATA", "class": "LLLNUM", "field_type": "LLLNUM", "field_length": 104, "pad":"0", ).
"37": ("wf":True, "field_name": "RETRIEVAL REFERENCE NUMBER", "class": "CHAR", "field_type": "CHAR", "field_length": 12, "pad":"0", "IsHex": "cp500"), #added "IsHex"
38": ("wf":True, "field_name": "AUTH RESPONSE", "class": "CHAR", "field_type": "CHAR", "field_length": 6, "pad":"0", "IsHex": "cp500">, #added "IsHex": "cp500"


"39": ("wf":True, "field_name": "RESPONSE CODE" "class": "CHAR",
"field_type":
"CHAR",
"41": (""f":True, "field_name": "CARD ACCEPTOR TERMINAL IDENTIFICATION",


"40": ("field_name": "SERVICE RESTRICTION CODE", "class": "CHAR",
"field_type"; "CHAR",
"field_length": 3, "pad":"0",
"IsHex": "cp500">, #added
"IsHex": "cp500"


"field_length":
"pad": "0",
"IsHex": "cp500">, #added.
"IsHex": "cp500"


"class": "CHAR",
"field_type"; "CHAR",
"field_length"; 8, "pad": """,
"IsHex": "cp500") #adde
42": ("wf":True, "field_name": "CARD ACCEPTOR ID CODE", "class": "CHAR", "field_type": "CHAR", "field_length": 15, "pad":"", "IsHex": "cp500"), #added "IsHex": "cp5
'45": ("field_name": "TRACK 1 DATA", "class": "LLHCHAR", "field_type": "LLHCHAR", "field_length": 76, "pad":"0", ",
"46": ("field_name": "ADDITIONAL DATA - ISO", "class": "LLHCHAR", "field_type": "LLHCHAR", "field_length": 99, "pad":"0", }
"47": ("field_name": "ADDITIONAL DATA - NATIONAL", "class": "LLHCHAR", "field_type": "LLHCHAR", "field_length": 99, "pad":""", ),
48": ("field_name": "ADDITIONAL DATA - PRIVATE", "class": "LLHBINARY", "field_type": "LLHBINARY", "field_length": 99, "pad":""", ),
'49": ("wf":True, "field_name": "TRANSACTION CURRENCY CODE", "class": "NUMERIC", "field_type": "FIXED", "field_length": 4, "pad":""", ),# Changed length 3 to 4
'50": ("field_name": "CURRENCY CODE, SETTLEMENT", "class": "NUMERIC", "field_type": "FIXED", "field_length": 3, "pad":""", ),
'51": (""f":True, "field_name": "CARDHOLDER BILLING CURRENCY CODE", "class": "NUMERIC", "field_type": "FIXED", "field_length": 3, "pad":""", )
'52": <"field_name": "PIN DATA", "class": "BINARY", "field_type": "BINARY", "field_length": 8, "pad":""", >
"53": ("field_name": "SECURITY RELATED CONTROL INFORMATION", "class": "NUMERIC", "field_type": "FIXED", "field_length": 16, "pad":""> ),
'54": ("field_name": "ADDITIONAL AMOUNTS", "class": "LLHECHAR", "field_type": "LLHECHAR", "field_length": 120, "pad":", "IsHex": "cp500")
'55": ("field_name": "RESERVED ISO", "class": "LLHBINARY", "field_type": "LLHBINARY", "field_length": 255, "pad":"0", )
'56": ("field_name": "RESERVED ISO", "class": "LLHCHAR", "field_type": "LLHCHAR", "field_length": 255, "pad":""", >,
'57": ("field_name": "RESERVED NATIONAL", "class": "LLHCHAR", "field_type": "LLHCHAR", "field_length": 255, "pad":"0",
'58": ("field_name": "RESERVED NATIONAL", "class": "LLHCHAR", "field_type": "LLHCHAR", "field_length": 255, "pad":"0", )
'59": ("field_name": "NATIONAL POS GEOGRAPHIC DATA", "class": "LLHECHAR", "field_type": "LLHECHAR", "field_length": 14, "pad":"0", "IsHex": "cp500").
'60": ("field_name": "RESERVED PRIVATE", "class": "LLHBINARY", "field_type": "LLHBINARY", "field_length": 10, "pad":"0", ).
62": ("field_name": "PAYMENT SERVICE FIELDS", "class": "LLHBINARY", "field_type": "LLHBINARY", "field_length": 59, "pad":""", >
'63": ("field_name": "SMS PRIVATE-USE FIELDS", "class": "LLHBINARY", "field_type": "LLHBINARY", "field_length": 255, "pad":""", )
'64": ("field_name": "MESSAGE AUTHENTICATION CODE FIELD", "class": "BINARY", "field_type": "BINARY", "field_length": 8, "pad":"0", ),
"65": ("field_name": "BITMAP, EXTENDED", "class": "BINARY", "field_type": "BINARY", "field_length": 1, "pad":""0", `,
"66": ("field_name": "SETTLEMENT CODE", "class": "NUMERIC", "field_type": "FIXED", "field_length": 1, "pad":"0", ),
"67": ("field_name": "EXTENDED PAYMENT CODE", "class": "NUMERIC", "field_type": "FIXED", "field_length": 2, "pad":"0", ),
"68": ("field_name": "RECEIVING INSTITUTION COUNTRY CODE", "class": "NUMERIC", "field_type": "FIXED", "field_length": 3, "pad":"0", `
"69": ("field_name": "SETTLEMENT INSTITUTION COUNTRY CODE", "class": "NUMERIC", "field_type": "FIXED", "field_length": 3, "pad":""", `,


"70": ("field_name": "NETWORK MANAGEMENT INFORMATION CODE",
"class": "NUMERIC" "field_type": "FIXED",
"field_length":
E


pad":"0"
"71": ("field_name": "MESSAGE NUMBER", "class": "NUMERIC", "field_type": "FIXED", "field_length": 4, "pad":"0", )
"72": ("field_name": "MESSAGE NUMBER LAST", "class": "NUMERIC", "field_type": "FIXED", "field_length": 4, "pad":""", )
"73": ("field_name": "DATE ACTION", "class": "NUMERIC", "field_type": "FIXED", "field_length": 6, "pad":"0", ).
"74": ("field_name": "CREDITS NUMBER", "class": "NUMERIC", "field_type": "FIXED", "field_length": 10, "pad":"0", >.
"75": ("field_name": "CREDITS REVERSAL NUMBER", "class": "NUMERIC", "field_type": "FIXED", "field_length": 10, "pad":""", >
"75": ("field_name": "CREDITS REVERSAL NUMBER", "class": "NUMERIC", "field_type": "FIXED", "field_length": 10, "pad":"0", )
"76": ("field_name": "DEBITS NUMBER", "class": "NUMERIC", "field_type": "FIXED", "field_length": 10, "pad":""", >,
77": ("field_name": "DEBITS REVERSAL NUMBER", "class": "NUMERIC", "field_type": "FIXED", "field_length": 10, "pad":""", )
'78": ("field_name": "TRANSFER NUMBER", "class": "NUMERIC", "field_type": "FIXED", "field_length": 10, "pad":""", ).
"79": ("field_name": "TRANSFER REVERSAL NUMBER", "class": "NUMERIC", "field_type": "FIXED", "field_length": 10, "pad":""", ),
'80": ("field_name": "INQUIRIES NUMBER", "class": "NUMERIC", "field_type": "FIXED", "field_length": 10, "pad":""", >
81": ("field_name": "AUTHORIZATION NUMBER", "class": "NUMERIC", "field_type": "FIXED", "field_length": 10, "pad":"", >>
'82": ("field_name": "CREDITS, PROCESSING FEE AMOUNT", "class": "NUMERIC", "field_type": "FIXED", "field_length": 12, "pad":"""> )
'83": ("field_name": "CREDITS, TRANSACTION FEE AMOUNT", "class": "NUMERIC", "field_type": "FIXED", "field_length": 12, "pad":""", )
84": ("field_name": "DEBITS, PROCESSING FEE AMOUNT", "class": "NUMERIC", "field_type": "FIXED", "field_length": 12, "pad":""", )
85": ("field_name": "DEBITS, TRANSACTION FEE AMOUNT", "class": "NUMERIC", "field_type": "FIXED", "field_length": 12, "pad":"0", ),
"86": ("field_name": "CREDITS, AMOUNT", "class": "NUMERIC", "field_type": "FIXED", "field_length": 16, "pad":""", ),
87": ("field_name": "CREDITS, REVERSAL AMOUNT", "class": "NUMERIC", "field_type": "FIXED", "field_length": 16, "pad":""", >,
'88": ("field_name": "DEBITS, AMOUNT", "class": "NUMERIC", "field_type": "FIXED", "field_length": 16, "pad":"0", )
89": ("field_name": "DEBITS, REVERSAL AMOUNT", "class": "NUMERIC", "field_type": "FIXED", "field_length": 16, "pad":""", ).
'91": ("field_name": "FILE UPDATE CODE", "class": "CHAR", "field_type": "CHAR", "field_length": 1, "pad": """, ),
"92": ("field_name": "FILE SECURITY CODE", "class": "CHAR", "field_type": "CHAR", "field_length": 2, "pad":""", >.
'93": ("field_name": "RESPONSE INDICATOR", "class": "CHAR", "field_type": "CHAR", "field_length": 5, "pad":"0", ),
"94": ("field_name": "SERVICE INDICATOR", "class": "CHAR", "field_type": "CHAR", "field_length": 7, "pad":""", ),
'96": <("field_name": "MESSAGE SECURITY CODE", "class": "BINARY", "field_type": "BINARY", "field_length": 8, "pad":"0"> >
"97": ("field_name": "AMOUNT, NET SETTLEMENT",
"class": "AMOUNT",
"field_type": "FIXED",
"field_ length": 17, "pad":""", ES
"98": ("field_name": "PAYEE". "class": "CHAR".
..
"field_ _type": "CHAR",
"field_length": 25, "pad": "0",
'99": ("field_name": "SETTLEMENT INSTITUTION IDENT CODE", "class": "LLHNUM", "field_type": "LLHNUM", "field_length": 11, "pad":"0", >.
"100": ("field_name": "RECEIVING INSTITUTION IDENT CODE",
"class": "LLHNUM",
"field_type": "LLHNUM",
"field length": 11, "pad": """,
101": ("field_name": "FILE NAME", "class": "LLHECHAR", "field_type": "LLHECHAR", "field_length": 17, "pad":"0", "IsHex": "cp500"),
"102": ("field_name": "ACCOUNT IDENTIFICATION 1", "class": "LLHECHAR", "field_type": "LLHECHAR", "field_length": 28, "pad":"0", "IsHex": "cp500")
103": ("field_name": "ACCOUNT IDENTIFICATION 2", "class"; "LLHECHAR", "field_type": "LLHECHAR", "field_length": 28, "pad":"0", "IsHex": "cp500").
"104": ("field_name": "TRANSACTION DESCRIPTION", "class": "LLHECHAR", "field_type": "LLHECHAR", "field_length": 100, "pad":"0", "IsHex": "cp500"),
"105": ("field_name": "RESERVED ISO USE", "class": "LLHCHAR", "field_type": "LLHCHAR", "field_length": 99, "pad":"0", >.
"106": ("field_name": "RESERVED ISO USE", "class": "LLHCHAR", "field_type": "LLHCHAR", "field_length": 99, "pad":""", ).
"107": ("field_name": "RESERVED ISO USE", "class": "LLHCHAR", "field_type": "LLHCHAR", "field_length": 99, "pad":", ),
"108": ("field_name": "RESERVED ISO USE", "class": "LLHCHAR", "field_type": "LLHCHAR", "field_length": 99, "pad":""", ),
"109": ("field_name": "RESERVED ISO USE", "class": "LLHCHAR", "field_type": "LLHCHAR", "Field_length": 99, "pad":"", )
'110": ("field_name": "RESERVED ISO USE", "class": "LLHCHAR", "field_type": "LLHCHAR", "field_length": 99, "pad":""", ),
'111": ("field_name": "RESERVED ISO USE", "class": "LLHCHAR", "field_type": "LLHCHAR", "field_length": 99, "pad":""", )
"112": ("field_name": "RESERVED NATIONAL USE", "class": "LLHCHAR", "field_type": "LLHCHAR", "field_length": 99, "pad":"""> ),
"113": ("field_name": "RESERVED NATIONAL USE", "class": "LLHCHAR", "field_type": "LLHCHAR", "field_length": 99, "pad":", ),
"114": ("field_name": "RESERVED NATIONAL USE", "class": "LLHCHAR", "field_type": "LLHCHAR", "field_length": 99, "pad":"0", ).
"115": ("field_name": "ADDITIONAL TRACE DATA 1", "class": "LLHCHAR", "field_type": "LLHCHAR", "field_length": 24, "pad":", ),
"116": ("field_name": "RESERVED NATIONAL USE", "class": "LLHCHAR", "field_type":""LLHCHAR", "field_length": 99, "pad":"0", ).
"117": ("field_name": "RESERVED NATIONAL USE", "class": "LLHCHAR" "field_type": "LLHCHAR",
"field_length": 99, "pad": "0",
"118": ("field_name": "INTRA-COUNTRY DATA", "class": "LLHBINARY", "field_type": "LLHBINARY", "field_length": 99, "pad":""", >,
"119": ("field_name": "RESERVED NATIONAL USE", "class": "LLHCHAR", "field_type": "LLHCHAR", "field_length": 99, "pad":"", ),
"120": ["field_name": "RESERVED PRIVATE USE", "class": "LLHNUM", "field_type": "LLHNUM", "field_length": 4, "pad":""", ),
"121": ("field_name": "ISSUING INSTITUTION IDENT CODE", "class": "LLHCHAR", "field_type": "LLHCHAR", "field_length": 11, "pad":""", >,
"122": ("field_name": "REMAINING OPEN-TO-USE", "class": "LLHCHAR", "field_type": "LLHCHAR", "field_length": 13, "pad":"0", )
"123": ("field_name": "FIELD 123", "class": "LLHBINARY", "field_type": "LLHBINARY", "field_length": 255, "pad":", >
"124": ("field_name": "FREE-FORM TEXT-JAPAN", "class": "LLHECHAR", "field_type": "LLHECHAR", "field_length": 135, "pad":"0", "IsHex": "cp500")
"125": ("field_name": "SUPPORTING INFORMATION", "class": "LLHCHAR", "field_type": "LLHCHAR", "field_length": 99, "pad":""", )
"127": ("field_name": "File Records", "class": "LLHBINARY", "field_type": "LLHBINARY", "field_length": 255, "pad":"0"> `
"128": ("field_name": "MAC 2", "class": "BINARY", "field_type": "BINARY", "field_length": 8, "pad":""", ).
"43":


"field_name": "CARD ACCEPTOR LOCATION" "class": "SUBFIELD" "field_type": "BINARY". "field_length": 40, "pad": "TRUE", "IsHex": "cp500"
"field_processor": "DE43"
"field_processor_config": r"(?P<DE43_NAME>.+?) *\\(?P<DE43_ADDRESS>.+>) *\\(?P<DE43|SUBURB>.+?) *\\(?P<DE43_POSTCODE>.[10;)(?P<DE43_STATE>.(3])(?P<DE43_COUNTRY>\5(3))S",
"44": `
"field_name":
"fields": f
"1":
"2":
"3":
"4":
"5":
"6":
"7":
""8":
"9":
"10":


("field_name": "NOT PRESENT",
"class": "NOP".
"field_ type": "NOP",
"field_ length": 0,
max_ length":
pad":""",
("wf":True, "field_name": "NAME", "class": "CHAR", "field_type": "CHAR", "field_length": 25, "max_length": 3, "pad":"""
("wf":True, "field_name": "CITY", "class": "CHAR", "field_type": "CHAR", "field_length": 13, "max_length": 3, "pad":"0"
"wf":True, "field_name": "COUNTRY", "class": "CHAR", "field_type": "CHAR", "field_length": 2, "max_length": 3,


3
"pad": "0",


"ADDITIONAL RESPONSE DATA"


"class":


"FIXED_SUBFIELD"


"field_type":


"LLHBINARY",


"field_length": 65,


"pad": "TRUE",


"IsHex":"cp500"


(""wf":True, "field_name": "RESPONSE SOURCE/REASON CODE", "class": "CHAR", "field_type": "CHAR", "field_length": 1, "max_length": 11, "pad":"""
"wf":True, "field_name": "AVS RESULT CODE", "class": "CHAR", "field_type": "CHAR", "field_length": 1, "max_length": 11, "pad":"0", )
("wf";True, "field_name": "TVC RESULT CODE",
"class": "CHAR",
"field_type": "CHAR",
"field_length": 1, "max_length": 11, "pad": "0",
[""wf":True, "field_name": "CARD PRODUCT TYPE", "class": "CHAR", "field_type": "CHAR", "field_length": 1, "max_length": 11, "pad":""", ),
"wf":True, "field_name": "CVV RESULT CODE", "class": "CHAR", "field_type": "CHAR", "field_length": 1, "max_length": 11, "pad":"0", ),
("wf":True, "field_name": "PACM DIVERSION LEVEL", "class": "CHAR", "field_type": "CHAR", "field_length": 2, "max_length": 11, "pad":"0", ),
("wf":True, "field_name": "PACM DIVERSION REASON CODE".
"class": "CHAR".,
"field_type":
"CHAR",
"field_length":
"max_length": 11, "pad": "0",
("wf": True, "field_name": "CARD AUTHENTICATION RESULT CODE", "class": "CHAR", "field_type": "CHAR", "field_length": 1, "max_length": 11, "pad":"""
""wf": True, "field_name": "LA ADDITIONAL RESPONSE DATA", "class": "CHAR", "field_type": "CHAR", "field_length": 1, "max_length": 11, ""ad": """, ),
("wf";True, "field_name": "CV2 RESULT CODE", "Class": "CHAR", "field_type": "CHAR", "field_length": 1, "max_length": 11, "pad":""", )
"61": t
"field_name":
"fields": (
"1":


"OTHER AMOUNTS"


("wf":True,
("wf":True,
("wf":True,


"field_name":


"2":


"field name":


"3":


"field_name":


"90":
"field_name":
"fields": (
"0":


"ORIGINAL


DATA


ELEMENTS"


("field_name"
("field_name":
("field_name":
("field_name":
<"field_name"


"1":
"2":


"3":


"4":


"95":
"field_name":
"fields":
"6":


"REPLACEMENT


("field_name"
("field_name":
("field_name":
("field_name"
("field_name":


"1":


"2":
"3":
"4";


"class":


"NOT PRESENT", "class": "NOP", "field_type": "NOP", "field_length": 0, "max_length": 4, "pad":""", ),
"class": "NUMERIC", "field_type": "FIXED". "field_length" Ax "ms.
max. length"
4,


"pad":"9",
"ORIGINAL MTI"
"ORIGINAL STAN", "class": "NUMERIC", "field_type": "FIXED", "field_length": 6, "max_length": 4, "pad":""", )
"class": "NUMERIC", "field_type": "FIXED", "field length": 10,
"max_length": 4, "pad":""">
"ORIGINAL TRANS DATE/TIME"
"ORIGINAL ACQ ID/FWD INST ID", "class": "NUMERIC", "field_type": "FIXED", "field_length": 22, "max_length": 4, "pad":"0"


"FIXED SUBFIELD"


"OTHER
"OTHER
"OTHER


"class":


AMOUNT, TRANSACTION", "class": "NUMERIC", "field_type": "FIXED", "field_length": 12, "max_length": 3, "pad":""> ),
AMOUNT, CARDHOLDER BILLING", "class": "NUMERIC", "field_type": "FIXED", "field_length": 12, "max_length": 3, "pad":""",
AMOUNT, REPLACEMENT BILLING", "class": "NUMERIC", "field_type": "FIXED", "field_length": 12, "max_length": 3, "pad":""> )>


"SUBFIELD".


"field_type":


"field_type": "BINARY"


"LLHBINARY"


"field_length": 19, "pad":"TRUE"


"field_length": 21, "pad":"TRUE"
[


"fieid_length"
42, pad":"TRUE"
gg


"IsHex":"cp500"


AMOUNTS"


"class":


"SUBFIELD".


"field_type": "BINARY"


"NOT PRESENT", "class": "NOP", "field_type": "NOP", "field_length": 0, "max_length": 4, "pad":""", ),
"ACTUAL AMT -TRANSACTION", "class": "CHAR" "field_type": "CHAR". "fieldu
42. "max_length": 4,
"UNUSED", "class": "CHAR", "field_type": "CHAR", "field_length": 12, "max_length": 4, "pad":"" 1,
"UNUSED", "class": "CHAR", "field_type": "CHAR", "field_length"
oad":""",
9,
"UNUSED", "class": "CHAR", "field_type": "CHAR", "field_length": 9, "max_lengt
D
"&"


285


"pad": "0",
"61": t
"field_name":
"fields": (
"1":


"OTHER AMOUNTS"


("wf":True,
("wf":True,
("wf":True,


"field_name":


"2":


"field name":


"3":


"field_name":


"90":
"field_name":
"fields": (
"0":


"ORIGINAL


DATA


ELEMENTS"


("field_name"
("field_name":
("field_name":
("field_name":
<"field_name"


"1":
"2":


"3":


"4":


"95":
"field_name":
"fields":
"6":


"REPLACEMENT


("field_name"
("field_name":
("field_name":
("field_name"
("field_name":


"1":


"2":
"3":
"4";


"class":


"NOT PRESENT", "class": "NOP", "field_type": "NOP", "field_length": 0, "max_length": 4, "pad":""", ),
"class": "NUMERIC", "field_type": "FIXED". "field_length" Ax "ms.
max. length"
4,


"pad":"9",
"ORIGINAL MTI"
"ORIGINAL STAN", "class": "NUMERIC", "field_type": "FIXED", "field_length": 6, "max_length": 4, "pad":""", )
"class": "NUMERIC", "field_type": "FIXED", "field length": 10,
"max_length": 4, "pad":""">
"ORIGINAL TRANS DATE/TIME"
"ORIGINAL ACQ ID/FWD INST ID", "class": "NUMERIC", "field_type": "FIXED", "field_length": 22, "max_length": 4, "pad":"0"


"FIXED SUBFIELD"


"OTHER
"OTHER
"OTHER


"class":


AMOUNT, TRANSACTION", "class": "NUMERIC", "field_type": "FIXED", "field_length": 12, "max_length": 3, "pad":""> ),
AMOUNT, CARDHOLDER BILLING", "class": "NUMERIC", "field_type": "FIXED", "field_length": 12, "max_length": 3, "pad":""",
AMOUNT, REPLACEMENT BILLING", "class": "NUMERIC", "field_type": "FIXED", "field_length": 12, "max_length": 3, "pad":""> )>


"SUBFIELD".


"field_type":


"field_type": "BINARY"


"LLHBINARY"


"field_length": 19, "pad":"TRUE"


"field_length": 21, "pad":"TRUE"
[


"fieid_length"
42, pad":"TRUE"
gg


"IsHex":"cp500"


AMOUNTS"


"class":


"SUBFIELD".


"field_type": "BINARY"


"NOT PRESENT", "class": "NOP", "field_type": "NOP", "field_length": 0, "max_length": 4, "pad":""", ),
"ACTUAL AMT -TRANSACTION", "class": "CHAR" "field_type": "CHAR". "fieldu
42. "max_length": 4,
"UNUSED", "class": "CHAR", "field_type": "CHAR", "field_length": 12, "max_length": 4, "pad":"" 1,
"UNUSED", "class": "CHAR", "field_type": "CHAR", "field_length"
oad":""",
9,
"UNUSED", "class": "CHAR", "field_type": "CHAR", "field_length": 9, "max_lengt
D
"&"


285


"pad": "0",
"126":


("field_name": "UNUSED"
("field_name": "UNUSED"


"class": "CHAR"
"class": "CHAR"


"field_type": "CHAR"
"field_type": "CHAR"


M-PE
ChAR"


"field_length"
Fieid iength": 12, "max_length": 4
"max_length":
..
Dr
"field_length": 9, "max_length": 4,


"pad": "@",
"pad":"0", ),
pad":"0", ),


Pau


"field_name": "FIELD 126"
"fields":
""0":
"1":
"2":
"3":
"4":
"5":
"6":
"7":
"8":
"9":
"10":
"11":
"12":
"13":
"14":
"15":
"16":
"18":
"19":


"class": "SUBFIELD_PACK"


"field_type": "LLHBINARY"


"field_length": 255,


"pad": "TRUE",


("field_name": "Field 126 Bitmap", "class": "BITMAP", "field_type": "BITMAP", "field_length": 8, "max_length": 19, "pad":""",
("field_name": "Customer Name", "class": "CHAR", "field_type": "CHAR", "field_length": 25, "max_length": 19, "pad":""", )
("field_name": "Customer Address", "class": "CHAR", "field_type": "CHAR", "field_length": 57, "max_length": 19, "pad":"0", )
("field_name": "Biller Address", "class": "CHAR", "field_type": "CHAR", "field_length": 57, "max_length": 19, "pad":""", ).
("field_name": "Biller Telephone Number", "class": "CHAR", "field_ type": "CHAR", "field_length": 16, "max_length": 19, "pad":""", )
"field_name": "VISA Merchant Identifier", "class": "BINARY",| "field_type": "BINARY", "field_length": 8, "max_length": 19, "pad":"0", )
("field_name": "Cardholder Cert Serial Number", "class": "BINARY", "field_type": "BINARY", "field_length": 17, "max_length": 19, "pad":"", >,
("field_name": "Merchant Cert Serial Number", "class": "BINARY", "field_type": "BINARY", "field_length": 17, "max_length": 19, "pad":""", ),
("field_name": "Transaction ID", "class": "BINARY", "field_ type": "BINARY", "field_length": 20, "max_length": 19, "pad":"> )
"field_name": "TransStain", "class": "BINARY", "field_type": "BINARY", "field_length": 20, "max_length": 19, "pad":"0", >,
("field_name": "CVV2 Request Data", "class": "CHAR", "field_type": "CHAR", "field_length": 6, "max_length": 19, "pad":""", "IsHex":"cp500")
"field_name": "IGOTS Transaction Description", "class": "CHAR", "field_type": "CHAR", "field_length": 2, "max_length": 19, "pad":""", ).
["field_name": "Service Deployment Indicator", "class": "BINARY", "field_type": "BINARY", "field_length": 3, "max_ length": 19, "pad":", >,
"field_name": "Recurring Payment Indicator", "class": "CHAR", "field_type": "CHAR", "field_length": 1, "max_length": 19, "pad":""", >.
"field_name": "Payment Guarantee Option Indicator", "class": "CHAR", "field_type": "CHAR", "field_length": 1, "max_length": 19, "pad":""", )
["field_name": "MC UCAF Option Indicator", "class": "CHAR", "field_type": "CHAR", "field_length": 1, "max_length": 19, "pad":""", )
("field_name": "MC UCAF Field", "class": "CHAR", "field_type": "CHAR", "field_length": 33, "max_length": 19, "pad":""", ).
("field_name": "Subfield", "class": "BINARY", "field_type": "BINARY", "field_length": 12, "max_length": 19, "pad":""", ).
("field_name": "Subfield", "class": "CHAR", "field_type": "CHAR", "field_length": 1, "max_length": 19, "pad":"0", >,
