import sentencepiece as spm

#spm.SentencePieceTrainer.train('--input=tweets_clean.txt --model_prefix=m_word --model_type=word --vocab_size=2000')

sp_word = spm.SentencePieceProcessor()
sp_word.load('Models/m_user.model')

token= sp_word.encode_as_pieces("This is a test<sep> hello word<cls>")
print(token)  # '.' will not be one token.
print(sp_word.encode_as_ids('este es un tweet de prueba #nel @tugfa '))
print(sp_word.decode_pieces(token))
"""
#<sep> and <cls>
spm.SentencePieceTrainer.train('--input=tweets_clean.txt --model_prefix=m_user --user_defined_symbols=<sep>,<cls> --vocab_size=2000')

sp_user = spm.SentencePieceProcessor()
sp_user.load('m_user.model')

print(sp_user.encode_as_pieces('this is a test<sep> hello world<cls>'))
print(sp_user.piece_to_id('<sep>'))  # 3
print(sp_user.piece_to_id('<cls>'))  # 4
print('3=', sp_user.decode_ids([3]))  # decoded to <sep>
print('4=', sp_user.decode_ids([4]))  # decoded to <cls>"""