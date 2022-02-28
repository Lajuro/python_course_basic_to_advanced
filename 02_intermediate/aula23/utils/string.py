def add_hashtag(string, pre_add = True, pos_add = True):
    pre_string = "# "
    pos_string = " #"

    string = pre_string + string if pre_add else string
    string = string + pos_string if pos_add else string

    return string