# Timur loves codeforces. That's why he has a string 𝑠
#  having length 10
#  made containing only lowercase Latin letters. Timur wants to know how many indices string 𝑠
#  differs from the string "codeforces".

# For example string 𝑠=
#  "coolforsez" differs from "codeforces" in 4
#  indices, shown in bold.

# Help Timur by finding the number of indices where string 𝑠
#  differs from "codeforces".

# Note that you can't reorder the characters in the string 𝑠
# .

def different_indexes(timurs_string):
    dif_index=0
    main_string= "codeforces"
    for i in range(0,10):
        if timurs_string[i] not in main_string[i]:
            dif_index+=1
        else:
            continue
    print(dif_index)
different_indexes("cadafurcie")
different_indexes("codeforces")
