--DROP PROCEDURE wf_vcg_db.getOriginalTransaction(character varying, character varying, boolean, jsonb)
create or replace procedure wf_vcg_db.getoriginalTransaction(
inORN character varying
inVCNum character varying,
dataFound out boolean,
outParams out jsonb


) language plpgsql
as


$5


declare


panNum wf_vcg_db.t_clearing_tx_ledger.pan_orig%type;
panExp wf_vcg_db.t_clearing_tx_ledger.pan_exp_orig%type;


begin


dataFound = false;
SELECT json build object( recordID', the record id, 'VOID', void, 'reform', ann,
'pannum', pan Or IB,
partxp', pan exp orig), true into STRICT outparams, datafound
FROM if VCR Oh I Clearing tx ledger where orn - inORN and ve humanvenom
order by the record it LIMIT 1:
EXCEPTION
when salstate Perez then
dot around = False,
return;
end
$$
