
def read_input ( lines ):
    user_friend_lists = {}
    for line in lines:
        user,friendListString = line.split('\t')
        user = int(user)
        if len(friendListString) != 1: # bo nhung id nao ko co ban
            user_friend_lists[user] = [int(i) for i in friendListString.strip().split(',')]
    return user_friend_lists

def find_recomment_friend( user_friend_list, U):
    recomment_friend = {}
    for i in user_friend_list:
        if( i != U):
            set_user = set(user_friend_list[U]) 
            set_other_user = set(user_friend_list[i])
            mutualFriend = set_user.intersection(set_other_user) #tim so ban giong nhau
            if len(recomment_friend) < N : #neu hang cho chua day
                recomment_friend[i] = len(mutualFriend)
            else:
                minval = min(recomment_friend.values()) #tim value nho nhat trong hang cho
                if len(mutualFriend) >= minval :
                    res = [k for k, v in recomment_friend.items() if v==minval] #tim list key co value be nhat
                    res.sort()
                    recomment_friend[i] = len(mutualFriend) 
                    del recomment_friend[res.pop()] #xoa phan tu 
    return recomment_friend

def result( U , user_friend_list):
    output = open('output.txt','w')
    if U not in user_friend_list and U < 50000: # neu ko co ban hoac ko ton tai
        output.write("Not have a friend ")
    elif U >= 50000:
        output.write("Don't have a id? Do you want to create an account?")
    else: 
        recomment_friend = find_recomment_friend(user_friend_list, U) #tao hang cho
        
        rcmtFriendList = [str(interger) for interger in recomment_friend.keys()]
        string_rcmtFriendList = "\n".join(rcmtFriendList)
        output.write(string_rcmtFriendList)

file_input = open('data.txt', 'r')

lines = file_input.readlines()
user_friend_list = read_input(lines)
   
file_input.close()

U = int(input())
N = int(input())

result(U, user_friend_list)

    


