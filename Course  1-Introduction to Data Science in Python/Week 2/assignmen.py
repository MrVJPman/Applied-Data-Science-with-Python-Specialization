# You should write your whole answer within the function provided. The autograder will call
# this function and compare the return value against the correct solution value
def answer_zero():
    # This function returns the row for Afghanistan, which is a Series object. The assignment
    # question description will tell you the general format the autograder is expecting
    return df.iloc[0]

# You can examine what your function returns by calling it in the cell. If you have questions
# about the assignment formats, check out the discussion forums for any FAQs
answer_zero() 


def answer_one():
    return df[df["Gold"] ==  df["Gold"].max()].index[0]


def answer_two():
    return "YOUR ANSWER HERE"

df_difference = df[["Gold", "Gold.1"]]
df_difference["difference"] = abs(df_difference["Gold"] - df_difference["Gold.1"])
df_difference