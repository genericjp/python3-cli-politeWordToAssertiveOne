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
    2018/11/10 03:10 (JST,UTC+9h)  v1.0.2 by ShozoNamikawa
        1)  convert a pattern following a specific letter into an assertion word
        ... [特定の一字に続くパターンを断定語に変換する]
    2018/11/03 20:00 (JST,UTC+9h)  v1.0.1 by ShozoNamikawa
        1) Tone conversion method by verb pattern classification was adopted.
        ...[動詞パターン分類によるトーン変換方式とした。]
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
        self.debug = True
        
        # dict for converting polite tone into assertive one
        # [丁寧語調を断定語調に変換するdict]
        self.dct_cnv = {
            # Beware of enumeration of dictionaries
            # [辞書の列挙順には要注意]
            
            # Note. automatically generated inside the script
            # [注.　スクリプト内部において自動的に生成する]
            }
        
        self.dct_cnv2 = {
            # convert a pattern following a specific letter into an assertion word
            # [特定の一字に続くパターンを断定語に変換する]
            
            # Note. automatically generated inside the script
            # [注.　スクリプト内部において自動的に生成する]
            }
        
        # forcibly change such as non-polite words (e.g.　more and more)
        # [丁寧語でない益々（ますます）などを強制的に置き換える]
        self.dct_fchg = {
                
                # more and more
                'ますます'           : '益々',
                
                # please
                'ください'           : '下さい',
                
                # 述語 + ...
                # 　→　...のこと
                
                # 
                '見て下さい'         : '見ること',
                '注意して下さい'     : '注意のこと',
                '使かってく下さい'   : '使用のこと',
                '続けて下さい'       : '続けること',
                '覚えておいて下さい' : '覚えておくこと',
                'お知らせ下さい'     : '知らせること',
                '出して下さい'       : '出すこと',
                '忘れないで下さい'   : '忘れないこと',
                '戻して下さい'       : '戻すこと',
                'ご覧下さい'         : '参照のこと',
                '頼んで下さい'       : '頼むこと',
                'しないで下さい'     : 'しないこと',
                'てみて下さい'       : 'てみること',
                'と考えて下さい'     : 'と考えること',
                '手を挙げて下さい'   : '手を挙げること',
                
                
                # 熟語 + ...
                # 余裕
                '余裕ございます'     : '余裕あり',
                '余裕がございます'   : '余裕あり',
                
                # 'いい'、'良い'、及び好い'
                # 
                'いいです'           : 'いいです',
                '良いです'           : '良い',
                '好いです'           : '好い',
                
                # ある
                'ありませんでした'   : 'なかった',
                'あるということです' : 'あるということだ',
                'ということです'     : 'ということだ',
                
                # する
                'することです'       : 'することだ',
                'することができました': 'することができた',
                'するだけではありません': 'するだけではない',
                
                # した
                'してやりました'     : 'した',
                'しておきます'       : 'しておく',
                'いけません'         : 'いけない',
                
                # です
                'していませんでした' : 'していなかった',
                'しませんでした'     : 'しなっかった',
                'させませんでした'   : 'させなかった',
                'せねばならない'     : 'しなければならない',
                'ならないです'       : 'ならない',
                'ないです'           : 'ない',# 役に立たないです
                'すでに'             : '既に', # ですでに　→　で既に　としてブロックする
                'ものですが'         : 'ものだが',
                'のとおりです'       : 'のとおり',
                'の通りです'         : 'の通り',
                
                # miscellaneous
                '使用できます'       : '使用できる',
                'ご使用いただけます' : '使用できる',
                '与えないで下さい'   : '与えないこと',
                'お読み下さい'       : '読むこと',
                '調べて下さい'       : '調べること',
                '学んで下さい'       : '学ぶこと',
                'お願いいたします'   : '願う',
                'お待ちしております' : '待っている',
                'どうなるでしょうか' : 'どうなるか',
                '抜いていきます'     : '抜いていく',
                'からです'           : 'からだ',
                'じですが'           : 'じだが',
                '食べてもらいます'   : '食べること',
                'おいしいです'       : 'おいしい',
                'おいしかったです'   : 'おいしかった',
                'おいしくないです'   : 'おいしくない',
                'しいです'           : 'しい',
                'するでしょう'       : 'するだろう',
                'しないでしょう'     : 'しないだろう',
                'うれしいでしょう'   : 'いいことだろう',
                'そうでした'         : 'そうだった',
                'ないでしょう'       : 'ない',
                'でしょうか'         : 'か',
                'もらえます'         : 'もらえる',
                'しれません'         : 'しれない',
                'はまりません'       : 'はまらない',
                'すぎません'         : 'すぎない',
                '何ですか'           : '何か',
                'なりますか'         : 'なるか',
                'よりますと'         : 'よると',
                
                # 
                'されてきました'     : 'されてきた',
                'わかってきました'   : 'わかってきた',
                
                }
        
        # register the stem list, word variation, and change pattern
        # [語幹リスト、語変、及び変化パターンを登録する]
        self.dct_wgrp1 = {
                
                # 熟語 + ...
                
                '頑張る'  :   {'語幹': ['がんば', '頑張'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},
                '出来る'  :   {'語幹': ['でき', '出来'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                
                '参照する':   {'語幹': ['参照'], '語変': 'し', '変化': '変化-する,のこと,した,しx,しx,すること'},
                '指示する':   {'語幹': ['指示'], '語変': 'し', '変化': '変化-する,のこと,した,しx,しx,すること'},
                '使用する':   {'語幹': ['使用'], '語変': 'し', '変化': '変化-する,のこと,した,しx,しx,すること'},
                '注意する':   {'語幹': ['注意'], '語変': 'し', '変化': '変化-する,のこと,した,しx,しx,すること'},
                '提示する':   {'語幹': ['提示'], '語変': 'し', '変化': '変化-する,のこと,した,しx,しx,すること'},
                '表示する':   {'語幹': ['表示'], '語変': 'し', '変化': '変化-する,のこと,した,しx,しx,すること'},
                '利用する':   {'語幹': ['利用'], '語変': 'し', '変化': '変化-する,のこと,した,しx,しx,すること'},
                '表現する':   {'語幹': ['表現'], '語変': 'し', '変化': '変化-する,のこと,した,しx,しx,すること'},
                '定義する':   {'語幹': ['定義'], '語変': 'し', '変化': '変化-する,のこと,した,しx,しx,すること'},
                '確認する':   {'語幹': ['確認'], '語変': 'し', '変化': '変化-する,のこと,した,しx,しx,すること'},
                '用意する':   {'語幹': ['用意'], '語変': 'し', '変化': '変化-する,のこと,した,しx,しx,すること'},
                '実行する':   {'語幹': ['実行'], '語変': 'し', '変化': '変化-する,のこと,した,しx,しx,すること'},
                '設定する':   {'語幹': ['設定'], '語変': 'し', '変化': '変化-する,のこと,した,しx,しx,すること'},
                '更新する':   {'語幹': ['更新'], '語変': 'し', '変化': '変化-する,のこと,した,しx,しx,すること'},
                '変更する':   {'語幹': ['変更'], '語変': 'し', '変化': '変化-する,のこと,した,しx,しx,すること'},
                '開始する':   {'語幹': ['開始'], '語変': 'し', '変化': '変化-する,のこと,した,しx,しx,すること'},
                '中断する':   {'語幹': ['中断'], '語変': 'し', '変化': '変化-する,のこと,した,しx,しx,すること'},
                '終了する':   {'語幹': ['終了'], '語変': 'し', '変化': '変化-する,のこと,した,しx,しx,すること'},
                
                '失望する':   {'語幹': ['失望'], '語変': 'し', '変化': '変化-する,のこと,した,しx,しx,すること'},
                '失望させる': {'語幹': ['失望させ'], '語変': '', '変化': '変化-る,よう,た,x,x'},
                
                # 単字 + ...
                
                'しめす':     {'語幹': ['しめ', '示'], '語変': 'し', '変化': '変化-す,そう,した,さx,さx'},
                
                'てみ':       {'語幹': ['てみ', 'でみ'], '語変': '', '変化': '変化-る,よう,た,x,x'}, # e.g. 考えてみる
                
                'あう':       {'語幹': ['あ', '会', '合', '逢', '遭'], '語変': 'い', '変化': '変化-う,うだろう,った,わx,わx'},
                'あたえる':   {'語幹': ['あたえ', '与え'], '語変': '', '変化': '変化-る,よう,た,x,x'},
                'あげる':     {'語幹': ['あげ', '上げ', '揚げ', '挙げ'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'あつかう':   {'語幹': ['あつか', '扱'], '語変': 'い', '変化': '変化-う,うだろう,った,わx,わx'},
                'あつかわれる': {'語幹': ['あつかわれ', '扱われ'], '語変': '', '変化': '変化-る,よう,た,x,x'},
                'あてる':     {'語幹': ['あて', '当て', '充て'], '語変': '', '変化': '変化-る,よう,た,x,x'},
                'あてはまる': {'語幹': ['あてはま', '当てはま'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},
                'あてられる': {'語幹': ['あてられ', '当てられ', '充てられ'], '語変': '', '変化': '変化-る,よう,た,x,x'},
                'あらわす':   {'語幹': ['あらわ', '表', '表わ'], '語変': 'し', '変化': '変化-す,そう,した,さx,さx'},
                'あわせる':     {'語幹': ['あわせ', '合わせ', '会わせ', '併せ', '逢わせ', '遭わせ', '併せ', '合せ'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                
                'いう':       {'語幹': ['い', '言'], '語変': 'い', '変化': '変化-う,うだろう,った,わx,わx'},
                'いく':       {'語幹': ['い', '行'], '語変': 'き', '変化': '変化-く,こう,った,かx,かx'},
                'いたす':     {'語幹': ['いた', '致'], '語変': 'し', '変化': '変化-す,そう,した,さx,さx'},
                'いただく':   {'語幹': ['いただ', '頂'], '語変': 'き', '変化': '変化-く,こう,いた,かx,かx'},
                
                'いっちする': {'語幹': ['致'], '語変': 'し', '変化': '変化-する,するだろう,した,しx,しx'}, # bug 一致の一が認識されない
                'うかぶ':     {'語幹': ['うか', '浮', '浮か'], '語変': 'び', '変化': '変化-ぶ,ぼう,んだ,ばx,ばx'},
                'うける':     {'語幹': ['うけ', '受け'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'うけいれる': {'語幹': ['うけいれ', '受け入れ'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'うごかす':   {'語幹': ['うごか', '動か'], '語変': 'し', '変化': '変化-す,そう,した,さx,さx'},
                'うごく':     {'語幹': ['うご', '動'], '語変': 'き', '変化': '変化-く,こう,いた,かx,かx'},
                'うしなう':   {'語幹': ['うし', '失'], '語変': 'い', '変化': '変化-う,うだろう,った,わx,わx'},
                'うみだす':   {'語幹': ['うみだ', '生み出'], '語変': 'し', '変化': '変化-す,そう,した,さx,さx'},
                'える':       {'語幹': ['え', '得'], '語変': '', '変化': '変化-る,よう,た,x,x'},
                'おこなう':   {'語幹': ['おこ', '行'], '語変': 'い', '変化': '変化-う,うだろう,った,わx,わx'},
                'おこなわれる':{'語幹': ['おこなわれ', '行われ'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'おきる':     {'語幹': ['お', '起'], '語変': 'き', '変化': '変化-る,るだろう,た,x,x'},
                'おきかえらる':{'語幹': ['起かえられ'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'おきかえらる':{'語幹': ['置き換えられ'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'おく':       {'語幹': ['お', '置'], '語変': 'き', '変化': '変化-く,こう,いた,かx,かx'},
                'おくる':     {'語幹': ['おく', '送'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},
                'おこす':     {'語幹': ['おこ', '起こ'], '語変': 'し', '変化': '変化-す,すだろう,した,さx,さx'},
                'おこる':     {'語幹': ['おこ', '起こ'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},
                'おすすめする':{'語幹': ['おすすめ', 'お勧め'], '語変': 'し', '変化': '変化-する,する,した,しx,しx'},
                'おす':       {'語幹': ['お', '押'], '語変': 'し', '変化': '変化-す,すだろう,した,さx,さx,すこと'},
                'おそう':     {'語幹': ['おそ', '襲'], '語変': 'い', '変化': '変化-う,うだろう,った,わx,わx'},
                'おちいる':   {'語幹': ['おちい', '陥'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},
                'おちる':     {'語幹': ['おち', '落ち', '墜ち', '陥ち'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'おもう':     {'語幹': ['おも', '思'], '語変': 'い', '変化': '変化-う,うだろう,った,わx,わx'},
                'おもわれる': {'語幹': ['おもわれ', '思われ', '想われ'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'およぼす':   {'語幹': ['およぼ', '及ぼ'], '語変': 'し', '変化': '変化-す,そう,した,さx,さx'},
                'おわる':     {'語幹': ['おわ', '終わ'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},

                'がいる':     {'語幹': ['がい'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                
                'かえす':     {'語幹': ['かえ', '返'], '語変': 'し', '変化': '変化-す,そう,した,さx,さx'},
                'かかる':     {'語幹': ['かか', '掛か', '懸か', '係'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},
                'かがやく':   {'語幹': ['かがや', '輝'], '語変': 'き', '変化': '変化-く,こう,いた,かx,かx'},
                'かく':       {'語幹': ['か', '書'], '語変': 'き', '変化': '変化-く,こう,いた,かx,かx'},
                'かきこむ':   {'語幹': ['書き込'], '語変': 'み', '変化': '変化-む,もう,んだ,まなかった,まない'},
                'かきこまれる':{'語幹': ['書き込まれ'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'かぎる':     {'語幹': ['かぎ', '限'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},
                'かこむ':     {'語幹': ['かこ', '囲'], '語変': 'み', '変化': '変化-む,もう,んだ,まなかった,まない'},
                'かたむく':   {'語幹': ['傾'], '語変': 'き', '変化': '変化-く,こう,いた,かx,かx'},
                'かる':       {'語幹': ['か', '刈'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},
                'かえる':     {'語幹': ['かえ', '変え', '換え', '代え', '替え'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'かまう':     {'語幹': ['かま', '構'], '語変': 'い', '変化': '変化-う,うだろう,った,わx,わx'},
                'かわる':     {'語幹': ['かわ', '変わ', '換わ', '代わ', '替わ'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},
                'かんがえる': {'語幹': ['かんがえ', '考え'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'かんじる':   {'語幹': ['かんじ', '感じ'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'きく':       {'語幹': ['き', '聞'], '語変': 'き', '変化': '変化-く,こう,いた,かx,かx'},
                'きめる':     {'語幹': ['きめ', '決め'], '語変': '', '変化': '変化-る,よう,た,x,x'},
                'きまる':     {'語幹': ['きま', '決ま'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},
                'きる':       {'語幹': ['切'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},
                'くわわる':   {'語幹': ['くわわ', '加わ'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},
                'こころみる': {'語幹': ['こころみ', '試み'], '語変': '', '変化': '変化-る,よう,た,x,x'},
                'ことなる':   {'語幹': ['ことな', '異な'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},
                'こまる':     {'語幹': ['こま', '困'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},
                'さがす':     {'語幹': ['さが', '探', '捜'], '語変': 'し', '変化': '変化-す,そう,した,さx,さx'},
                'しらべる':   {'語幹': ['しらべ', '調べ'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'したがう':   {'語幹': ['したが', '従', '随'], '語変': 'い', '変化': '変化-う,うだろう,った,わx,わx'},
                'しっている': {'語幹': ['知ってい'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'しる':       {'語幹': ['し', '知'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},
                'すぎる':     {'語幹': ['すぎ', '過ぎ'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'たかめる':   {'語幹': ['たかめ', '高め'], '語変': '', '変化': '変化-る,よう,た,x,x'},
                'だす':       {'語幹': ['だ', '出'], '語変': 'し', '変化':  '変化-す,そう,した,さx,さx'},
                'たすける':   {'語幹': ['たすけ', '助け'], '語変': '', '変化':  '変化-る,るだろう,た,x,x'},
                'たつ':       {'語幹': ['た', '立'], '語変': 'ち', '変化': '変化-つ,とう,った,たx,たx'},
                'たのむ':     {'語幹': ['たの', '頼'], '語変': 'み', '変化': '変化-む,もう,んだ,まなかった,まない'},
                'たのしむ':   {'語幹': ['たのし', '楽し'], '語変': 'み', '変化': '変化-む,もう,んだ,まなかった,まない'},
                'たべる':     {'語幹': ['たべ', '食べ'], '語変': '', '変化': '変化-る,よう,た,x,x'},
                'ついやす':   {'語幹': ['ついや', '費や'], '語変': 'し', '変化': '変化-す,すだろう,した,さx,さx'},
                'つかう':     {'語幹': ['つか', '使'], '語変': 'い', '変化': '変化-う,うだろう,った,わx,わx'},
                'つかえる':   {'語幹': ['つかえ', '使え'], '語変': '', '変化': '変化-る,よう,た,x,x'},
                'つかわれる': {'語幹': ['つかわれ', '使われ'], '語変': '', '変化': '変化-る,よう,た,x,x'},
                'つく':       {'語幹': ['つ'], '語変': 'き', '変化': '変化-く,こう,いた,かx,かx'},
                'つくりだす': {'語幹': ['つくりだ', '作り出'], '語変': 'し', '変化': '変化-す,そう,した,さx,さx'},
                'つくる':     {'語幹': ['つく', '作'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},
                'つくれる':   {'語幹': ['つくれ', '作れ'], '語変': '', '変化': '変化-る,よう,た,x,x'},
                'つける':     {'語幹': ['つけ', '付け'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'つたえる':   {'語幹': ['つたえ', '伝え'], '語変': '', '変化': '変化-る,よう,た,x,x'},
                'つづく':     {'語幹': ['つづ', '続'], '語変': 'き', '変化': '変化-く,こう,いた,かx,かx'},
                'つづける':   {'語幹': ['つづけ', '続け'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'つなぐ':     {'語幹': ['つな', '繋'], '語変': 'ぎ', '変化': '変化-ぐ,ごう,がった,がx,がx'},
                'つながる':   {'語幹': ['つなが', '繋が'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},
                'つぶやく':   {'語幹': ['つぶや', '呟'], '語変': 'き', '変化': '変化-く,こう,いた,かx,かx'},
                'どうきづける':{'語幹': ['どうきづけ', '動機づけ'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'ととのう':   {'語幹': ['ととの', '整'], '語変': 'い', '変化': '変化-う,うだろう,った,わx,わx'},
                'とどまる':   {'語幹': ['とどま', '留ま', '止ま'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},
                'とまる':     {'語幹': ['とま', '泊ま', '止ま', '停ま', '泊', '止', '停'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},
                'とりあげる': {'語幹': ['とりあげ', '取あげ'], '語変': '', '変化': '変化-る,よう,た,x,x'},
                'とりこまれる':{'語幹': ['とりこまれ', '取り込まれ'], '語変': '', '変化': '変化-る,よう,た,x,x'},
                'とる':       {'語幹': ['と', '取'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},
                'とめる':     {'語幹': ['とめ', '止め'], '語変': '', '変化': '変化-る,よう,た,x,x'},
                'のぞむ':     {'語幹': ['のぞ', '望'], '語変': 'み', '変化': '変化-む,もう,んだ,まなかった,まない'},
                'ぬく':       {'語幹': ['ぬ', '抜'], '語変': 'き', '変化': '変化-く,こう,いた,かx,かx'},
                'ぬける':     {'語幹': ['ぬけ', '抜け'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'ねがう':     {'語幹': ['ねが', '願'], '語変': 'い', '変化': '変化-う,うだろう,った,わx,わx'},
                'のこる':     {'語幹': ['のこ', '残'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},
                'はいる':     {'語幹': ['はい', '入'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},
                'はかる':     {'語幹': ['はか', '計', '図', '測', '量', '諮', '謀'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},
                'はじまる':   {'語幹': ['はじま', '始ま'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},
                'はじめる':   {'語幹': ['はじめ', '始め'], '語変': '', '変化': '変化-る,よう,た,x,x'},
                'はじめられる':{'語幹': ['はじめられ', '始められ'], '語変': '', '変化': '変化-る,よう,た,x,x'},
                'はたす':     {'語幹': ['はた', '果た', '果'], '語変': 'し', '変化': '変化-す,すだろう,した,さx,さx'},
                'はたらく':   {'語幹': ['はたらく', '働'], '語変': 'き', '変化': '変化-く,こう,いた,かx,かx'},
                'はたらかせる':{'語幹': ['はたらかせ', '働かせ'], '語変': '', '変化': '変化-る,よう,た,x,x'},
                'はなれる':   {'語幹': ['はなれ', '離れ', '放れ'], '語変': '', '変化': '変化-る,よう,た,x,x'},
                'はぶける':   {'語幹': ['はぶけ', '省け'], '語変': '', '変化': '変化-る,よう,た,x,x'},
                'ひろがる':   {'語幹': ['ひろが', '広が'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},
                'ひろげる':   {'語幹': ['ひろげ', '広げ'], '語変': '', '変化': '変化-る,るだろう,った,らx,らx'},
                'ふくまれる': {'語幹': ['ふくまれ', '含まれ'], '語変': '', '変化': '変化-る,よう,た,x,x'},
                'ふくめられる':{'語幹': ['ふくめられ', '含められ'], '語変': '', '変化': '変化-る,よう,た,x,x'},
                'ふくむ':     {'語幹': ['ふく', '含'], '語変': 'み', '変化': '変化-む,もう,んだ,まなかった,まない'},
                'ふれる':     {'語幹': ['ふれ', '触れ', '振れ'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'ひらく':     {'語幹': ['ひら', '開'], '語変': 'き', '変化': '変化-く,こう,いた,かx,かx'},
                'ながれる':   {'語幹': ['ながれ', '流れ'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'なげる':     {'語幹': ['なげ', '投げ'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'のこす':     {'語幹': ['のこ', '残'], '語変': 'し', '変化': '変化-す,すだろう,した,さx,さx,すこと'},
                'のぞまれる': {'語幹': ['のぞまれ', '望まれ', '臨まれ'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'まつ':       {'語幹': ['ま', '待'], '語変': 'ち', '変化': '変化-つ,とう,った,たx,たx'},
                'まなぶ':     {'語幹': ['まな', '学'], '語変': 'び', '変化': '変化-ぶ,ぼう,んだ,ばx,ばx'},
                'まもる':     {'語幹': ['まも', '守', '護'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},
                'みる':       {'語幹': ['見'], '語変': '', '変化': '変化-る,よう,た,x,x'},      # del 'み', 
                'みえる':     {'語幹': ['みえ', '見え'], '語変': '', '変化': '変化-る,よう,た,x,x'},
                'ひらく':     {'語幹': ['ひら', '開'], '語変': 'き', '変化': '変化-く,こう,いた,かx,かx'},
                'みたす':     {'語幹': ['みた', '満た', '充た'], '語変': 'し', '変化': '変化-す,すだろう,した,さx,さx'},
                'みちびく':   {'語幹': ['みちび', '導'], '語変': 'き', '変化': '変化-く,こう,いた,かx,かx'},
                'みつかる':   {'語幹': ['みつか', '見つか'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},
                'みつける':   {'語幹': ['みつけ', '見つけ'], '語変': '', '変化': '変化-る,よう,た,x,x'},
                'みてみる':   {'語幹': ['みてみ', '見てみ'], '語変': '', '変化': '変化-る,よう,た,x,x'},
                'むかう':     {'語幹': ['むか', '向か'], '語変': 'い', '変化': '変化-う,うだろう,った,わx,わx'},
                'もうしあげる':{'語幹': ['もうしあげ', '申し上げ'], '語変': '', '変化': '変化-る,よう,た,x,x'},
                'もうしこみ': {'語幹': ['もうしこ', '申込', '申し込'], '語変': 'み', '変化': '変化-む,もう,んだ,まなかった,まない'},
                'もつ':       {'語幹': ['も', '持'], '語変': 'ち', '変化': '変化-つ,とう,った,たx,たx'},
                'もてる':     {'語幹': ['もて', '持て'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'もっている': {'語幹': ['もってい', '持ってい'], '語変': '', '変化': '変化-る,よう,た,x,x'},
                'もどる':     {'語幹': ['もど', '戻'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},
                'よむ':       {'語幹': ['よ', '読'], '語変': 'み', '変化': '変化-む,もう,んだ,まなかった,まない'},
                'よみこむ':   {'語幹': ['読み込'], '語変': 'み', '変化': '変化-む,もう,んだ,まなかった,まない'},
                'よみこまれる':{'語幹': ['読み込まれ'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'よぶ':       {'語幹': ['よ', '呼'], '語変': 'び', '変化': '変化-ぶ,ぼう,んだ,ばx,ばx'},
                'もらう':     {'語幹': ['もら', '貰'], '語変': 'い', '変化': '変化-う,うだろう,った,わx,わx'},
                'もらえる':   {'語幹': ['もらえ', '貰え'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'やめる':     {'語幹': ['やめ', '病め', '止め', '辞め'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'やる':       {'語幹': ['や', '遣'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},
                'よわまる':   {'語幹': ['よわま', '弱ま'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},
                'よむ':       {'語幹': ['よ', '読'], '語変': 'み', '変化': '変化-む,もう,んだ,まなかった,まない'},
                'わかる':     {'語幹': ['わか', '分か'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},
                'わすれる':   {'語幹': ['わすれ', '忘れ'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                
                'されている': {'語幹': ['されてい'], '語変': '', '変化': '変化-る,よう,た,x,x'},
                'される':     {'語幹': ['され'], '語変': '', '変化': '変化-る,よう,た,x,x'},
                
                'していく':   {'語幹': ['してい'], '語変': 'き', '変化': '変化-く,こう,った,かx,かx'},
                'してくる':   {'語幹': ['して'], '語変': 'き', '変化': '変化-くる,こよう,きた,こx,こx'},
                'ってくる':   {'語幹': ['って'], '語変': 'き', '変化': '変化-くる,こよう,きた,こx,こx'},
                'している':   {'語幹': ['してい'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                
                
                'かれる':     {'語幹': ['かれ'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'れている':   {'語幹': ['れてい'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'ている':     {'語幹': ['てい'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'でいる':     {'語幹': ['でい'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'ばれる':     {'語幹': ['ばれ'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'とれる':     {'語幹': ['とれ'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'られる':     {'語幹': ['られ'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},
                'まれる':     {'語幹': ['まれ'], '語変': '', '変化': '変化-る,るだろう,た,x,x'}, # e.g. 囲まれる
                
                'なる':       {'語幹': ['な'], '語変': 'り', '変化': '変化-る,るだろう,った,らx,らx'},
                'いる':       {'語幹': ['い', '居', '入', '要', '射', '鋳', '炒', '煎'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},

                '有る':       {'語幹': ['有'], '語変': 'り', '変化': '変化-有る,有るだろう,有った,無かった,無い', '変語幹':'有'},
                'ある':       {'語幹': ['あ'], '語変': 'り', '変化': '変化-ある,あるだろう,あった,なかった,ない', '変語幹': '有'},

                '来る':       {'語幹': ['来'], '語変': '', '変化': '変化-来る,来よう,来た,来なかった,来ない', '変語幹':'有'},
                'くる':       {'語幹': ['き'], '語変': '', '変化': '変化-くる,こよう,きた,こなかった,こない', '変語幹':'有'}, # e.g. 見てきた

                'があります': {'語幹': ['が'], '語変': 'あり', '変化': '変化-ある,あるだろう,あった,なかった,ない'},
                # 'いる':       {'語幹': ['い', '居'], '語変': '', '変化': '変化-る,よう,た,x,x'},
                'する':       {'語幹': [''], '語変': 'し', '変化': '変化-する,しよう,した,しなかった,しない', '変語幹':'有'},
                
                # 
                'でる':       {'語幹': ['で', '出'], '語変': '', '変化': '変化-る,るだろう,た,x,x'},

                }
                
        # register the leaked polite tone that should be interpreted at the very end
        # [一番最後になって解釈すべき漏れた敬語表現を登録する]
        self.dct_tail = {
                
                # して
                'して下さい'         : 'すること',
                'させます'           : 'させる',
                
                # です
                'ですから'           : 'だから',
                'ですが'             : 'だが',
                'ですか'             : 'であろうか',
                'ですべて'           : 'で全て',  # です　のやりすぎを回避
                'ですね'             : 'ね',
                'です'               : 'だ',
                'でしょうか'         : 'であろうか',
                'でしょう'           : 'であろう',
                'でした'             : 'だった',
                
                # 
                '恐縮だ'             : '恐縮です',
                # 
                }
        
        # register the stem list, word variation, and change pattern
        # [語幹リスト、語変、及び変化パターンを登録する]
        self.dct_wgrp2 = {
                # 例：　踏みます : 踏む
                'みる':       {'語幹': [''], '語変': 'み', '変化': '変化-る,よう,た,x,x',
                     '漢字' : {'語幹': [''], '語変': 'み', '変化': '変化-む,もう,んだ,まなかった,まない'}
                             },
                }
                
        # correspond to polite endings, register the assertive endings
        # [丁寧語尾に対応し、断定語尾を登録する]
        self.dct_wchg = {
                
                # 
                '変化-う,うだろう,った,わx,わx':
                        {'ます': 'う',  'ましょう': 'うだろう', 'ました': 'った', 'ませんでした': 'わなかった', 'ません': 'わない'},
                
                # 
                '変化-く,こう,いた,かx,かx': 
                        {'ます': 'く',  'ましょう': 'こう', 'ました': 'いた', 'ませんでした': 'かなかった', 'ません': 'かない'},
                '変化-く,こう,った,かx,かx': 
                        {'ます': 'く',  'ましょう': 'こう', 'ました': 'った', 'ませんでした': 'かなかった', 'ません': 'かない'},
                
                # 
                '変化-くる,こよう,きた,こx,こx': 
                        {'ます': 'くる','ましょう': 'こよう', 'ました': 'きた', 'ませんでした': 'こなかった', 'ません': 'こない'},
                
                # 
                '変化-す,そう,した,さx,さx':  
                        {'ます': 'す',  'ましょう': 'そう', 'ました': 'した', 'ませんでした': 'さなかった', 'ません': 'さない'},
                '変化-す,すだろう,した,さx,さx':
                        {'ます': 'す',  'ましょう': 'すだろう', 'ました': 'した', 'ませんでした': 'さなかった', 'ません': 'さない'},
                '変化-す,すだろう,した,さx,さx,すこと':
                        {'ます': 'す',  'ましょう': 'すだろう', 'ました': 'した', 'ませんでした': 'さなかった', 'ません': 'さない', 'て下さい': 'すこと'},
                
                # 
                '変化-する,のこと,した,しx,しx,すること': 
                        {'ます': 'する', 'ましょう': 'のこと', 'ました': 'した', 'ませんでした': 'しなかった', 'ません': 'しない', 'て下さい': 'すること'},
                '変化-する,する,した,しx,しx': 
                        {'ます': 'する', 'ましょう': 'する' , 'ました': 'した', 'ませんでした': 'しなかった', 'ません': 'しない'},
                '変化-する,するだろう,した,しx,しx': 
                        {'ます': 'する', 'ましょう': 'するだろう' , 'ました': 'した', 'ませんでした': 'しなかった', 'ません': 'しない'},
                
                # 
                '変化-る,よう,た,x,x':  
                        {'ます': 'る',  'ましょう': 'よう',    'ました': 'た',  'ませんでした': 'なかった',  'ません': 'ない'},
                '変化-る,るだろう,た,x,x': 
                        {'ます': 'る',  'ましょう': 'るだろう', 'ました': 'た',  'ませんでした': 'なかった',  'ません': 'ない'},
                '変化-る,るだろう,った,らx,らx': 
                        {'ます': 'る',  'ましょう': 'るだろう', 'ました': 'った', 'ませんでした': 'らなかった', 'ません': 'らない'},
                
                #
                '変化-つ,とう,った,たx,たx': 
                        {'ます': 'つ',  'ましょう': 'とう', 'ました': 'った',  'ませんでした': 'たなかった', 'ません': 'たない'},
                '変化-ぐ,ごう,がった,がx,がx': 
                        {'ます': 'ぐ',  'ましょう': 'ごう', 'ました': 'がった', 'ませんでした': 'がらなかった', 'ません': 'がらない'},
                '変化-ぶ,ぼう,んだ,ばx,ばx': 
                        {'ます': 'ぶ',  'ましょう': 'ぼう', 'ました': 'んだ', 'ませんでした': 'ばなかった', 'ません': 'ばない'},
                '変化-む,もう,んだ,まなかった,まない': 
                        {'ます': 'む',  'ましょう': 'もう', 'ました': 'んだ', 'ませんでした': 'まなかった', 'ません': 'まない'},
                
                # 
                '変化-くる,こよう,きた,こなかった,こない':
                        {'ます': 'くる',  'ましょう': 'こよう',    'ました': 'きた',  'ませんでした': 'こなかった',  'ません': 'こない'},
                '変化-来る,来よう,来た,来なかった,来ない':
                        {'ます': '来る',  'ましょう': '来よう',    'ました': '来た',  'ませんでした': '来なかった',  'ません': '来ない'},
                '変化-する,しよう,した,しなかった,しない':
                        {'ます': 'する', 'ましょう': 'しよう', 'ました': 'した', 'ませんでした': 'しなかった', 'ません': 'しない'},
                
                #
                '変化-ある,あるだろう,あった,なかった,ない':
                        {'ます': 'ある',  'ましょう': 'あるだろう',    'ました': 'あった',  'ませんでした': 'なかった',  'ません': 'ない'},
                '変化-有る,有るだろう,有った,無かった,無い':
                        {'ます': '有る',  'ましょう': '有るだろう',    'ました': '有った',  'ませんでした': '無かった',  'ません': '無い'},
                
        }
        
        # used class
        self.clip_board = ClipBoard()
        
        # read clipping content of machine translation result at startup
        self.clip_str = self.clip_board.get()
    
    def cnvForced(self):
        """
            forcibly convert tones with a certain vocabulary pattern
            [一定の語彙パターンでトーンを強制的に変換する]
        """
        # forcibly change such as non-polite words (e.g.　more and more)
        # [丁寧語でない益々（ますます）等を強制的に置き換える]
        for k_fchg in self.dct_fchg:
            self.dct_cnv[k_fchg] = self.dct_fchg[k_fchg]
        
        # create conversion dict
        # [変換dictを作成]
        
        # extract approximate stems in order
        # [近似語幹を順に取り出す]
        for k_wgrp in self.dct_wgrp1:
            w_stem_lst = self.dct_wgrp1[k_wgrp]['語幹']
            w_schg = self.dct_wgrp1[k_wgrp]['語変']
            w_endp = self.dct_wgrp1[k_wgrp]['変化']
            
            # 語幹が変わる場合
            if '変語幹' in self.dct_wgrp1[k_wgrp]:
                w_chg_stem = True
            else:
                w_chg_stem = False
            
            # extract the stem from the list
            # [リストより語幹を取り出す]
            for w_stem in w_stem_lst:
                
                # extract polite change dict
                # [丁寧語尾変化dictを取り出す]
                
                # polite to assertive
                if not w_endp in self.dct_wchg:
                    print('not specifid -{}'.format(w_endp))
                    return(False)
                else:
                    endp_dct = self.dct_wchg[w_endp]
                
                # take polite endings in order
                # [丁寧語尾を順に取り出す]
                for polite_end in endp_dct:
                    
                    # extract the corresponding asserted endings
                    # [丁寧語尾に対応する断定語尾を取り出す]
                    assert_end = endp_dct[polite_end]
                    
                    # add to conversion dict
                    # [変換dictに加える]
                    # '語幹' + '語変' + '丁寧語尾' : '語幹'+'断定語尾'
                    
                    # 語幹が変わる場合
                    if w_chg_stem:
                        w_polite_end = w_stem + w_schg + polite_end 
                        w_assert_end = assert_end
                    else:
                        w_polite_end = w_stem + w_schg + polite_end
                        w_assert_end = w_stem + assert_end
                    self.dct_cnv[w_polite_end] = w_assert_end
                    
        # register the leaked polite tone that should be interpreted at the very end
        # [一番最後になって解釈すべき漏れた敬語表現を登録する]
        for k_tail in self.dct_tail:
            self.dct_cnv[k_tail] = self.dct_tail[k_tail]
        
        # convert polite tone to assertive one
        # [丁寧語（「です・ます」調）を断定語（「だ・である」調）に変換]
        for k in self.dct_cnv:
            self.clip_str = self.clip_str.replace(k, self.dct_cnv[k])
            
            if self.debug:
                print(k + ' : ' + self.dct_cnv[k])
            
        return(True)
    
    def cnvCoditional(self):
        """
            # convert a pattern following a specific letter into an assertion word
            # [特定の一字に続くパターンを断定語に変換する]
        """
        
        for k_wgrp in self.dct_wgrp2:
            w_stem_lst = self.dct_wgrp2[k_wgrp]['語幹']
            w_schg = self.dct_wgrp2[k_wgrp]['語変']
            w_endp = self.dct_wgrp2[k_wgrp]['変化']
            
            if not self.dct_wgrp2[k_wgrp]['漢字']:
                print('not specifid -{}'.format('漢字'))
                return(False)
            w_endp2 = self.dct_wgrp2[k_wgrp]['漢字']['変化']
            if not w_endp2 in self.dct_wchg:
                print('not specifid -{}'.format(w_endp2))
                return (False)
            
            # 語幹が変わる場合
            if '変語幹' in self.dct_wgrp2[k_wgrp]:
                w_chg_stem = True
            else:
                w_chg_stem = False
            
            # extract the stem from the list
            # [リストより語幹を取り出す]
            for w_stem in w_stem_lst:
                    
                # extract polite change dict
                # [丁寧語尾変化dictを取り出す]
                
                # polite to assertive
                if not w_endp in self.dct_wchg:
                    print('not specifid -{}'.format(w_endp))
                    return(False)
                else:
                    endp_dct = self.dct_wchg[w_endp]
                
                # polite to assertive
                if not w_endp2 in self.dct_wchg:
                    print('not specifid -{}'.format(w_endp2))
                    return(False)
                else:
                    endp_dct2 = self.dct_wchg[w_endp2]
                
                # take polite endings in order
                # [丁寧語尾を順に取り出す]
                for polite_end in endp_dct:
                    
                    # extract the corresponding asserted endings
                    # [丁寧語尾に対応する断定語尾を取り出す]
                    assert_end = endp_dct[polite_end]
                    
                    # add to conversion dict
                    # [変換dictに加える]
                    # '語幹' + '語変' + '丁寧語尾' : '語幹'+'断定語尾'
                    
                    # 語幹が変わる場合
                    if w_chg_stem:
                        w_polite_end = w_stem + w_schg + polite_end
                    else:
                        w_polite_end = w_stem + w_schg + polite_end
                    
                    # pattern of particle following one word of kanji
                    # [一語の漢字に続く助詞のパターン]
                    w_pattern = re.compile('([\u4E00-\u9FD0])' + '(' + w_polite_end + ')')
                    m_list = re.findall(w_pattern, self.clip_str)
                    if (m_list):
                        for m_item in m_list:
                            (kanji, particle) = m_item
                            polite_word = kanji + particle
                            
                            # register the target polite word in dict
                            # [対象の丁寧語をdictに登録する]
                            self.dct_cnv2[polite_word] = kanji + endp_dct2[polite_end]
                    
            # convert polite tone to assertive one
            # [丁寧語（「です・ます」調）を断定語（「だ・である」調）に変換]
            for k in self.dct_cnv2:
                self.clip_str = self.clip_str.replace(k, self.dct_cnv2[k])
            
                if self.debug:
                    print(k + ' : ' + self.dct_cnv2[k])
                    
                        
        return(True)
    
    def cnvTone(self):
        """
            convert polite tone to assertive one
            [丁寧語（「です・ます」調）を断定語（「だ・である」調）に変換]
        """
        
        # forcibly convert tones with a certain vocabulary pattern
        if not self.cnvForced():
            return(False)
        
        # convert a pattern following a specific letter into an assertion word
        if not self.cnvCoditional():
            return(False)
        
        # past result of the tone conversion to clip board
        self.clip_board.set(self.clip_str)
        
        return(True)


if __name__ == '__main__':

    cnv_tone = CnvTone()                                # convert tone
    if cnv_tone.cnvTone():
        exit(0)
    else:
        exit(1)