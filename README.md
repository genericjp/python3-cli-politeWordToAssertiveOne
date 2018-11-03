# python3-cli-politeWordToAssertiveOne

# -*- coding:utf-8 -*-
# politeWordToAssertiveOne.py

"""
    Convert polite word to assertive one.
    [
　　　　丁寧語（「です・ます」調）を断定語（「だ・である」調）に変換する。
    ]

    1. motivation
        When machine translation from english resources in each field , 
        often translates into Japanese polite tone.
        Using polite translation as indirect Japanese notes, 
        then become redundant against readability.
        Case of manualy converting to assertive Japanese tone, 
        it is simple and intuitive tone and it will not get caught on the way.

        To consider the following when tone conversion is done all at once ...
            1) Target vocabulary of the tone conversion may amend and.spread.
            2) Do not suffer from differences in code due to OS dependent I / O.
            3) I would like to use any OS-independent wrappers.
    [
　　　　１．　動機

　　　　　　　英語による各分野のリソースを機械翻訳すると、日本語の丁寧語調に翻訳されるケースが多い。
　　　　　　　翻訳結果を間接的なメモとして使う場合、丁寧語調の記述のままでは可読性上で冗長となる
　　　　　　　断定語調に変換すると簡潔で直感的となり途中で引っかかることも無い。
　　　　　　　
　　　　　　　語調変換を一括して行う場合に、下記を考慮したい、・・・
　　　　　　　
　　　　　　　　　　１）　語調変換の対象語彙は修正または広がる可能性がある。
　　　　　　　　　　２）　OSに依存するI/Oによるコード上の相違点に悩されないこと。
　　　　　　　　　　３）　OSに依存しないラッパーがあれば使用したい。
    ]

    2. politeWordToAssertiveOne.py
       [丁寧語（「です・ます」調）を断定語（「だ・である」調）に変換する.py]

    3. Prerequisites for using
       [使う上での前提条件]

      1) python 3 If possible install v 3.6 or later
         However, considering when python 2 is already installed.
        [
        python3 出来れば　v3.6以降をインストール。
        但し、python2がインストール済みの場合の考慮すること。
        ]

          https://www python org/downloads/release/python-366/ is no problem

      2) Since clipboard operation is used, after installing python 3, 
         execute the following command to acquire external library.
        [
        クリップボード操作を使うのでpython3インストール後、
        外部ライブラリ取得のため、下記コマンドを行う。
        ]

          >pip install pyperclip

      4) How to use,

        (1) Perform the following procedure,...
            ①　Format the English original text as a single sentence.
            ②　Machine to translate.
            ③ Paste machine translation result to clipboard.
            ④ Execute the following command,...
                PoliteWordToAssertiveOne.py

            ⑤ The result of the tone conversion is pasted on the clipboard, 
              so use it.
            ⑥ Compare  with those before. 
              (Use diff etc.)the results of tone conversion
            ⑦ If the target vocabulary needs to be modified or added, 
              reflect in dict on the script and operate again.
        
        [
　　　　　　　使用方法は、
　　　　　　　　　　　　　　
　　　　　　　（１）　下記手順を行う。
　　　　　　　　　　　①　英文の原文を短文の行として整形する。
　　　　　　　　　　　②　機械翻訳する。
　　　　　　　　　　　③　機械翻訳結果をクリップボードに貼り付ける。
　　　　　　　　　　　④　以下のコマンドを実行する。
　　　　　　　　　　　　　　politeWordToAssertiveOne.py
　　　　　　　　　　　
　　　　　　　　　　　⑤　語調変換結果がクリップボード上に貼り付けられているので使用する。
　　　　　　　　　　　⑥　語調変換結果と変換前のものと比較レビューする。（diff等を使用する）。
　　　　　　　　　　　⑦　対象語彙はの修正または追加が必要な場合はスクリプト上のdictに反映し、再操作する。
        ]

History
    2018/11/03 20:00 (JST,UTC+9h)  v1.0.1 by ShozoNamikawa
        1) Tone conversion method by verb pattern classification was adopted.
        ...[動詞パターン分類によるトーン変換方式とした。]
    2018/10/24 22:00 (JST,UTC+9h)  v1.0.0 by ShozoNamikawa
     
"""
