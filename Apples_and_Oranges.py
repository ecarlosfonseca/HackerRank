string = 'TestCaseTestCase'
sub_string = 'CaseT'

counter = 0
for v in range(len(string)):
    if string[v] == sub_string[0]:
        for i in range(1, len(sub_string)):
            if string[v+1]:
                if string[v+1] == sub_string[i]:
                    counter += 1
            else:
                pass

print(counter)