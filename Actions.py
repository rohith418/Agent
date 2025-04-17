from clearinglib.transactions.record import ClearingRecord
from db dpmanager import DBManager
from psycopg2.extras import Json



class ClearingActions:


def IsFileAlreadyProcessed(self, fileID, mode) -> tuple[bool, dict]:
rsFiles = DBManager.fetchSQL("""SELECT clearing_id, file_uniq_ID, total_records, processed_ records, process_st_date, process_en date, file_total_amt, processed amt
FROM wf_vcg_db.t_clearing_file_info where trim(file_uniq_ID)-trim((%s)) and process_modea(%s)""", (fileID, mode))


if len(rsFiles)> 0:
    d = {

'clearingID': rsFiles[0][0], 'fileID': rsFiles[0][1], 'totRecords': rsFiles[0][2],
processed_records': rsFiles[0][3], "process_st_date': rsFiles[0][4], 'process_en_date': rsfiles[Ø][5]
'file_ total amt': rsFiles[0][6],
processed amt': rsFiles[0][7]
}

return (True, d)
else:


return (False, None)


# def selectFiles(self):
results = DBManager.fetchSQL C SELECT clearing id, file_uniq_ID, total_records, processed_records, process_stidate, process. en _date, file_total amt processed amt
FROM wf_vcg_db.t_clearing_file_info'"")


return results


def InsertClearingFile(self, file, fileID, mode, totalRecords) -> int:
rs DBManager.insertOrUpdate("""INSERT INTO wf_vcg_db.t_clearing_file_info(
file_name, file_uniq ID, total_records, process_st_date, process_mode)
VALUES (%s), (%s), (%s), now(), (*s) returning clearing. id''
(file, fileID, totalRecords, mode))


return rs
