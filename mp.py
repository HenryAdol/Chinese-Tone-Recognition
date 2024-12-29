import pandas as pd
from multiprocessing import Pool
from tqdm import tqdm
from pydub import AudioSegment

# Fix the path - removed space after "Recognition"
result = pd.read_csv("./small_wav_dataset/small_wav_dataset.csv")

def mp(file_name):
    try:
        # Updated paths to use underscores instead of spaces
        audio = AudioSegment.from_mp3('./small_dataset/clips/' + file_name)  
        audio.export("./small_wav_dataset/wav_clips/" + file_name[:-4] + ".wav", format='wav')
    except Exception as err:
        print(f"mp error: {str(err)}")

def main():
    with Pool(6) as p:
        total = len(result['path'])
        list(tqdm(p.imap(mp, result['path']), total=total, desc="Converting files"))

if __name__ == '__main__':
    main()