#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for i in range(len(dir(hidden_4))):
        if "__" in dir(hidden_4)[i]:
            pass
        else:
            print(dir(hidden_4)[i])
