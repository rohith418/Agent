ļa virtuPay Clearing Service
his service processes all clearing files received on daily basis from networks like Visa/Mastercard (T5YS Sends these files on behalf of networks) and responds back on with acknowledgement on settlement
learing process is reconciliation of the online authrorized transactions and realizing adjustments of any fees, credit vouchers, and revert transactions
tach network follows their own Clearing file format and daily schedules for posting consolidated clearing files to Issuer Banks/Processors(like TSYS) via SFTP, or other channels


VISA uses BASE II clearing file format
Base II is
a


clearing and settlement file format from Visa
This is plain fixed length based Data Elements (Positional fields)
It is in plain text format
2. MASTERCARD uses IPM clearing file format
IPM (Integrated Product Messages) is the format follwed in Master card Global Clearing Management System (GCHS)
It is in EBCDIC (Entended Binary Coded Decimal Interchange Code), not readable. Its a hexacode representation
F
This requires IS08583 Parser and PDS parsing.


## VISA


Clearing process
Visa Clearing file will have


types of rows/records (Each line in one record).
3
1. *Header Record*:
It will have file information
like File version, origin bank id, destination bank id, date, file sequence, file generation date and time, file identifier, etc.,
2. "Transaction Information Record*
It will have transaction related fixed lenght data elements. Length and data elements are defined for each Transaction Code
Each record will start with 2 char Transaction Code. Ex: 05 - Purchase, 06
3.*Trailer Record*:
Original Credit or Returns
It will contains summary of transactions in the file
like Purchage total records total amounts, reversal records, reversal amount, credit voucher total records
and amount ..
etc.
### Transaction Codes

We can identify different transactions records based on transaction codes (First 2 char in the row/record).

Here are the different transaction code details:

Transaction Code

Type of Transaction |

Description |

TC05

Purchase/Acc Funding Success

TC06

Credit Voucher/Original Credit Success

TC06

Funds return

Success

TC07

Widthdrawal

| Success

TC25

Purchase Cancellation Canceled

TC26

Original Credit Cancellation Canceled

TC27

Withdrawal Cancellation Canceled

### More details on Transaction codes

Transaction Code |

Decription |

TC01 Returned Credit

TC02 Returned Debit

TC03 Returned Nonfinancial |

TC04 Reclassification Advice transaction

TC05 Sales Draft

TC06 Credit Voucher

TC07 Cash Disbursement

TC09 Money Transfer transaction

TC10 Fee Collection transaction

TC15 Chargeback|

TC16 Chargeback

TC17 | Chargeback

TC19 Reversal Money Transfer transaction

TC20 Funds Disbursement transaction

TC25 Reversal

TC26|Reversal

TC27 Reversal

TC35|Chargeback Reversal of Sales Draft TC36 Chargeback Reversal of Credit Voucher

TC37|Chargeback Reversal of Cash Disbursement

TC46 Member Settlement Data transaction
### VISA BASE II Fixed Length Data Elements for most transactions

Start Pos Fixed Length Data Element|

|1|2| Transaction Code

|3|1|Transaction Code Qualifier

4|1| Transaction Component Sequence Number |

15/19 PAN Account Number (19)|

|24|1|Floor Limit Indicator

|25|1|CRB/Exception File Indicator|

|26|1| Positive Cardholder Authorization Service (PCAS) Indicator

27/23 Acquirer Reference Number |

|50|8|Acquirers Business ID

58/4 Purchase Date (MMDD) |

62/12 Destination Amount

|74|3| Destination Currency Code

77/12 Source Amount

|89|3|Source Currency Code

|92|25|Merchant Name

117 13 Merchant City

1303 Merchant Country Code

133/4 Merchant Category Code |

137/5 Merchant ZIP Code

142|3|Merchant State/Province Code

145|1| Requested Payment Service

146|1| Reserved

| 147|1| Usage Code

148|2| Reason Code

| 150|1|Settlement Flag|

151|1| Authorization Characteristics Indicator

152|6|Authorization Code |

158 1 POS Terminal Capability|

159 1 International Fee Indicator|

|160|1|Cardholder ID Method

|161|1| Collection-Only Flag

162/2 POS Entry Mode)

164 4 Central Processing Date (YDDD) |

168|1| Reimbursement Attribute

###VISA BASE II Transaction Processing Rules:
Transaction Codes 90, 91 and 92 are ignored as they are header and trailer records, they will be processed separately Based on Transaction Code (TC), Transaction Code Qualifier (TCQ) and Usage Code (UC), we need to validate the record as per below table.

Input TC

Input

TCQ

Input

UC

Validate

01

Original Sales Presentment | D |

TC05

TC05

01

TC05

1

TC06

TC06

2

TC07

1

TC07

TC25

TC26

TC27

TC15

TC16

TC17

TC35

TC36

TC37

Processing Type |

Credit/Debit |

Second Sales Presentment (Linked) | D |

Account Funding | D |

| Credit Presentment (Linked) | C |

| Cardholder Funds Transfer | C

Original Cash Presentment |

DI

Second Cash Presentment (Linked) | D

Sales Reversal (Linked) C

Credit Reversal (Linked) | D|

Cash Reversal (Linked) | C

Sales Chargeback (Linked) | C |

Credit Chargeback (Linked) | D |

Cash Chargeback (Linked) | C

Sales Chargeback Reversal (Linked) | D| Chargeback Reversal (Linked) | C |

Credit Cash Chargeback Reversal (Linked) | D |

For Original transacation Records there should be existing Authorization record exists with ARN (Acquirer Reference Number)

For Linked transactions along with Authorization record there will should be one original transaction record with same ARN exists

Apply all rules to Identify fraud transactions

Authorised Amount is less than clearing amount

Too many transaction records on one authorization

Clearing date is after 7 days of authorization

TODO: Update other rules

## MASTERCARD Clearing process
Mastercard used to have INET clearing system, but now it was replaced their clearing file format with an 150-8583 format called IPM (Integrated Product Messaging).

IPM Clearing file is EBCDIC encoded.

EBCDIC stands for Extended Binary Coded Decimal Interchange Code, its a old IBM interchange code used in mainframe systems, every ASCII has its equalant EBCDIC code. IPM File comes with 1644-697 Header message and 1644-695 trailer message

IPM File contains multiple transaction message including header and tailer message.

### MasterCard Key messages and their order.

Message Type MTI (DE1) Function Code (DE24) |

File Header 1644|697|

First Presentments 1240|200|

Second Presentments, Full|1240|205|

Second Presentments, Partial|1240|282 |

Financial Detail Addendum<br/>(Follows Presentments) | 1644 696 |

File Trailer|1644|695|

#### Other Message Types from MasterCard IPM File

MIT-Function Code Description

*1442-450*

First Chargeback (Full)/1442 for the full First Presentment/1240 message amount. Initiated by the issuer.

*1442-453*

First Chargeback (Partial)/1442 for part of the First Presentment/1240 message amount. Initiated by the issuer.

*1442-451*

Arbitration Chargeback (Full)/1442 for the full First Presentment/1240 amount. Initiated by the issuer.

*1442-454*

Arbitration Chargeback (Partial)/1442 for part of the First Presentment/1240 amount. Initiated by the issuer

*1740-XXX*

Miscellaneous Fee Collection

*1644-693*

Text message. Broadcast Test memessage for any outages or updates

*1644-699* *1644-691* File Reject (System sends the file reject between a file header and a file trailer.) Message Exception (The rejected message follows its associated message exception message)

### MasterCard Clearing File 1508583 Schema Spec which we used in VirtuPay

Data Element Description Data Extract Type Length/Max Length
12 PAN LL_CHAR|19|

13 PROCESSING CODE CHAR_FIXED|6|

14 AMOUNT, TRANSACTION CHAR FIXED|12|

15 AMOUNT, SETTLEMENT CHAR FIXED |12|

16 AMOUNT, CARDHOLDER BILLING CHAR_FIXED|12|

8 AMOUNT, CARDHOLDER BILLING FEE CHAR_FIXED|8|

9 CONVERSION RATE, SETTLEMENT CHAR_FIXED|8|

10 CONVERSION RATE, CARDHOLDER BILLING CHAR_FIXED|8|

12 LOCAL TRANSACTION TIME CHAR_FIXED|12|

14 EXPIRY DATE CHAR FIXED|4|

22 POS DATA CODE CHAR FIXED|12|

23 CARD SEQUENCE NUMBER CHAR_FIXED|3|

24 FUNCTION CODE CHAR FIXED|3|

25 MESSAGE REASON CODE CHAR_FIXED|4|

26 CARD ACCEPTOR BUSINESS CODE CHAR FIXED|4|

30 AMOUNTS ORIGINAL EBC_CHR_FIXED|24|

31 ACQUIRER REFERENCE DATA LL_CHAR|99| INST ID CODE LL_CHAR|11|

32 ACQUIRER

33 FORWARDING INST ID CODE | LL_CHAR|11|

37 RETRIEVAL REFERENCE NUMBER EBC_CHR_FIXED|12|

38 AUTH RESPONSE EBC_CHR_FIXED|6|

40 SERVICE CODE EBC_CHR_FIXED |3|

41 CARD ACCEPTOR TERMINAL IDENTIFICATION EBC_CHR_FIXED|8|

42 CARD ACCEPTOR ID CODE EBC CHR FIXED|15|

43 CARD ACCEPTOR NAME/LOCATION LL CHAR | 99|

49 TRANSACTION CURRENCY CODE EBC_CHR_FIXED|3|

150 CURRENCY CODE RECONCILIATION EBC_CHR_FIXED|3|

51 CARDHOLDER BILLING CURRENCY CODE EBC_CHR_FIXED|3|

154 ADDITIONAL AMOUNTS LLL_EBC_CHAR 201

55 ICC SYSTEM RELATED DATA LLL_EBC_CHAR/255

63 RESERVED PRIVATE LLL_EBC_CHAR | 999 | |

71 MESSAGE NUMBER EBC_CHR_FIXED|8

72 DATA RECORD LLL EBC_CHAR 999|

73 DATE ACTION CHAR FIXED|6|

193 TXN DEST INST ID CODE LL_CHAR|11|

194 TXN ORIG INST ID CODE LL_CHAR 11

95 CARD ISSUER REF DATA LL_CHAR|10|

100 RECEIVING INST ID CODE LL CHAR 11

111 AMOUNT CURR CONV ASSESSMENT LLL EBC_CHAR|12|

127 NETWORK DATA LLL_EBC_CHAR 999|

48 MASTERCARD FIELD 48, type LLL BINARY PDS]

62 ADDITIONAL DATA 2, type LLL BINARY | PDS

123 ADDITIONAL DATA 3, type LLL BINARY PDS|

124 ADDITIONAL DATA 4, type LLL BINARY PDS

125 ADDITIONAL DATA 5, type LLL BINARY POS

#### Defination of Data Extract Type's
All EBCDIC Fields are 'cp500" encoded, we need to decode when returning the data.

CHAR FIXED:

Fixed Length Charecter field, if length is 6 then read next 6 bytes LL CHAR:

-LLL EBC CHAR:

Variable Length Charecter field, first 2 bytes gives length of the data, find lenght and read next no of bytes length, Ex: first two bytes give 4 as lenght then read next 4 bytes for data

EBC CHR FIXED:

Variable Length Charecter field, first 3 bytes gives length of the data, find lenght and read next no of bytes length. Ex: first two bytes give 4 as lenght then read next 4 bytes for data, do "cp5ae" decoding.

-Fixed Length EBC field, if length is 6 then read next 6 bytes , do decoding with "cp500"

-Variable All Other:

LLL BINARY: Length binary field, first 3 bytes gives length of the data, find lenght and read next no of bytes length. Ex: first two bytes give 4 as lenght then read next 4 bytes for data, do 'cp500 decoding.

Fixed Length Binary field, if length is 6 then read next 6 bytes

MasterCard PDS Fields:

POS data is a schema with RDW (Record Desciptor Word)

Parse entire PDS data in a loop until all PDS fields in the data is finished.

First 4 chars are PDS Tag field

Next 3 chars represents length of value of the tag available next to it.

Extract next set of chars based on length above, which is a value.

Ex: PDS Data is: 0159002US

Tag is first 4 chars: '0159"

Value is of length int(002)-2

next 2 chars is value: us

POS data may contain multple tags, we just need to extract sameway in loop.

#as MasterCard Clearing: Some Extra Information & Glossary

Glossary:

Record Descriptor Word (ROW)

PDS

Variable Block Spanned (VBS)
PDS

MTI is 1240 and DE24 in (200, 205, 282)

==> process may includes next record also to check if it is addendum record..

==> addendum message is MTI=1644 and DE24 696

==> there can be multple addendum messages till next record comes
DE31 An ARN or Acquirer Reference Number is a distinct marker assigned to credit or debit card transactions as the  funds move from the merchant's bank to the card holders bank through a payment processor that a friend's number is essential for tracking and resolving errors.Or this rupen, is that we occurred during the transaction potential transverse and disability, an online payment processes
