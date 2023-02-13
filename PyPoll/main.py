import os
import csv
import numpy as np
import pandas as pd
csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")
with open (csvpath, encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Skipping the header
    next(csvreader)
    election_data_list = list(csvreader)
    total_number_of_votes = 0
    candidates_voted = []
    # Finding unique names of the candidates    
    for row in election_data_list:
        if row [2] not in candidates_voted:
            candidates_voted.append(row[2])
    
    # Finding total votes    
    for row in election_data_list:
        total_number_of_votes += 1 
    
    # Finding total votes, and the vote percentage of each candidate    
    candidates_voted_counted = []
    for i in range(len(candidates_voted)):
        total_personal_votes = 0
        percentage = 0
        for row in election_data_list:
            if row[2] == candidates_voted[i]:
                total_personal_votes += 1
            percentage = round((100 * total_personal_votes/total_number_of_votes), 3)
        candidates_voted_counted.append([candidates_voted[i], total_personal_votes, percentage])
    
    # Fiding the winner  
    dataf = pd.DataFrame(candidates_voted_counted, columns=['Candidate', 'Votes', 'Percentage'])
    winner_vote = dataf['Votes'].max()
    winner_name = dataf[dataf['Votes']==winner_vote].Candidate.iloc[0]
  
  
    # Prepearing the output  
    def results():
        final_results = ''
        for i in range(len(candidates_voted_counted)):
            final_results += (f'{candidates_voted_counted[i][0]}: {candidates_voted_counted[i][2]}% ({candidates_voted_counted[i][1]}) \n \t  ')
        return final_results
    

    final_results1 = results()
    output = str((f'''          Election Results
          -------------------------------------------------------
          Total Votes: {total_number_of_votes}
          -------------------------------------------------------
          {final_results1}
          -------------------------------------------------------
          Winner: {winner_name}          
          -------------------------------------------------------
          '''))

    print(output)
    savepath = os.path.join('PyPoll', 'analysis.txt')

    with open(savepath, 'w') as output_file:
        output_file.write(output)