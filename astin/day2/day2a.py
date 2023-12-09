def possible_checker(file):
    with open(file, 'r')as my_file:
        line = my_file.readlines()
        sum_IDs = 0
        for sentence in line:
            sentence = sentence.strip().split(':')
            id = sentence[0].split()[1]
            games = sentence[1]
            set = games.split(';')
            t_or_f = True
            for results in set:
                if 'red' in results:
                    index = int(results.find('red'))
                    if index - 3 != ' ':
                        number = int(results[index-3:index-1])
                    else:
                        number = int(results[index-2])
                    if number > 12:
                        t_or_f = False
                        break
                if 'green' in results:
                    index = results.find('green')
                    if index - 3 != ' ':
                        number = int(results[index-3:index-1])
                    else:
                        number = int(results[index-2])
                    if number > 13:
                        t_or_f = False
                        break
                if 'blue' in results:
                    index = results.find('blue')
                    if index - 3 != ' ':
                        number = int(results[index-3:index-1])
                    else:
                        number = int(results[index-2])
                    if number > 14:
                        t_or_f = False
                        break
            if t_or_f == True:
                sum_IDs += int(id)
    return sum_IDs
            

print(possible_checker('day2.txt'))
