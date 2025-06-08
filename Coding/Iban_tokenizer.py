import sentencepiece as spm

spm.SentencePieceTrainer.Train(
    input='iban_text_split_sentences.txt',
    model_prefix='iban_sp',
    vocab_size=356,
    model_type='bpe',
    bos_id=1,
    eos_id=2,
    unk_id=0,
    pad_id=3
)





