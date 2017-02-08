import subprocess
import json

result = subprocess.check_output('python curlgen.py | xargs -n 1 bash -c', shell=True)

data =  json.loads('[' + result.replace('}{', '},{') + ']')

transactions = [t for d in data for t in d.get('data', {}).get('transactions', [])]


fees = [
    [t.get('datetime_created'), ((t.get('funding_source') or {}).get('fee') or {}).get('variable_percentage', 0) * t.get('amount') / 100. ]
    for t in transactions
]

print 'List of all transaction fees:'
print '\n'.join([str(t[0]) + ' ' + str(t[1]) for t in fees])
print ''
print 'Total:'
print sum([t[1] for t in fees])
