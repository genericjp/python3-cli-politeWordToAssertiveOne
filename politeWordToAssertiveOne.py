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
    2018/10/24 22:00 (JST,UTC+9h)  v1.0.0 by ShozoNamikawa
     
"""

import os
import re

import pyperclip


class ClipBoard():
    """
        read the text content of the current clipboard, 
        or paste the new text contents and update the contents.
        [現在のクリップボードのテキスト内容を読む、ないし新たなテキスト内容を貼り付け内容を更新する。]
    """
    
    def get(self):
        """
            Contents of current clipboard.
            [現在クリップボードの内容を取得する。]
        """
        return (str(pyperclip.paste()))
    
    def set(self, past_text):
        """
            Rewrite the clipboard to this content.
            [この内容に、クリップボードを書き換える。]
        """
        pyperclip.copy(past_text)
        return (past_text)


class CnvTone():
    """
        convert tone.
        [語調変換を行う。]
    """
    
    def __init__(self):
        """
            define of conversion
            [語調変換の定義。]
        """
        
        # debug option
        self.debug = False
        
        # Dict for converting polite tone into assertive tone.
        # [丁寧語調を断定語調に変換するdict。]
        self.dct_cnv = {
                # Beware of enumeration of dictionaries
                # [辞書の列挙順には要注意]
                
                # case where the range is relatively limited
                '会います'             : '会う' ,           # 'あいます'
                'あたえます'           : '与える',          # 'あたえます'
                '与えます'             : '与える',          # 'あたえます'
                'あてます'             : '当てる',          # 'あてます'
                '当てます'             : '当てる',          # 'あてます'
                'あてられます'         : '当てられる',      # 'あてられます'
                '当てられます'         : '当てられる',      # 'あてられます'
                'あります'             : 'ある',            # 'あります'
                '言います'             : '言う',            # 'いいます'
                '行きます'             : '行く',            # 'いきます'
                '受け取ります'         : '受け取る',        # 'うけとりまする'
                'うけます'             : '受ける',          # 'うけます'
                '受けます'             : '受ける',          # 'うけます'
                '覚えておいてください' : '覚えておくこと',  # 'おぼえておいてください
                '思います'             : '思う',            # 'おもいます'
                '返します'             : '返す',            # 'かえす'
                '考えます'             : '考える',          # 'かんがえます'
                '聞きます'             : '聞く',            # 'ききます'
                'できます'             : '出来る',          # 'きます'
                '来ます '              : '来る',            # 'きます'
                '異なります'           : '異なる',          # 'ことなります'
                'されます'             : 'される',          # 'されます'
                '参照してください'     : '参照のこと',      # 'さんしょうしてください'
                'してください'         : 'すること',        # 'してください'
                '知っています'         : '知っている',      # 'しっています'
                '使用してください'     : '使用のこと',      # 'しようしてください'
                'することです'         : 'する',            # 'することです'
                '出してください'       : '出すこと',        # 'だしてください'
                'たちます'             : '立つ',            # 'たちます'
                '立ちます'             : '立つ',            # 'たちます'
                '食べます'             : '食べる',          # 'たべます'
                '注意してください'     : '注意のこと',      # 'ちゅういしてください'刷る
                '伝えます'             : '伝える',          # 'つたえます'
                '出来ます'             : '出来る' ,         # 'できます'
                'でした'               : 'であった',        # 'でした'
                'ですが'               : 'であるが',        # 'ですが、'
                '取ります'             : '取る',            # 'とります'
                'なります'             : 'なる',            # 'なります'
                '待ちます'             : '待つ',            # 'まちます'
                '学びます'             : '学ぶ',            # 'まなびます'
                '見ます'               : '見る',            # 'みます'
                '持ちます'             : '持つ',            # 'もつ'
                '呼びます'             : '呼ぶ',            # 'よびます'
                '読みます'             : '読む',            # 'よみます'
                '利用します'           : '利用する',        # 'りようします'
                '分かりません'         : '分からない',      # 'わかりません'
                '忘れないでください'   : '忘れないこと',    # 'わすれないでください'

                # Placing 'show', 'present', 'instruct', etc. before 'show'
                # ['示します'の前に'表示します'、'提示します'、'指示します'等を配置すること]
                '表示します'           : '表示する',        # '表示します'
                '提示します'           : '提示する',        # '提示します'
                '指示します'           : '指示する',        # '指示します'

                '示します'             : '示す',            # 'しめします'

                # case where range extends
                'あります'             : 'ある',            # 'あります'
                'います'               : 'いる',            # 'います'
                'します'               : 'する',            # 'します'
                'れます'               : 'れる',            # 'れます'
                'ます'                 : 'である',          # 'ます'
                'です'                 : 'です',            # 'です'
                }
    
        # used class
        self.clip_board = ClipBoard()
        
        # read clipping content of machine translation result at startup
        self.clip_str = self.clip_board.get()
        
    def cnvTone(self):
        """
            convert polite tone to assertive one
            [丁寧語（「です・ます」調）を断定語（「だ・である」調）に変換]
        """
        
        for k in self.dct_cnv:
            self.clip_str = self.clip_str.replace(k, self.dct_cnv[k])

            if self.debug:
                print(k + ' : ' + self.dct_cnv[k])
            
        # past result of the tone conversion to clip board
        self.clip_board.set(self.clip_str)
        
        return(True)


if __name__ == '__main__':

    cnv_tone = CnvTone()                                # convert tone
    if cnv_tone.cnvTone():
        exit(0)
    else:
        exit(1)