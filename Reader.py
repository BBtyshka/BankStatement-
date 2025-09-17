import camelot as cm

tables = cm.read_pdf('eStatementFile_20250917122947.pdf')

print(f'number of tables found: {len(tables)}')

for i,table in enumerate(tables):
    table.to_csv(f'tableN{i}.csv')

    