# 英語のファイルを選択 → 日本語に翻訳　→ テキスト化
from googletrans import Translator
import os

def main():
  english_file = input('翻訳したい英語ファイルのパスを入力して下さい>>')
  while True:
    if not os.path.isfile(english_file):
      english_file = input('ファイルが存在しません。再度入力して下さい>>')
    else:
      break
  translation(english_file)
  
def translation(file_path):
  with open(file_path) as f:
    lines = f.readlines()
    f.close()

  tr = Translator()
  try:
    for line in lines:
      # 1行ずつ日本語に翻訳
      result = tr.translate(line, src="en", dest="ja").text
      writing_translation(result)
    print('翻訳ファイルを作成しました。')
  except Exception as e:
    print(e)

# 1行づつ翻訳文を書き込む
def writing_translation(result):
  path = './ja.txt'
  f = open(path, 'a')#追加モード
  f.write(result + '\n')#改行
  f.close()

if __name__ == "__main__":
  main()