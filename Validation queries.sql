SELECT bin_range_id, vc_bin_prefix, vc_bin_start_range, vc_bin_end_range, active, created_at, updated_at
FROM wf_vcg_db.t_vc_binrange;


SELECT * from wf_vcg_db.t_card_network;


select c.network_id, c.network_name, vc_bin_prefix from wf_vcg_db.t_card_network c, wf_vcg_db.t_vc_binrange b
where b.bin_range_id-c.df_bin_range_id;


select * from wf_vcg_db.t_log_info order by created_dtz desc;


select from wf_vcg_db.t_pan_ master order by created at desc:


select * from wf_vcg_db.t_vc_master order by created_at desc;
select vc_id, vc_num, status, vc_exp,
)
gultiuse, tolerance_min, tolerance max, pan_id, valid_till. VC_ flag from wf_vcg db. t_vc_master order by creat


select from wf_vcg_db.t_vcn_allowed_mcc;
select now();
