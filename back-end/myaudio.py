import pyaudio
import wave
from aip import AipSpeech

APP_ID = '118427177'
API_KEY = '9vNHYQw9YNSuGnUwTGtJ7rib'
SECRET_KEY = '8dUiPfOPv0dcWsHmoFnVOXQzkCJqti18'

# 录音
def record_audio(filename, duration):
    #recording = True
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000

    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    print("Recording...")

    frames = []
    
    for i in range(0, int(RATE / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    print('end')

# 识别
def recognize_audio(audio_file):
    # 使用百度语音识别大模型进行语音识别
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    # 读取音频文件
    with open(audio_file, 'rb') as f:
        audio_data = f.read()

    # 进行语音识别
    result = client.asr(audio_data, 'wav', 16000, {
        'dev_pid': 1537, 
    })


    if 'result' in result:
        # 提取识别结果
        print(result)
        return result['result'][0]
    else:
        # 识别失败
        print(result)
        return "识别失败"
    
record_audio("4.9.wav",10)
recognize_audio('audio1.wav')