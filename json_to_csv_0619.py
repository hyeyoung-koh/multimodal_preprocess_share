import json
import pandas as pd

def json_to_csv(t):
    episode_nos = []
    scripts = []
    person_ids = []
    emotion_text_emotions = []
    emotion_text_valences = []
    emotion_text_arousals = []
    emotion_sound_emotions = []
    emotion_sound_valences = []
    emotion_sound_arousals = []
    emotion_multimodal_emotions = []
    emotion_multimodal_valences = []
    emotion_multimodal_arousals = []
    text_strategies = []
    text_script_ends = []
    text_script_starts = []
    text_scripts = []
    text_intents = []
    df = pd.DataFrame()
    with open('D:\\json_file_list\\clip_' + str(t) + '.json', 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
        frames = []
        for key, value in data['data'].items():
            frames.append(key)
    for i in range(len(frames)):
        frame = frames[i]
        for ppl in data['data'][frame].keys():
            if 'text' in data['data'][frame][ppl].keys():
                episode_no = data['clip_id']
                script = data['data'][frame][ppl]['text']['script']
                person_id = data['data'][frame][ppl]['person_id']
                emotion_text_emotion = data['data'][frame][ppl]['emotion']['text']['emotion']
                emotion_text_valence = data['data'][frame][ppl]['emotion']['text']['valence']
                emotion_text_arousal = data['data'][frame][ppl]['emotion']['text']['arousal']
                emotion_sound_emotion = data['data'][frame][ppl]['emotion']['sound']['emotion']
                emotion_sound_valence = data['data'][frame][ppl]['emotion']['sound']['valence']
                emotion_sound_arousal = data['data'][frame][ppl]['emotion']['sound']['arousal']
                emotion_multimodal_emotion = data['data'][frame][ppl]['emotion']['multimodal']['emotion']
                emotion_multimodal_valence = data['data'][frame][ppl]['emotion']['multimodal']['valence']
                emotion_multimodal_arousal = data['data'][frame][ppl]['emotion']['multimodal']['arousal']
                text_strategy = data['data'][frame][ppl]['text']['strategy']
                text_script_end = data['data'][frame][ppl]['text']['script_end']
                text_script_start = data['data'][frame][ppl]['text']['script_start']
                text_script = data['data'][frame][ppl]['text']['script']
                text_intent = data['data'][frame][ppl]['text']['intent']
                episode_nos.append(episode_no)
                scripts.append(script)
                person_ids.append(person_id)
                emotion_text_emotions.append(emotion_text_emotion)
                emotion_text_valences.append(emotion_text_valence)
                emotion_text_arousals.append(emotion_text_arousal)
                emotion_sound_emotions.append(emotion_sound_emotion)
                emotion_sound_valences.append(emotion_sound_valence)
                emotion_sound_arousals.append(emotion_sound_arousal)
                emotion_multimodal_emotions.append(emotion_multimodal_emotion)
                emotion_multimodal_valences.append(emotion_multimodal_valence)
                emotion_multimodal_arousals.append(emotion_multimodal_arousal)
                text_strategies.append(text_strategy)
                text_script_ends.append(text_script_end)
                text_script_starts.append(text_script_start)
                text_scripts.append(text_script)
                text_intents.append(text_intent)
    df['Episode_no'] = episode_nos
    df['Episode_sequence'] = ''
    df['person_id'] = person_ids
    df['age'] = ''
    df['gender'] = ''
    df['text_emotion'] = emotion_text_emotions
    df['text_valence'] = emotion_text_valences
    df['text_arousal'] = emotion_text_arousals
    df['sound_emotion'] = emotion_sound_emotions
    df['sound_valence'] = emotion_sound_valences
    df['sound_arousal'] = emotion_sound_arousals
    df['multimodal_emotion'] = emotion_multimodal_emotions
    df['multimodal_valence'] = emotion_multimodal_valences
    df['multimodal_arousal'] = emotion_multimodal_arousals
    df['text_strategy'] = text_strategies
    df['text_script_start'] = text_script_starts
    df['text_script_end'] = text_script_ends
    df['text_script'] = text_scripts
    df['text_intent'] = text_intents

    for i, row in df.iterrows():
        if df['person_id'][i] == list(data['actor'].keys())[0]:
            pid = list(data['actor'].keys())[0]
            df.loc[i, 'age'] = data['actor'][pid]['age']
            df.loc[i, 'gender'] = data['actor'][pid]['gender']
        if df['person_id'][i] == list(data['actor'].keys())[1]:
            pid2 = list(data['actor'].keys())[1]
            df.loc[i, 'age'] = data['actor'][pid2]['age']
            df.loc[i, 'gender'] = data['actor'][pid2]['gender']
    df2 = df.drop_duplicates(['text_script']).sort_values(by=df.columns[15], ascending=True)
    df3 = df2.reset_index(drop=True)

    for j in range(len(df3)):
        df3.loc[j, 'Episode_sequence'] = j + 1
    df3.to_csv('D:\\json_file_list\\clip_' + str(t) + '.csv', encoding='utf-8-sig', index=False)