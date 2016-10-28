import random
from providedcode import dataset
from providedcode.transitionparser import TransitionParser
from featureextractor import FeatureExtractor
from transition import Transition


def main():
    swedish_data = dataset.get_swedish_train_corpus().parsed_sents()
    danish_data = dataset.get_danish_train_corpus().parsed_sents()
    english_data = dataset.get_english_train_corpus().parsed_sents()

    random.seed(1234)
    swedish_subdata = random.sample(swedish_data, 200)
    danish_subdata = random.sample(danish_data, 200)
    english_subdata = random.sample(english_data, 200)

    tp_swedish = tp_danish = tp_english = TransitionParser(Transition, FeatureExtractor)

    print '\n===== Start training Swedish Data ====='
    tp_swedish.train(swedish_subdata)
    tp_swedish.save('swedish.model')

    print '\n===== Start training Danish Data ====='
    tp_danish.train(danish_subdata)
    tp_danish.save('danish.model')

    print '\n===== Start training English Data ====='
    tp_english.train(english_subdata)
    tp_english.save('english.model')

    print '===== Sucessfully generating models ====='

if __name__ == '__main__':
    main()
