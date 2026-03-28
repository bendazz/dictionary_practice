from intel_reports import reports 

def retrieve_report(classification:str):
    report_list = []
    for report in reports:
        if report["classification"] == classification:
            report_list.append(report)
    return report_list

print(retrieve_report("TOP SECRET"))