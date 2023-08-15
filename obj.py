import cv2 as cv 
import math 
import numpy as np
from xgboost import XGBClassifier
import sklearn
import pickle as pkl

def get_r(Video_File_Path):
    # Video_File_Path = "F:/Important/Python/Projects/3.CCTV Vilonce Detection/SCVD/videos/Non-Violence Videos/nv2.mov"
    Video_Cap = cv.VideoCapture(Video_File_Path)
    Frame_Rate = Video_Cap.get(5)
    video_frame_list =[]    
    while Video_Cap.isOpened():
            Current_Frame_ID = Video_Cap.get(1)
            ret,frame = Video_Cap.read()
            if ret != True:
                break
                
            if Current_Frame_ID % math.floor(Frame_Rate) == 0:
                Frame_Resize = cv.resize(frame,(64,64))
                video_frame_list.append(Frame_Resize)
                
                
    Video_Cap.release()

    X_2D_Violence = np.reshape(video_frame_list, (len(video_frame_list), 64*64*3))
    X_2D_Violence = X_2D_Violence.astype(int)
    pickled_model = pkl.load(open('F:/Important/Python/Projects/3.CCTV Vilonce Detection/code/3.Classification/xgmodel.pkl', 'rb'))
    y_pred = pickled_model.predict(X_2D_Violence)
    
    violence = np.unique(y_pred)

    return {"length": len(video_frame_list), "predicted": y_pred.tolist(), "violence": int(violence[0]) }