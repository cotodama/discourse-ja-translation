discourse-ja-translation
========================

discourseを頑張って日本語に翻訳する

もともと、

https://github.com/discourse/discourse/commit/3f049f4853c6162601bccb2c91244f3762bea6ca

で日本語化が行われていたのだが discourse自体が変わっていっており未翻訳箇所が出ている。
yamlのままだと未翻訳箇所がとてもわかりにくいので、一度CSVに変換した。

server.ja.csv と client.ja.csv のうち、***TO BE TRANSLATED*** となっている所を日本語に翻訳する。

それぞれ csv2yaml.pyスクリプトで server.ja.yml と client.ja.yml に変換し、

https://github.com/discourse/discourse/tree/master/config/locales

に上書き保存する。

