''' ======================================================================
* Copyright (c) 2023, MongooseOrion.
* All rights reserved.
*
* The following code snippet may contain portions that are derived from
* OPEN-SOURCE communities, and these portions will be licensed with: 
*
* <NULL>
*
* If there is no OPEN-SOURCE licenses are listed, it indicates none of
* content in this Code document is sourced from OPEN-SOURCE communities. 
*
* In this case, the document is protected by copyright, and any use of
* all or part of its content by individuals, organizations, or companies
* without authorization is prohibited, unless the project repository
* associated with this document has added relevant OPEN-SOURCE licenses
* by github.com/MongooseOrion. 
*
* Please make sure using the content of this document in accordance with 
* the respective OPEN-SOURCE licenses. 
* 
* THIS CODE IS PROVIDED BY https://github.com/MongooseOrion. 
* FILE ENCODER TYPE: UTF-8
* ========================================================================
'''
# 将源目录中的音频按照相同的路径转换为 WAV，并将采样率重采样为 16kHz
from pydub import AudioSegment
import os
import shutil

input_path = "C:\\Users\\smn90\\repo\\FPGA_Audio_Noise_Gate\\dataset\\voice_adjust" 
output_path = input_path + '_clean\\'
print(output_path)
if os.path.exists(output_path):
    shutil.rmtree(output_path)

# 按顺序读取，并按顺序存储
dirs = os.listdir(input_path)

for _cls in dirs:
    target_dir = os.path.join(output_path, _cls)
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    src_dir = os.path.join(input_path, _cls)
    sub_src_dir = os.listdir(src_dir)
    for sub_cls in sub_src_dir:
        src_file_path = os.path.join(src_dir, sub_cls)
        audio = AudioSegment.from_file(src_file_path)
        if audio.channels != 1:
            audio = audio.set_channels(1)  # Convert to mono if stereo
        if audio.frame_rate != 16000:
            audio = audio.set_frame_rate(16000)  # Set the sample rate to 16kHz Hz
        # 导出文件
        target_file = os.path.join(target_dir, sub_cls.split('.')[0] + '.wav')
        audio.export(target_file, format="wav")

print('所有文件都已转换为 wav 格式。')