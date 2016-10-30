import sys
from providedcode import dataset
from providedcode.transitionparser import TransitionParser
from providedcode.evaluate import DependencyEvaluator

def get_data_from_lang(lang):
    if lang == 'swedish':
        return dataset.get_swedish_test_corpus().parsed_sents()
    elif lang == 'danish':
        return dataset.get_danish_test_corpus().parsed_sents()
    elif lang == 'english':
        return dataset.get_english_test_corpus().parsed_sents()
    else:
        raise ValueError("Please don't use {}, only use english, swedish or danish".format(lang))


def extract_lang_from_model_name(model):
    lang = model.split('.')[0]
    if not lang == 'swedish' and not lang == 'danish' and not lang == 'english':
        raise ValueError('Please only use english, swedish or danish models')
    else:
        return lang

def verify_lang_data(model, conll_output):
    try:
        lang = extract_lang_from_model_name(model)
        testdata = get_data_from_lang(lang)
        tp = TransitionParser.load(model)

        parsed = tp.parse(testdata)

        with open(conll_output, 'w') as f:
            for p in parsed:
                f.write(p.to_conll(10).encode('utf-8'))
                f.write('\n')

        ev = DependencyEvaluator(testdata, parsed)
        uas, las = ev.eval()
        print "\n=====Prediction of {}.model===== \nUAS: {} \nLAS: {}".format(lang, uas, las)
        return las
        pass
    except ValueError as e:
        print(e)

def cal_each_score(las):
    return (min(las,0.7)/0.7)**2

def main():
    lang_to_verify = []
    if len(sys.argv) == 1:
        lang_to_verify = ['swedish', 'danish', 'english']
    else:
        lang_to_verify = sys.argv[1:]

    las_list = []
    for lang in lang_to_verify:
        las = verify_lang_data(lang+'.model', lang+'.conll')
        las_list.append(las)

    if len(sys.argv) == 1:
        each_lang_score = [cal_each_score(l) for l in las_list]
        final_score  = (each_lang_score[0]+each_lang_score[1])*25+each_lang_score[2]*50
        print 'Score will be {}'.format(final_score)
if __name__ == '__main__':
    main()
