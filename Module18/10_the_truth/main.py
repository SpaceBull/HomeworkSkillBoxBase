def shift_in_alphabet(shift_text, code_line):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet = list(alphabet)
    new_text = []
    for symbol in code_line.lower():
        if symbol not in alphabet:
            new_text.append(symbol)
            continue
        index = alphabet.index(symbol)
        index_symbol = index - shift_text  # (- на расшифровку, + на закодирование)
        if index_symbol >= 25:
            index_symbol -= 26
            new_symbol = alphabet[index_symbol]
            new_text.append(new_symbol)
        else:
            new_symbol = alphabet[index_symbol]
            new_text.append(new_symbol)
    return new_text


def line_shift(new_text):
    result = ''.join(new_text)
    word_shift = 3  # сдвиг в слове
    symbol = '/'
    answer = []
    flag = False
    for word in result.split():
        for _ in range(word_shift):
            letter = word[len(word) - 1]
            copy_word = list(word)
            copy_word.pop(len(word) - 1)
            copy_word.insert(0, letter)
            word = ''.join(copy_word)
            if symbol in list(word):
                word = list(word)
                word.remove('/')
                word_shift += 1
                result = ' '.join(answer)
                flag = True
        if flag:
            word += '.'
            flag = False
        answer.append(word)
    return result


text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/' \
       'jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/' \
       'dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/' \
       'ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/' \
       'svmf ipvhiBmu zqsbdujdbmju fbutc uz/' \
       'qvsj Fsspst tipvme wfsof qbtt foumz/' \
       'tjm omfttV mjdjumzfyq odfe/' \
       'tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/' \
       'hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/' \
       ' Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/' \
       'Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/' \
       'op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /' \
       'jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/' \
       ' bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'
print('Введите ниже: 1')
shift = int(input('Введите сдвиг в алфавите: '))  # 1 Вводим
new_roster = shift_in_alphabet(shift, text)
print(line_shift(new_roster))
