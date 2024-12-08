
def is_imposter(information, corrupter_fuction):
    if id(information[0]) == id(corrupter_fuction[0]):
        return False
    else:
        return True

'''
The way to solve is to check in og list if theres a nested list or element and see if something changed in the new container is changed
Inner lists are changed and that change is reflected in both the shallow and og
'''