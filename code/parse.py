import sys
from providedcode.transitionparser import TransitionParser
from providedcode.dependencygraph import DependencyGraph

def main():
    file_to_parse = sys.stdin
    sentences_list = [s for s in file_to_parse]
    file_to_parse.close()

    lang_model = sys.argv[1]
    tp = TransitionParser.load(lang_model)

    sentences = [DependencyGraph.from_sentence(s) for s in sentences_list]
    parsed = tp.parse(sentences)
    for p in parsed:
        print p.to_conll(10).encode('utf-8')

if __name__ == '__main__':
    main()
