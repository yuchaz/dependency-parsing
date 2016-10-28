import random
from providedcode import dataset
from providedcode.transitionparser import TransitionParser
from featureextractor import FeatureExtractor
from transition import Transition

def get_train_data_from_lang(lang):
    if lang == 'swedish':
        return dataset.get_swedish_train_corpus().parsed_sents()
    elif lang == 'danish':
        return dataset.get_danish_train_corpus().parsed_sents()
    elif lang == 'english':
        return dataset.get_english_train_corpus().parsed_sents()
    else:
        raise ValueError("Please don't use {}, only use english, swedish or danish".format(lang))

def main():
    lang_train_list = ['swedish', 'danish', 'english']
    random.seed(1126)

    for lang in lang_train_list:
        whole_data = get_train_data_from_lang(lang)
        subdata = random.sample(whole_data, 200)
        tp = TransitionParser(Transition, FeatureExtractor)
        print '\n===== Start training {} data ====='.format(lang)
        tp.train(subdata)
        tp.save(lang+'.model')

    print '===== Sucessfully generating models ====='

if __name__ == '__main__':
    main()
