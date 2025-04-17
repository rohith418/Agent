PROCEDURE: wf_vcg_db.createVCNassignPAN(jsonb,jsonb,bigint)
DROP PROCEDURE IF EXISTS wf_vcg_db.createVCNassignPAN(jsonb,jsonb,bigint).
CREATE OR REPLACE PROCEDURE wf_vcg_db.createVCNassignPAN(
IN vcnison jsonb,
OUT retjson jsonb,
OUT outint bigint)
LANGUAGE 'plpgsql
AS $BODY$
declare
MULTI_USAGE_MAX smallint := 999;
SINGLE VC_FLAG smallint :- 6356;
MULTI_VC_FLAG smallint := 4116;
sourcePAN wf_vcg_db.t_pan_master.pan%type;
sourcepANExpiry wf_vcg_db. t_pan_ master.pan_exp%type;
sourcePANcvv wf_vcg_db.t_pan_master.pan_cvv%type;
vcStartDate wf_vcg_db.t_vc_master.valid_from%type.
vcEndDate wf_vcg_db.t_vc_master.valid_till%type;
allowedMCCs jsonb;
vcnAmount wf_vcg_db.t_vc_master.vc_amt%type;
vcnMultiUse wf_vcg_db.t_vc_master.multiuse%type;
vcnCurrency wf_vcg_db.t_Vc. master crrency. id%type;
vcToleranceUnder wf_vcg_db.t_vc_master.tolerance_minxtype;
vcToleranceOver wf_vcg_db.t_vc_master.tolerance_max%type;
vcNum wf_vcg_db.t_vc_master.vc_idxtype;
vcnId
vcCVV wf_vcg_db.t_vc_master.vc_num%type;
wf_vcg_db.t_vc_master.vc_cvv%type;
vcEXP wf_vcg_db.t_vc_master.vc_exp%type;
panID wf_vcg_db.t_vc_master.pan_id%type;
binrangeID wf_vcg_db.t_vc_master.binrange_id%type;
statusCD wf_vcg_db.t_vc_master.status%type;
vcnFlag wf_vcg_db.t_vc_master.vc_flag%type:= SINGLE_VC_FLAG;
rMcc record;
begin


insert into wf_vcg_db.t_log_info(blob) values(vcnjson::TEXT):
sourcePAN = vcnjson->>"sourcePAN';
sourcePANExpiry = vcnjson->>"sourcePANExpiry"
sourcePANcVV = vcnjson->>'sourcePANcVy'
-raise exception 'Json-sourcePAN: % sourcePAN;
vcStartDate = vcnjson->>'vcStartDate';
vcEndDate = vcnjson->>'vcEndDate';
allowedMCCs - vcnjson->"allowedMCCs'
vcnAmount = vcnjson->>"vcnAmount';
vcnMultiuse vcnjson->>"vcnMultiUse';
vcnCurrency = vcnjson->> "vcnCurrency"
vcToleranceUnder = vcnjson->>"vcToleranceUnder';
vcToleranceOver = vcnjson->>"vcToleranceOver'
vcNum = vcnjson->>"vcNum'
vcCW - vcnjson->>"vcCVV';
vcEXP
vcnison-b> "VcEXP


binrangeID = vcnjson->>"binrangeID"
statuscD = "AM;


begin


SELECT pan_id
INTO strict panID
FROM wf_vcg_db.t_pan_master
WHERE pan= sourcePAN;
exception
when no_data_found then
begin


insert into wf_vcg_db.t_pan_master(pan, pan_cvv, pan_exp, active) values (sourcePAN, sourcePANcVV, sourcePANExpiry,'A');
select currval(`wf_vcg_db.t_pan_master_pan_id_seq') into panID;
exception


when others then
outint
-1;
raise exception 'PAN Insert failed: %


SQLERRM;


end;


end;


if vcnMultiuse = 'Y' then
vcnFlag - MULTI_VC_FLAG;
end if;


INSERT INTO wf_vcg_db.t_vc_master(
vC_num, vC_cvV, vc_exp, pan_id, binrange_id, status,currency_id, vc_amt, multiuse, tolerance_min, tolerance_max,
created_by, modified_by, valid_from, valid_till, tx_limit, overall_limit, vc_flag)
VALUES (vcNum, vcCVV, VCEXP, panID
DinrangeID.
statusCD, vcnCurrency, vcnAmount, vcnMultiUse,
vcToleranceUnder,
vcToleranceover.
VirtuPay', "VirtuPay', vcStartDate, vcEndDate, vcnAmount, (vcnAmount+vcToleranceOver), vcnFlag):
select currval('wf_vcg_db.t_can_master _can_id_seq') into vcnId;
for rMcc in (select jsonb_array_elements_text(allowedMCCs) mcc)
loop
--raise notice '%', rMcc.mcc;
insert into wf_vcg_db.t_vcn_allowed_mcc(vc_id, mcc_cd) values (vcnId,rMcc.mcc);
end loop;


sexect currval('wf_vcg_db.t_can_master_can_id_seq") into vcnId;
」
‣, vetnavate, VcnAmount, (vcnAmount+vcToleranceOver), vcnFla,
verureränceUnde


retjson json_build_object(


panID'
panID,
vcnID', vcnId ,
message, 'success


outInt = vcnId;
return;


end


$BODY$;
ALTER PROCEDURE wf_vcg_db.createVCNassignPAN(jsonb,jsonb,bigint.
OWNER TO postgres;
