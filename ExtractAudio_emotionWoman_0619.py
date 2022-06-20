from pydub import AudioSegment
import pandas as pd
import os


def extract_audio_feature(wav_file):
    audio=AudioSegment.from_wav(wav_file)
    audio=audio.set_channels(1)
    audio=audio.get_array_of_samples()
    #print(type(audio))
    return audio

#df1=pd.read_csv('F:/감성대화/원천데이터/man5000_2.csv',encoding='utf-8-sig')
#print(df1.columns)
df2 = pd.read_csv('F:/감성대화/원천데이터/woman5000_2.csv', encoding='utf-8-sig')
#print(df2.head())
#df4=pd.DataFrame(columns=['Episode_no','age','text','audio'])

for i in range(len(df2)):
    wav_file='F:/감성대화/원천데이터/감성대화말뭉치AI데이터_Wave_남자성우_5000/'+str(df2.iloc[i, 0])+'.wav'
    audio_feature = extract_audio_feature(wav_file)
    df2=df2.append(pd.DataFrame(audio_feature, columns=['audio']), ignore_index=True)
    i+=1

print(df2.head())

#-------------------------
# for j in range(1907,1985): # j-> Episode_no 컬럼
#     if j==2005 or j==3038 or j==3101 or j==3109 or j==3166 or j==3173 or j==3174 or j==3177 or j==3193 or j==3251 or j==3270 or j==3273 or j==3274 or j==3288 or j==3289 or j==3290 or j==3291 or j==3295 or j==3296 or j==3299 or j==3301 or j==3305 or j==3312 or j==3315 or j==3316 or j==3320 or j==3331 or j==3333 or j==3337 or j==3356 or j==3366 or j==3401 or j==3402 or j==3405 or j==3406 or j==3408 or j==3412 or j==3414 or j==3415 or j==3416 or j==3427 or j==3429 or j==3435 or j==3437 or j==3440:
#         continue
#     ii=[i for i in os.listdir('F:/wav_file_cut') if 'clip'+str(j)+'_' in i]
#     for k in range(len(ii)): #k-> Episode_sequence 컬럼
#         wav_cut_file='F:/wav_file_cut/'+ii[k]
#         audio_feature=extract_audio_feature(wav_cut_file)
#         df1=df1.append(pd.DataFrame([audio_feature],columns=['audio']),ignore_index=True)
#         df2=df2.append()
#         #df4=df4.append(pd.DataFrame([[j,k,audio_feature]],columns=['Episode_no','Episode_sequence','audio']),ignore_index=True)
#         k+=1
#     print(j)
#     j+=1
#
# df4.to_pickle('D:/df_pickle_1907to1984.pkl')
#-------------------------------
#df4.to_csv('D:/json_file_list/df_pickle_4000.csv')
#----------------------------------------------------------------------------

# data=pd.read_pickle('D:/json_file_list/df_pickle_3000.pkl')
# print(data)
# print(data['Episode_sequence'])
# print(data['Episode_no'])
#
# # import pickle
# # pickle.load('D:/json_file_list/df_pickle_5600.pkl')
# import pickle
# with open('D:/json_file_list/df_pickle_5600.pkl','rb') as fr:
#     data=pickle.load(fr)
# print(data)


