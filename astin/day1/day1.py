def number_finder(file):
    with open(file, 'r') as my_file:
        line = my_file.readlines()
        sum = 0
        for sentence in line:
            sentence = sentence.strip()
            converted = digit_convertor(sentence)
            first_digit = ''
            second_digit = ''
            t_or_f = False
            for ch in converted:
                if ch.isdigit() == True:
                    t_or_f = True
                    break
            if t_or_f == True:
                for ch in converted:
                    if ch.isdigit() == True:
                        first_digit = ch
                        break
                for ch in converted[::-1]:
                    if ch.isdigit() == True:
                        second_digit = ch
                        break
                number = first_digit + second_digit
                sum += int(number)
            else:
                sum += 0
    return sum


def digit_convertor(sentence):
    digit_dict = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five': '5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', 'zero':'0'}
    temp = ''
    for ch in sentence:
        temp += ch
        for k in digit_dict.keys():
            if k in temp:
                sentence = sentence.replace(k, digit_dict[k])
                temp = temp.replace(k, digit_dict[k])
    return sentence

print(number_finder('day1.txt'))
