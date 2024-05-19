from tensorflow.keras.models import load_model
from clean import downsample_mono, envelope
from kapre.time_frequency import STFT, Magnitude, ApplyFilterbank, MagnitudeToDecibel
import numpy as np
import argparse
import socket
import time


def make_prediction(args):
    model = load_model(args.model_fn,
        custom_objects={'STFT':STFT,
                        'Magnitude':Magnitude,
                        'ApplyFilterbank':ApplyFilterbank,
                        'MagnitudeToDecibel':MagnitudeToDecibel})
    
    # 设置音频参数
    RATE = args.sr
    BUFFER_SIZE = 1024

    # 创建UDP套接字
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((args.UDP_IP, args.UDP_PORT))

    print("接收 UDP 音频数据并实时进行推理分类...")

    # 从classes.txt文件中加载类别名称
    with open('classes.txt', 'r') as file:
        classes = file.readlines()
    class_list = [cls.strip() for cls in classes]

    try:
        recv_data = b''
        data = b''
        while True:
            if(len(recv_data) < 48000 * 2): 
                data, addr = sock.recvfrom(BUFFER_SIZE)  # 从UDP套接字接收数据
                recv_data = recv_data + data
                continue
            else:
                recv_data = recv_data[0:48000*2]

            # 对接收到的音频数据进行分类推理
            rate, wav = downsample_mono(recv_data, RATE, 2)
            mask, env = envelope(wav, rate, threshold=args.threshold)
            clean_wav = wav[mask]
            if(len(clean_wav) != 16000): 
                print(None)
                recv_data = b''
                time.sleep(1)
                continue
            X = clean_wav.reshape(1, -1, 1)
            y_pred = model.predict(X)
            class_index = np.argmax(y_pred)
            predicted_class = class_list[class_index]
            print('Predicted class:', predicted_class)
            recv_data = b''


    except KeyboardInterrupt:
        print("接收停止。")

    finally:
        # 关闭UDP套接字
        sock.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='实时音频分类推理')
    parser.add_argument('--model_fn', type=str, default='models/conv2d.h5',
                        help='model file to make predictions')
    parser.add_argument('--UDP_IP', type=str, default='192.168.0.3',
                        help='UDP IP address to receive audio data')
    parser.add_argument('--UDP_PORT', type=int, default=8080,
                        help='UDP port to receive audio data')
    parser.add_argument('--dt', type=float, default=1.0,
                        help='time in seconds to sample audio')
    parser.add_argument('--sr', type=int, default=16000,
                        help='sample rate of clean audio')
    parser.add_argument('--threshold', type=str, default=20,
                        help='threshold magnitude for np.int16 dtype')
    args, _ = parser.parse_known_args()

    make_prediction(args)
