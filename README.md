# 适用于 tensorflow2 的音频分类模型

该项目基于 [github.com/seth814/Audio-Classification](https://github.com/seth814/Audio-Classification) 修改，加入了对单个音频文件的检测功能和以太网音频的实时检测功能，并做了一些结构改进。原自述文件[点此](README_old.md)查看。

## 数据预处理

请将你的数据集按如下格式建立文件夹：

```
|-- class_1
  file_1,
  file_2,
  ...
|-- class_2
  file_1,
  file_2,
  ...
|-- class_3
  file_1,
  file_2,
  ...
...
```

如果你的音频数据集是 `mp3` 格式的，那么你需要将其转换为 `wav` 格式的音频， `convert_wav.py` 就可以转换。在转换完成后，请运行 `clean.py` ，该程序用于将数据集中的音频切成小片段，以便可以转换为梅尔频谱输入模型处理。 `clean.py` 中有一些必要的输入参数，你需要根据实际情况指定：

```
'--src_root', type=str, default='wavfiles'              // 数据集位置
'--dst_root', type=str, default='clean'                 // 经过 clean 处理后保存的位置
'--delta_time', '-dt', type=float, default=1.0          // 想要划分的小片段时长
'--threshold', type=str, default=20                     // 音频数据的要限制的阈值幅度
```

`clean.py` 同时会生成一个 `classes.txt` 类别文件以便其他的处理。

## 训练

`train.py` 会自动根据 `clean` 文件夹中的类别进行训练，请自行根据 `train.py` 中的描述自行指定参数并运行。

## 推理

你可以执行 `predict_eval.py` 来评估音频在整个训练数据集上推理的结果。若要实时识别 UDP 发送的音频数据，你可以执行 `predict.py` 。