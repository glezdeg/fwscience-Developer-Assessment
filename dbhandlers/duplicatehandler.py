# -*- coding: utf-8 -*-
import pandas as pd
import os
import difflib
import json

#report creation method
def report_duplicates(data_frame,
                      column_to_report,
                      reportdir,
                      match_sensitivity=0.9):
    
    #use pandas to create a dataframe
    DF=pd.DataFrame(data_frame)
    
    #select column to report duplication
    series=DF[column_to_report]
    
    #get unique values out of the series
    count=series.value_counts()
    
    #creating json dir and duplicates dict for the report
    report_file=os.path.join(reportdir,'report.json')
    duplicates={}
    
    #loop over the diferent names
    for name in count.index:
        #use of difflib to get close matches
        duplicate_match=difflib.get_close_matches(name, series,cutoff=match_sensitivity)
        #removing self match
        duplicate_match=[elem for elem in duplicate_match if name!=elem]
        #counting duplicates and duplicates list
        if len(duplicate_match)>0:
            duplicates[name]={
                'num of duplicates':len(duplicate_match),
                'duplicates':duplicate_match}
            print(name,len(duplicate_match))
    
    #writing json report
    report=open(report_file,'w')
    json.dump(duplicates,report,indent=4, sort_keys=True)
    report.close()
      
if __name__=='__main__':
    current_dir = os.path.abspath(os.path.dirname(__file__)) 
    file_dir=os.path.join(current_dir,'companies_example_data.csv')
    DF=pd.read_csv(file_dir)
    report_duplicates(DF,'name',current_dir)

    