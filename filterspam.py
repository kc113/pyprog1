def filterFun(msg, spam, ham):

    """(list,list,list) -> Boolean

    returns True if the message is more likely to be spam than ham
    
    and False if the message is less likely to be spam than ham.
    
    In the event of a tie between spam & ham, the function returns True.
    """
    print(msg)
    print(spam)
    print(ham)
    #assert that length of msg/spam/ham is at least 1.
    #assert that length of msg is at most 100.
    assert ((len(msg) > 0) and (len(msg) < 101) and (len(spam)) > 0 and (len(ham)) > 0),"Input Error!"
