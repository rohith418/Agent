IPMSpec
{

"1": {"name": "Bitmap secondary", "type": "CHAR FIXED", "length": 16, ).

"2": "name": "PAN", "type": "LL CHAR", "length": 19),

"3": "name": "PROCESSING CODE", "type": "CHAR FIXED", "length": 6),

"4" ("name": "APCUNT, TRANSACTION", "type": "CHAR FIXED", "length": 12), "5": "name" "AMOUNT, SETTLEMENT", "type": "CHAR FIXED", "length": 12),

"6": "name": "ANDUNT, CARDHOLDER BILLING", "type": "CHAR FIXED", "length": 12),

"B"name": "APOUNT, CARDHOLDER BILLING FEE", "type": "CHAR FIXED", "length": 8), "9":{"name": "CONVERSION RATE, SETTLEMENT", "type": "CHAR FIXED", "length" 8),

"10" ("name": "CONVERSION RATE, CARDHOLDER BILLING", "type": "CHAR FIXED", "length"; 8),

"12": ["name": "LOCAL TRANSACTION TIME", "type": "CHAR FIXED", "length": 12),

"14": ("name": "EXPIRY DATE", "type": "CHAR FIXED", "length": 4), "22":{"name": "POS DATA CODE "type": "CHAR FIXED", "length": 12),

"23" ("name": "CARD SEQUENCE NUMBER", "type": "CHAR FIXED", "length": 3),

"24": "name": "FUNCTION CODE", "type": "CHAR FIXED", "length": 3),

"25" ("name": "MESSAGE REASON CODE", "type": "CHAR FIXED", "length": 4),

"26" ("name": "CARD ACCEPTOR BUSINESS CODE", "type": "CHAR FIXED", "length": 4),

" "31": ["name": "ACQUIRER REFERENCE DATA", "type": "LL CHAR", "length": 99),

30":{"name": "AMOUNTS ORIGINAL", "type": "EBC CHR FIXED", "length": 24),

"32":{"name": "ACQUIRER INST ID CODE", "type": "LL CHAR", "length": 11), "33": ("name": "FORWARDING INST ID CODE", "type": "LL CHAR", "length": 11),

"37": ["name": "RETRIEVAL REFERENCE NUMBER", "type": "EBC CHA FIXED", "length": 12),

" 38": ("name": "AUTH RESPONSE", "type": "EBC CHR FIXED", "length": 6), "40" {"name": "SERVICE CODE".

DE", "type": "EBC CHR FIXED", "length": 3). "41": ["name": "CARD ACCEPTOR TERMINAL IDENTIFICATION", "type": "EBC CHA FIXED", "length": B),

"42": "name": "CARD ACCEPTOR ID CODE", "type": "EBC CHR FIXED", D", "length": 15),

"43" "CARD ACCEPTOR NAME/LOCATION, "type": "LE CHAR", "length": 99), "name"

" 49" ("name": "TRANSACTION CURRENCY CODE", "type": "EBC CHR FIXED", "length": 3, "pad":"",), "

50":{"name": "CURRENCY CODE RECONCILIATION", "type": "EBC CHR FIXED", "length": 3),

"51": {"name": "CARDHOLDER BILLING CURRENCY CODE", "type": "EBC CHR FIXED", "length": 3, "pad":""

"54": ["name": "ADDITIONAL AMOUNTS", "type": "LLL EBC CHAR", "length": 20),

"55": "name": "ICC SYSTEM RELATED DATA", "type": "LLL EBC CHAR", "length": 255),

"63": ("name": "RESERVED PRIVATE", "type": "LLL EBC CHAR", "length": 999),

"71": ["name": "MESSAGE NUMBER", "type": "EBC CHR FIXED", "length": 8),

"72": ["name": "DATA RECORD", "type": "LLL EBC CHAR", "length": 999),

"73": ["name": "DATE ACTION", "type": "CHAR FIXED", "length":6},

"93":{"name": "TXN DEST INST ID CODE", "type": "LL CHAR", "length": 11),

"94" ["name": "TION ORIG INST ID CODE", "type": "LL CHAR", "length": 11), ),

"95": "name": "CARD ISSUER REF DATA", "type": "LL CHAR", "length":30

"100" ["name": "RECEIVING INST ID CODE", "type": "LL CHAR", "length": 11),

"111": ["name": "AMOUNT CURR CONV ASSESSMENT", "type" "LLL_EBC CHAR", "length": 12),

"127":{"name": "NETWORK DATA", "type": "LLL EBC CHAR", ", "length": 999),

"48":{"name": "HASTERCARD FIELD 48", "type": "LLL BINARY", "processor": "POS", "length": 999), "62" ["name": "ADDITIONAL DATA 2", "type": "LLL BINARY", "processor": "POS", "length": 999),

"123":{"name": "ADDITIONAL DATA 3", "type": "type": "LLL BINARY", "processor": "POS", "length": 999), "124":{"name": "ADDITIONAL DATA 4", "type": "LLL BINARY", "processor": "PDS", "length": 999),

125

"name": "ADDITIONAL DATA 5", "type": "LLL BINARY", "processor": "POS", "length": 999, "fields": {

"0" {"name": "Default", "type": "PDS LLL VCHAR", "length":999},
"1": {"name": "174", "type": "PDS_LLL_CHAR", "length": 15),

"2": {"name": "596", "3": {"name": "506", "type": "PDS_LLL_CHAR", "length": 21), "type": "PDS_LLL_CHAR", ,

"4": ("name": "512", "type": " "length": 15) PDS_LLL_CHAR", "length": 12),

"5": {"name": "523", " "type": "PDS_LLL_CHAR", "length": 5),

6": {"name": "524", 7": {"name": "530", "type": "PDS_LLL_CHAR", "length": 5), "type": "PDS_LLL CHAR", "length": 5),

" "8": {"name": "549", "type": "PDS_LLL CHAR", "length ": 10),

" 10": {"name": "646", "11 "type": "PDS LLL CHAR", "length": 13, "PDSInterpretor": "EXPONENTIAL"}, "type": "PDS_LLL_CHAR", "length": 13, "PDS Interpretor": "EXPONENTIAL"),

9": ["name": "643", "

": {"name": "580", "type": "PDS_LLL_CHAR", "length": 13, "PDSInterpretor": "EXPONENTIAL"),

"12 ": {"name": "512", "13": ("name": "553", "type": "PDS_LLL_CHAR", "length": 12, "PDSInterpretor": "AMOUNT"}, "type": "PDS_LLL_CHAR", "length": 13, "PDSInterpretor": "RATE"),
}
}
}
