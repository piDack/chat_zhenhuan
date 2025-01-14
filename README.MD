# Chat-甄嬛
 
> 本repo基于[chatGLM](https://github.com/THUDM/ChatGLM-6B)模型以及[chatglm_finetuning](https://github.com/ssbuild/chatglm_finetuning)提供的微调脚本。甄嬛对话数据集来自于互联网，灵感来着[Fine-tune LLaMA to speak like Homer Simpson](https://replicate.com/blog/fine-tune-llama-to-speak-like-homer-simpson)

## 模型效果

训练结果可在[huggingface](https://huggingface.co/Pcdack/chat_zhenhuan)下载。

在数据集中的数据已经得到记忆

```
你是谁:   家父是大理寺少卿甄远道。
大理寺少卿，也不是什么高官:   凡事不论官位高低，只论个理字。
小主怎么了？脸色怎么这么差:   我心里慌得厉害。浣碧，你去找温太医来瞧瞧——记得，温大人请起，眉姐姐的身子要往场场请安，本宫的宫外用香也无碍，你且去送过东西没有？
```

对在数据集中的问题进行轻微改动也可正常回答

```
原：弘曕到底是不是朕的儿子？
弘曕是不是朕的孩子？:   当然，天下万民都是皇上您的子民
原：年羹尧不是骁勇善战吗，怎么不让他去平定准葛尔的边患？
为什么不让骁勇善战年羹尧去平？:   能用一个女子就能平息的事情，何必动用千军万马？何况年羹尧军功高权重，若是输，咱们要付出的不止一个公主，若是赢，年羹尧军功更盛，功高震主，所以和亲是皇上的伤言，若真一败涂地，年羹尧会难受的。
```

不在数据集中的数据会胡编乱造：

```
你有没有私通:   臣妾失德，不宜侍奉皇上。
你就要行册封礼，好好歇着:   多谢皇后娘娘。
华妃娘娘来找你来:   眉姐姐在吗？
```

## 使用步骤
### 数据处理
1. 下载对话脚本到/data/raw目录下;
2. 然后使用/data/script/raw2alpaca.py（需进行部分修改）进行处理，输出结果为`output.json`;
3. 继续使用alpaca2qa.py进行处理，需要注意的是记得修改prompt；
4. 将输出结果`finetune_train_examples.json`移动到`/data/`目录下。

### 微调训练
参照[chatglm_finetuning](https://github.com/ssbuild/chatglm_finetuning) repo提供的步骤。
1. 执行`data_utils.py`
2. 执行`train.py`
