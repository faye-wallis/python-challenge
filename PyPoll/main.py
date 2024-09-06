import os, csv, pathlib


#set filepath using os.path.join to allow use between different operating systems

filepath = pathlib.Path(__file__).parent / 'Resources' / 'election_data.csv'

#open csv, store header, and assign starter variables


with open(filepath, 'r') as election_data:
    reader = csv.reader(election_data)
    header = next(election_data)
    rows = list(reader)
    total_votes = len(rows)
    names = sorted(set([i[2] for i in rows]))
    stockham_votes = 0
    degette_votes = 0
    doane_votes = 0
    winner = ""
    for row in rows:
        if row[2] == names[0]:
            stockham_votes+=1
        elif row[2] == names[1]:
            degette_votes+=1
        elif row[2] == names[2]:
            doane_votes +=1
    if stockham_votes > degette_votes and doane_votes:
        winner = names[0]
    elif degette_votes > stockham_votes and doane_votes:
        winner = names[1]
    elif doane_votes > stockham_votes and degette_votes:
        winner = names[2]

    stockham_percent = (stockham_votes / total_votes)*100
    degette_percent = (degette_votes / total_votes)*100
    doane_percent = (doane_votes / total_votes)*100
    results = f'''
                Election Results
                ---------------------------
                Total Votes: {total_votes}
                ---------------------------
                {names[0]}: {"{:.3f}".format(stockham_percent)}% ({stockham_votes})
                {names[1]}: {"{:.3f}".format(degette_percent)}% ({degette_votes})
                {names[2]}: {"{:.3f}".format(doane_percent)}% ({doane_votes})
                ---------------------------
                Winner: {winner}
                ---------------------------
                '''
    output_path = filepath = pathlib.Path(__file__).parent / 'analysis.txt'
    with open(output_path, 'w') as analysis:
        analysis.write(results)
    print(results)

