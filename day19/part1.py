def gen_rule_function(question):
    rating = question[0]
    if question[1] == '<':
        return lambda part: part[rating] < int(question[2:])
    return lambda part: part[rating] > int(question[2:])


rules = {}
with open('input.txt') as inp:
    rules_txt, parts = inp.read().strip().split('\n\n')

for rule_txt in rules_txt.split('\n'):
    rule_name, workflow = rule_txt[:-1].split('{')
    workflow = workflow.split(',')
    
    new_workflow = {'rules':[], 'default':None}
    for rule in workflow[:-1]:
        question, result = rule.split(':')
        new_workflow['rules'].append((gen_rule_function(question), result))
    new_workflow['default'] = workflow[-1]
    
    rules[rule_name] = new_workflow

accepted = []
for part in parts.split('\n'):
    part = eval(part.replace('=', ':').replace('x', "'x'").replace('m', "'m'").replace('a', "'a'").replace('s', "'s'"))
    
    c_workflow = 'in'
    while True:
        if c_workflow == 'A':
            accepted.append(part)
            break

        if c_workflow == 'R':
            break

        for rule in rules[c_workflow]['rules']:
            if rule[0](part):
                c_workflow = rule[1]
                break
        else:
            c_workflow = rules[c_workflow]['default']

total = 0
for part in accepted:
    total += sum(part.values())
print(total)