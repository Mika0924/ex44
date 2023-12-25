import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

encoder = OneHotEncoder(handle_unknown='ignore')

encoder_df = pd.DataFrame(encoder. fit_transform(data[['whoAmI']]). toarray ())

final_df = data.join (encoder_df)

print(final_df)