import pandas as pd

dis = {
    'A':[1,2,3,4,5,6],
    'B':[3,2,1,4,5,6],
    'C':[3,5,6,7,8,9]
}
data = pd.DataFrame(dis)

# data.to_csv("Test_new_CSV.csv")
# data.to_csv("Test_new_CSV1.csv",index=False)
data.to_csv("Test_new_CSV2.csv",index=False,header=[1,2,3])