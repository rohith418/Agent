VirtuPay Authorization Service fulfills the need of approving on declining the credit using Virtual Cards (VCN)
Its similar to any other Card authrorization process, except an additional layer which only knows about VCN details.
In regular auth process, PAN will be directly authorized by
Issuer/Processor. In VCN auth process, We will have VirtuPay
additional layer which will only have details about VCN.
as


a## Request:The contents of the auth and reversal tags are


ARN - an internal field used to match reversals to authorisations, ISO Field 37
Currency Code
field that overwrites ISO field 49
a


### Response: content of auth response


![alt text](card-auth-flowl.svg)
a Flow Link](https://github.wellsfargo.com/pages/U785068/mermaid-lite-editor/#/view/Z3JhcGggTFIKQVtDYXJkIEhvbGRlc10gLS0-fEF1dGggTIzc2FnZXwgQihBY3F1aXJlcikKQiAtLT4gQ1t0ZXR3b3JFIFZpc2EvTWFzdGVyQ2FyZF0KQyAtLT4gRFtDYXJkIElzc3vlci9Qcm9jZXNzb3JdCkOgLS0
[EV7Q2FyZCBJc3N1ZXIvUHJvY2Vzc29yfQpFIC0tPnxQ05BIEZbZmEGZmEtY2hlY2sgVmlydHVQYxldCkUgLS0-fFBBTnwgRFtBCHByb3ZlL1JlamVjdFøKRiAtLT4gRQpEICOtPnxQQU4gQS9SfCBDCKMgLS0-fFBBTiBBL1JBIEIKQiAtLT58UEFOIEEvUnwgQQ
The entire communication of authorization happens using IS08583 messaging. TO know about IS08583, please refer [a relative link](README-IS08583.md) READHE-IS08583.md:


Amount - the amount of tBAhe transaction, in minor units. ISO Field 4
MID - the merchant index, as discussed in the Acquiring Server description. ISO Field 42
the terminal id of the merchant, as discussed in the Acquiring Server description. I50 Field 41
TID
Transaction Date
transaction date time, ISO Field 7
PAN - In Virtual Card Case it will be the card number of the VCN. ISO Field 2
the expiry date of the VCN
EXP Date
ISO Field 14
the card validation value of the VCN. ISO Sub Filed 10 of Field 126
AW/CW
Merchant Category Code. ISO Field 18
HCC


On Top of above fields We will get addition below
as
response.
In request we will get VCN, but in response we will send Original PAN instead of of VCN.
PAN


send the VCN back in response in Additional Data. In I5O Field 102
VCN
reconsiliation purpose
we
For


Auth Response
Approved/Rejection Codes


Few codes:


-0
Approved
14: Invalid Card Number
54
Expired Card
- 63 Security Violation
ADDITIONAL RESPONSE DATA


### Authorization Flow:
![Auth Flow](devtools/apitesterui/static/authflow.svg)


Information about more validations.


I50 Sub Fields of 44.
### Authorization Flow:


![Auth Flow](devtools/apitesterui/static/authflow.svg)
