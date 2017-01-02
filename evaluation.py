import nltk
import re
import pandas as pd

_WORD_SPLIT = re.compile("([.,!?\"':;)(])")


def tokenizer(sentence):
    """Very basic tokenizer: split the sentence into a list of tokens."""
    words = []
    for space_separated_fragment in sentence.strip().split():
      words.extend(re.split(_WORD_SPLIT, space_separated_fragment))
    return [w for w in words if w]

def getBLEUscore(true_headline, predicted_headline):

    token_true_headline = []
    for sentence in true_headline:
        token_true_headline.append(tokenizer(sentence))

    token_predicted_headline = []
    for sentence in predicted_headline:
        token_predicted_headline.append(tokenizer(sentence))

    BLEUscore = []
    weights = [1, 0, 0, 0]  # param weights: weights for unigrams, bigrams, trigrams and so on
    total_predicted_headline = len(predicted_headline)
    count = 0
    for id in range(total_predicted_headline):
        BLEUscore.append(nltk.translate.bleu_score.sentence_bleu
                         ([token_true_headline[id]], token_predicted_headline[id], weights=weights))
        count += 1
        if count % 100 == 0:
            print ("Calculating BLEU for sentence %d" %count)

    avgBLEUscore = sum(BLEUscore)/total_predicted_headline
    return BLEUscore, avgBLEUscore


def main():

    desired_width = 600
    pd.set_option('display.width', desired_width)

    # specify sentence/true headline/predicted headline path.
    sentence_path = './dataset/test_enc.txt'
    true_headline_path = "./dataset/test_dec.txt"
    predicted_headline_path = "./output/predicted_test_headline.txt"

    # specify number of lines to read.
    number_of_lines_read = 400

    with open(true_headline_path) as ft:
        print("reading actual headlines...")
        true_headline = [next(ft).strip() for line in range(number_of_lines_read)]
    ft.close()

    with open(predicted_headline_path) as fp:
        print("reading predicted headlines...")
        predicted_headline = []
        for line in range(number_of_lines_read):
            predicted_headline.append(next(fp).strip())
    fp.close()
    # for debugging to detect empty predicted headlines (empty predicted headline will cause error while calculating BLEU)
    # print (predicted_headline[88380])
    # print (true_headline[88380])

    with open(sentence_path) as f:
        print("reading sentences...")
        sentence = [next(f).strip() for line in range(number_of_lines_read)]
    ft.close()

    # For testing purpose
    # true_headline = ["F1's Schumacher Slams Into Wall"]
    # predicted_headline = ["Schumacher Crashes in Practice"]
    BLEUscore, avgBLEUscore = getBLEUscore(true_headline, predicted_headline)
    print("average BLEU score: %f" % avgBLEUscore)

    summary = list(zip(BLEUscore, predicted_headline, true_headline, sentence))
    # pd.set_option("display.max_rows", 999)
    # pd.set_option('max_colwidth', 80)
    df = pd.DataFrame(data=summary, columns=['BLEU score', 'Predicted headline', 'True headline', 'article'])
    df_sortBLEU = df.sort_values('BLEU score', ascending=False)
    # print(df_sortBLEU)

    # Store the top 100 predicted headline in terms of BLEU score
    output_file = 'BLEU.txt'
    df_sortBLEU.head(100).to_csv(output_file, sep='\n', index=False,
                       line_terminator='\n-------------------------------------------------\n')
    print("Finished creating results summary in %s!" %output_file)

if __name__ == "__main__":
    main()
