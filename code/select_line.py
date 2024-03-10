import re, sys

input_txt = sys.argv[1]
output_txt = sys.argv[2]
wer_1 = float(sys.argv[3])
wer_2 = float(sys.argv[4])
len_1 = float(sys.argv[5])
len_2 = float(sys.argv[6])


# 入力文から記号を除外する関数
def removeSymbols(sentence):
    return re.sub(r'[^\w\s]', '', sentence)

with open(input_txt, 'r', encoding='utf-8') as file:
    with open(output_txt, 'w') as f:
        for line in file:
            elements = line.strip().split('\t')
            if len(elements) == 6:
                iwslt_word = re.split(r'\s+', removeSymbols(elements[3].lower()).strip())
                asr_word = re.split(r'\s+', removeSymbols(elements[4].lower()).strip())
                len_division = int(len(asr_word)) / int(len(iwslt_word))
                if len_division <= 0:
                    len_division = -1 * len_division
                if  wer_1 <= float(elements[2]) <= wer_2 and len_1 <= float(len_division) <= len_2:
                    f.write(f"{line}")
