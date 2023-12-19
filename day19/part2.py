workflows = {}
with open('test.txt') as inp:
    rules_txt, parts = inp.read().strip().split('\n\n')

for rule_txt in rules_txt.split('\n'):
    workflow_name, workflow = rule_txt[:-1].split('{')
    workflow = workflow.split(',')
    
    workflows[workflow_name] = []
    for rule in workflow[:-1]:
        workflows[workflow_name].append(rule.split(':'))
    workflows[workflow_name].append(workflow[-1])

def overlap_ranges(r1, r2):
    return (max(r1[0], r2[0]), min(r1[1], r2[1]))

def possibilities(rating_ranges):
    total = 1

    for rating in rating_ranges:
        if rating_ranges[rating][1] < rating_ranges[rating][0]:
            return 0
        
        total *= (rating_ranges[rating][1] - rating_ranges[rating][0] + 1)

    return total

def evaluate_workflow(workflow, rating_ranges):
    # Takes in a workflow and rating_ranges and returns a dictionary where
    # key = result
    # value = ranges that get to this result
    results = {}
    for (rule, result) in workflow[:-1]:
        # This variable represents the rating ranges required for this rule to be enacted
        new_rating_ranges = rating_ranges.copy()
        rating = rule[0]
        if rule[1] == '<':
            new_rating_ranges[rating] = overlap_ranges(rating_ranges[rating], (1, int(rule[2:])-1))
            rating_ranges[rating] = overlap_ranges(rating_ranges[rating], (int(rule[2:]), 4000))
        else:
            new_rating_ranges[rating] = overlap_ranges(rating_ranges[rating], (int(rule[2:])+1, 4000))
            rating_ranges[rating] = overlap_ranges(rating_ranges[rating], (1, int(rule[2:])))
        
        if not result in results:
            results[result] = []
        results[result].append(new_rating_ranges)
    
    if not workflow[-1] in results:
        results[workflow[-1]] = []
    results[workflow[-1]].append(rating_ranges)

    return results

total = 0
queue = [('in', {k:(1, 4000) for k in 'xmas'})]
for workflow_name, rating_ranges in queue:
    results = evaluate_workflow(workflows[workflow_name], rating_ranges)

    for new_workflow_name in results:
        new_rating_ranges_list = results[new_workflow_name]
        for new_rating_ranges in new_rating_ranges_list:
            if new_workflow_name == 'A':
                total += possibilities(new_rating_ranges)
            elif new_workflow_name != 'R':
                queue.append((new_workflow_name, new_rating_ranges))
print(total)