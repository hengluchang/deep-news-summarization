import numpy as np
import random
import codecs

def split_dataset(path):
    dataset = open(path).read().split('\n')

    dataset_len = len(dataset)
    print("There are %s headline-article pairs" % dataset_len)

    # Random shuffle data
    random.seed(11)
    dataset = np.array(random.sample(dataset, len(dataset)))

    # Split dataset to 70% training, 20% evaluation and 10% testing.
    train_size = int(dataset_len*0.7)
    eval_size = int(dataset_len*0.2)
    train, eval, test = dataset[0:train_size], dataset[train_size:train_size+eval_size], dataset[train_size+eval_size:]
    return train, eval, test


def write_dataset(dec_train, dec_eval, dec_test, enc_train, enc_eval, enc_test):

    # create and write training, evaluation, and testing encoding/decoding files.
    with open('./dataset/train_enc.txt', 'w') as train_enc:
        for line in enc_train:
            train_enc.write(line+'\n')
    train_enc.close()

    with open('./dataset/eval_enc.txt', 'w') as eval_enc:
        for line in enc_eval:
            eval_enc.write(line+'\n')
    eval_enc.close()

    with open('./dataset/test_enc.txt', 'w') as test_enc:
        for line in enc_test:
            test_enc.write(line+'\n')
    test_enc.close()

    with open('./dataset/train_dec.txt', 'w') as train_dec:
        for line in dec_train:
            train_dec.write(line + '\n')
    train_dec.close()

    with open('./dataset/eval_dec.txt', 'w') as eval_dec:
        for line in dec_eval:
            eval_dec.write(line + '\n')
    eval_dec.close()

    with open('./dataset/test_dec.txt', 'w') as test_dec:
        for line in dec_test:
            test_dec.write(line + '\n')
    test_dec.close()

def decode(sourceFileName, targetFileName):
    BLOCKSIZE = 1048576  # or some other, desired size in bytes
    with codecs.open(sourceFileName, "r", "latin-1") as sourceFile:
        with codecs.open(targetFileName, "w", "utf-8") as targetFile:
            while True:
                contents = sourceFile.read(BLOCKSIZE)
                if not contents:
                    break
                targetFile.write(contents)

def main():
    # encode using utf-8 if needed
    # decode('./dataset/10yapw/headline.txt', './dataset/10yapw/u_headline.txt')
    # decode('./dataset/10yapw/article.txt', './dataset/10yapw/u_article.txt')

    # specify headline/article path here
    headline_datapath = './dataset/headline.txt'
    article_datapath = './dataset/article.txt'
    dec_train, dec_eval, dec_test = split_dataset(headline_datapath)
    enc_train, enc_eval, enc_test = split_dataset(article_datapath)


    write_dataset(dec_train, dec_eval, dec_test, enc_train, enc_eval, enc_test)
    print("Finished splitting dataset!")

if __name__ == "__main__":
    main()
