# ������ tensorflow2 ����Ƶ����ģ��

����Ŀ���� [github.com/seth814/Audio-Classification](https://github.com/seth814/Audio-Classification) �޸ģ������˶Ե�����Ƶ�ļ��ļ�⹦�ܺ���̫����Ƶ��ʵʱ��⹦�ܣ�������һЩ�ṹ�Ľ���ԭ�����ļ�[���](README_old.md)�鿴��

## ����Ԥ����

�뽫������ݼ������¸�ʽ�����ļ��У�

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

��������Ƶ���ݼ��� `mp3` ��ʽ�ģ���ô����Ҫ����ת��Ϊ `wav` ��ʽ����Ƶ�� `convert_wav.py` �Ϳ���ת������ת����ɺ������� `clean.py` ���ó������ڽ����ݼ��е���Ƶ�г�СƬ�Σ��Ա����ת��Ϊ÷��Ƶ������ģ�ʹ��� `clean.py` ����һЩ��Ҫ���������������Ҫ����ʵ�����ָ����

```
'--src_root', type=str, default='wavfiles'              // ���ݼ�λ��
'--dst_root', type=str, default='clean'                 // ���� clean ����󱣴��λ��
'--delta_time', '-dt', type=float, default=1.0          // ��Ҫ���ֵ�СƬ��ʱ��
'--threshold', type=str, default=20                     // ��Ƶ���ݵ�Ҫ���Ƶ���ֵ����
```

`clean.py` ͬʱ������һ�� `classes.txt` ����ļ��Ա������Ĵ���

## ѵ��

`train.py` ���Զ����� `clean` �ļ����е�������ѵ���������и��� `train.py` �е���������ָ�����������С�

## ����

�����ִ�� `predict_eval.py` ��������Ƶ������ѵ�����ݼ�������Ľ������Ҫʵʱʶ�� UDP ���͵���Ƶ���ݣ������ִ�� `predict.py` ��