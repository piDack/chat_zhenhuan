# -*- coding: utf-8 -*-
# @Time    : 2023/4/9 11:20
# 格式参照：https://replicate.com/blog/fine-tune-llama-to-speak-like-homer-simpson
#```json
#{'previous': 'Marge Simpson: Ooo, careful, Homer.',
# 'character': 'Homer Simpson',
# 'line': "There's no time to be careful."}
#```
import json

PROMPT='{prompt}'

def alaca2qa(src,dst):
    with open(src,mode='r',encoding='utf-8') as f:
        list_data_dict = json.loads(f.read())
    sources = [
        PROMPT.format_map({'character':example['c'], 'prompt': example['p']}) 
        for example in list_data_dict
    ]
    targets = [f"{example['l']}" for example in list_data_dict]

    with open(dst, mode='w', encoding='utf-8',newline='\n') as f:

        for i,(s, t) in enumerate(zip(sources, targets)):
            paragraph = [
                {
                    'q': s,
                    'a': [t]
                }
            ]
            f.write(json.dumps({'id': i+1 ,'paragraph' : paragraph },ensure_ascii=False) +'\n')


if __name__ == '__main__':
    src = r'./output.json'
    dst = r'./finetune_train_examples.json'
    alaca2qa(src,dst)
