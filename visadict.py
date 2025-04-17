#VISA BASEII messages dictionary

TC= {'01': 'Returned Credit',

}

'02': 'Returned Debit',

'03': 'Returned Nonfinancial',

'04': 'Reclassification Advice transaction',

'05': 'Sales Draft',

'06': 'Credit Voucher',

'07': 'Cash Disbursement',

'09': 'Money Transfer transaction',

'10': 'Fee Collection transaction',

'15': 'Chargeback, Sales Draft',

'16': 'Chargeback, Credit Voucher',

'17': 'Chargeback, Cash Disbursement',

'19': 'Reversal Money Transfer transaction',

'20': 'Funds Disbursement transaction',

'25': 'Reversal, Sales Draft',

'26': 'Reversal, Credit Voucher',

'27': 'Reversal, Cash Disbursement',

'35': 'Chargeback Reversal of Sales Draft',

'36': 'Chargeback Reversal of Credit Voucher',

'37': 'Chargeback Reversal of Cash Disbursement

'46': 'Member Settlement Data transaction'
}
#TC05, TCRO

TCR 05X0

[1,2, 'Transaction Code',

[3,1, Transaction Code Qualifier',

[4,1, Transaction Component Sequence Number',

[5,19, 'Account Number (19),

[5,16, 'Account Number (16)',

[24,1, Floor Limit Indicator'],

[25,1, 'CRB/Exception File Indicator'],

'TransCode'],

'TCQ'],

'TransComponent Seq'],

'CardNum'],

'CAN'],

[26,1, 'Positive Cardholder Authorization Service

(PCAS) Indicator'],

[27,23, 'Acquirer Reference Number',

[50,8, 'Acquirers Business ID',

[58,4, 'Purchase Date (MMDD),

[62,12, 'Destination Amount,

[74,3, 'Destination Currency Code',

[77,12, 'Source Amount',

[89,3, 'Source Currency Code',

[ 92,25, Merchant Name',

[117,13, 'Merchant City',

[130,3, 'Merchant Country Code',

[133,4, 'Merchant Category Code',

[137,5, 'Merchant ZIP Code',

[142,3, 'Merchant State/Province Code',

[145,1, 'Requested Payment Service'],

[146,1, 'Reserved'],

[147,1, 'Usage Code',

[148,2, 'Reason Code',

[150,1, 'Settlement Flag'],

[151,1, 'Authorization Characteristics Indicator"],

[152,6, 'Authorization Code',

'RefNum'],

'AcquirerID'],

'TransactionDate'],

'CardholderAmt'],

CardholderCurrency'],

'TransactionAmt"],

'TransactionCurrency"],

'MerchantName'],

'MerchantCity'],

'MerchantCountry'],

'MCC'],

MerchantPostCode'],

'MerchantState'],

'UsageCode'],

MsgReasonCode'],

'AuthCode"],
[158,1, 'POS Terminal Capability'],

[159,1, 'International Fee Indicator'],

[160,1, 'Cardholder ID Method'],

[161,1, 'Collection-Only Flag'],

[162,2, 'POS Entry Mode'],

[164,4, Central Processing Date (YDDD)'],

[168,1, 'Reimbursement Attribute']
]
[1,2,

[3,1,

[4,1,

[5,6,

[11,6,

[17,6,

#TC05, TCR1

TCR_05X1 = [

Transaction Code',

'Transaction Code Qualifier',

'Transaction Component Sequence Number,

Issuer Workstation BIN'],

'Acquirer Workstation BIN'],

Chargeback Reference Number'],

'TransCode'],

'TCQ'],

ansComponentSeq'],

[23,1,

'Documentation Indicator'],

[24,50,

Member Message Text',

'MsgTextBlock'],

[74,2,

'Special Condition Indicators'],

[76,3,

'Fee Program Indicator'],

[79,1,

'Issuer Charge'],

[80,1,

*Reserved'],

[81,15,

*Card Acceptor ID',

CardAcceptorID'],

96,8,

'Terminal ID',

'TerminalID'],

[104,12,

"National Reimbursement Fee'],

[116,1,

"Mail/Telephone or Electronic Commerce Indicator'],

[117,1,

'Special Chargeback Indicator'],

[118,6,

"Interface Trace Number'],

[124,1,

'Unattended Acceptance Terminal Indicator'],

[125,1,

'Prepaid Card Indicator'],

[126,1,

'Service Development Field'],

[127,1,

'Response Code'],

[128,1,

'Authorization Source Code'],

[129,1,

'Purchase Identifier Format'],

[130,1,

Account Selection'],

[131,2,

'Installment Payment Count'],

[133,25,

'Purchase Identifier'],

[158,9,

'Cashback"],

[167,1,

'Chip Condition Code'],

[168,1,

'POS Environment']

]
#TC05, TCR5

TCR 05X5=[

[1,2,

[3,1,

[4,1,

[5,15,

[20,12,

[32,3,

[35,2,

[37,4,

[41,1,

[42,1,

[43,2,

[45,2,

[47,2,

[49,1,

[50,12,

[62,1,

[63,14,

[77,1,

[78,2,

[80,2,

[82,10,

[92,15,

[107,1,

[108,8,

Transaction Code',

Transaction Code Qualifier',

Transaction Component Sequence Number',

Transaction Identifier'],

"Authorized Amount"],

"Authorization Currency Code'],

'Authorization Response Code'],

'Validation Code'],

'TransCode'],

'TCQ'],

TransComponentSeq'],

Excluded Transaction Identifier Reason'],

'Processing Code'],

'Chargeback Rights Indicator'],

'Multiple Clearing Sequence Number'],

'Multiple Clearing Sequence Count'],

'Market-Specific Authorization Data Indicator'],

"Total Authorized Amount'],

Information Indicator'],

"Merchant Telephone Number'],

'Additional Data Indicator'],

"Merchant Volume Indicator'],

'Electronic Commerce Goods Indicator'],

Merchant Verification Value'],

"Interchange Fee Amount'],

Interchange Fee Sign'],

Source Currency to Base Currency Exchange Rate'],

Base Currency to Destination Currency Exchange Rate'],

'Optional Issuer ISA Amount'],

'Product ID'],

"Program ID'],

[116,8,

[124,12,

[136,2,

[138,6,

[144,24,

'Reserved'],

[168,1,

'CVV2 Result Code']

]
#TC05, TCR7

TCR 05X7 [

[1,2,

[3,1,

Transaction Code',

Transaction Code Qualifier',

[4,1,

Transaction Component Sequence Number',

[5,2,

Transaction Type'],

[7,3,

Card Sequence Number'],

[10,6,

'Terminal Transaction Date'],

[16,6,

Terminal Capability Profile'],

[22,3,

Terminal Country Code'],

[25,8,

Terminal Serial Number'],

[33,8,

"Unpredictable Number'],

[41,4,

"Application Transaction Counter'],

[45,4,

"Application Interchange Profile'],

[49,16,

"Cryptogram'],

'TransCode'],

'TCQ'],

TransComponentSeq'],

1

[65,2,

[67,2,

[69,10,

[79,8,

[87,12,

[99,2,

[101,16,

[117,2,

[119,2,

[121,30,

[151,8,

[159,10,

TCR_ELSE = [

[1,2,

[3,1,

[4,1,

Issuer Application Data, Byte 2'],

Issuer Application Data, Byte 3'],

'Terminal Verification Results'],

'Issuer Application Data, Byte 4-7'],

Cryptogram Amount'],

'Issuer Application Data, Byte 8'],

'Issuer Application Data, Byte 9-16'],

'Issuer Application Data, Byte 1'],

'Issuer Application Data, Byte 17'], 'Issuer Application Data, Byte 18-32'],

Form Factor Indicator'],

'Issuer Script 1 Results']

'Transaction Code'

Transaction Code Qualifier',

Transaction Component Sequence Number',

'TransCode'],

TCQ'],

TransComponentSeq'],
[5,164,

'Unknown']
]
TCR = {

'05X0':

TCR_05X0,

'06X0':

TCR_05X0,

'07X0':

TCR_05X0,

'15X0': TCR_05X0,

'16X0':

TCR_05X0,

'17X0':

TCR_05X0,

'25X0':

TCR_05X0,

'26X0':

TCR_05X0,

'27X0':

TCR_05X0,

'35X0':

TCR_05X0,

'36X0':

TCR_05X0,

'37X0':

TCR_05X0,

'05X1':

TCR_05X1,

'06X1':

TCR_05X1,

'07X1':

TCR_05X1,

'15X1':

TCR_05X1,

'16X1':

TCR_05X1,

'17X1':

TCR_05X1,

'25X1':

TCR_05X1,

'26X1':

TCR_05X1,

'27X1':

TCR_05X1,

'35X1':

TCR_05X1,

'36X1':

TCR_05X1,

'37X1':

TCR_05X1,

'05X5':

TCR_05X5,

'06X5':

TCR_05X5,

'07X5':

TCR_05X5,

'15X5':

TCR_05X5,

'16X5':

TCR_05X5,

'17X5':

TCR_05X5,

'25X5':

TCR_05X5,

'26X5':

TCR_05X5,

'27X5':

TCR_05X5,

'35X5':

TCR 05X5,
'36X5': TCR_05X5,

'37X5': TCR_05X5,

'05X7': TCR_05X7,

'06X7': TCR_05X7,

'07X7': TCR_05X7,

'15X7': TCR_05X7,

'16X7': TCR_05X7,

'17X7': TCR_05X7,

'25X7': TCR_05X7,

'26X7': TCR_05X7,

'27X7': TCR_05X7,

'35X7': TCR_05X7,

'36X7': TCR_05X7,

'37X7': TCR_05X7

}
