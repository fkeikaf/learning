import json
import numpy as np
import pandas as pd
import random

def drawTalkTheme():
    theme_df = pd.read_csv("../resource/themes.csv", sep=',')
    # TODO unselectionが一つもないときは自動的にリセットが必要
    theme_unselection = theme_df[theme_df['used'].isnull()]
    theme_count = len(theme_unselection)
    theme_selection = random.randint(0, theme_count-1)
    theme_text = theme_unselection.iloc[theme_selection,0]
    theme_df.loc[theme_df['theme'] == theme_text, 'used'] = 1 

    response = {"result": theme_text}
    return json.dumps(response, indent=4, ensure_ascii=False)

if __name__ == "__main__": 
    drawTalkTheme()