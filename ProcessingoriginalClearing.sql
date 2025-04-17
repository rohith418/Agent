create or replace procedure wf_vcg_db. processQriginalClearing(
tranJS0N jsonb,
retJS0N out jsonb
outInt out int
) language plpgsql
as
$S
declare


`uleset jsonb:= '("validatePAN": true, "validateExp":true, "validateCvv":true, "noOfDaysToAuth": 7, "excessAuthAmount":10 )'::jsonb:
cardScheme int:-tran]SON->> 'CardType
v_vc_id wf_vcg_db.t_clearing_tx_ledger.vc_id%type;
cardFound bpool:=false;
orginalCard jsonb := "[]"::jsonb;
panNum wf_vcg_db.t_clearing_tx_ledger.pan_orig%type;
panExp wf_vcg_db.t_clearing_tx_ledger.pan_exp_onig%type;
lk_ORN character varying;
lk_acquirerID character varying;
lk_RecordID character varying;
lk_AuthFound boolean:=false;
inVC_NUM character varyings
linkFound boolean;
outparams jsonb;
v_auth_id wf_vcg_db.t_auth_ledger.record_id%type;
v_auth_dt wf_vcg_db.t_auth_ledger.created_at%type;
v_tx_amount wf_vcg_db.t_vc_master.clearomg_amount%type;
begin
jinsert into wf_vcg_db.t_log_info(blob) values(tranJSON::TEXT);
inVC_NUM = tranJSON->>"CardNum';
Process_Type = tranJSON->>"ProcessType';
v_tx_amount = tranJSON->>'TransactionAmt';
Clearing_Type - tranJSON->>ClearingType';


if Process_Type='L' Then
CALL wf_vcg_db.getoriginaltransaction(lK_ORN
if not linkFound then
TODO: Fraud check


lk_RecordID = outparams ->> 'recordID';
panExp - outparams ->> 'panExp
panNum = outparams ->> 'panNum
outparams ->> 'vcID'
end if;
end if;


,inVC_NUM, linkFound, outparams);


else


if Process_Type ='0"
begin


or not linkFound then


SELECT m.pan, pm.pan_exp, vcm.vc_id, true
INTO strict panNum, panExp, v_vc_id, cardFound
FROM wf_vcg_db.t_vc_master vcm, wf_vcg_db.t_pan_master
WHERE vcm.vc_num - inVC_NUM AND vcm.pan_id - pm.pan_id;


pm


exception
when no_data_found then
cardFound
false;
panNum = tranJSON ->> 'CardNum';
panExp = tranJSON ->> 'CardExpDate';
end;


if cardFound then
if Process_Type= '0 and Clearing_Type -"D' then
BEGIN
true


select record_id, tx_date,
into strict
v_auth_id, v_auth_dt, lk_AuthFound from wf_vcg_db.t_auth_l
where vc. id-v_vc_id and record_type in (0,1) and exception_cd-0
and settled_cd 'U';


exception
when no_data_found then
1k_AuthFound
false;
END;
If 21 Authfound then
and If
update of very dot auth lederer set settled cd's where record Idw ruth ids
If Clearing Type = 'D' then
UPDATE of UCB do I've master
SET Clearing amount - Clearing amount + VIX amount,
clearing count = clearing count + 1,
last clearing at - to date(tran)SON->> Transactionbate', WHOOHIREMISS :),
updated at = now(),
status = C- TODD: It should be based on amount )= overall Limit (Cumulative)
modified by = 'VEG-CLE RING
and If
WHERE Ve 10= Vive Id
If Clearing Type = C' then
--TOO0- Check Fraud code 15- Credit force posting
UPDATE of VCE do I ve easter
SET clearing amount - clearing amount - u the amount,
scoring count - Clearance count + 1,
last clearing of - to date(tran]SON 33 TransactionDate, SMOOTHIEMISS :),
updated at = now(),
status = C' -7000: It should be based on amount 2- overall limit (Cumulative)
and FIRE By = 'VCG-CLEARING'
WHERE vc_id= v_vc_id;
end if;
end if;
end if;
SELECT tx_record_id, orn, vc_id, clearing_id mit, tx_type, pan_orig, pan_exp_orig, trans_amt, cardholder amt, recon_amt, created_at, currency_code_trans, currency_code_ch, currency_recon_cd, pos_c data_codes, function_cd,msg_reason_cd, mcc, acquirer_ref merchant_id, retr_ref_num, auth_cd, terminal_id, merchant name,
merchant_city,
merchant. addr, merchant_ state,merchant_pincd,merchant country, msg_txt. block, fraud_flg, settlement_dt, settlement month, auth_txid, addi_fldl addi f1d2, addi_fld3, addi.fld4, status_cd, orig_txid, VC_amt, clearing type, orig_or linked, vc_num, VC_exp, card acceptor id, pcode, revl. indicator, acquirer-id receiver_id, exchange. tx_rate, forwinst_ id, acquirer_map id, trans_cd, tcq, usage_cd,tx_desc_cd, dest_id, tx_desc_text, fx_amt, fx_posting dt, exception_type, is_stp


FROM wf_vcg_db.t_clearing_tx_ledger where orn


if cardFound then
orginalCard - json_build_object(
num'
panNum,
panExp', panExp);


end if
ret]S0N - json_build_object(
found`, cardFound,
'orignalCard', orginalCard
refNum', orgRefNum


outInt S
20;
return;


end
$$
