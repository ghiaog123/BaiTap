
def read_input ( lines ):
    user_friend_lists = {}
    for line in lines:
        user,friendListString = line.split('\t')
        user = int(user)
        if len(friendListString) != 1: # bo nhung id nao ko co ban
            user_friend_lists[user] = [int(i) for i in friendListString.strip().split(',')]
    return user_friend_lists


def find_recomment_friend( user_friend_list, U, N):
    
    recomment_friend = {}
    for i in user_friend_list:
        
        if( i != U):
            set_user = set(user_friend_list[U]) 
            set_other_user = set(user_friend_list[i])
            mutualFriend = set_user.intersection(set_other_user) #find mutual friend
            
            if len(recomment_friend) < N : 
                recomment_friend[i] = len(mutualFriend)
                
            else:
                minval = min(recomment_friend.values()) #find min value
                
                if len(mutualFriend) >= minval :
                    res = [k for k, v in recomment_friend.items() if v==minval] 
                    res.sort()
                    recomment_friend[i] = len(mutualFriend) 
                    del recomment_friend[res.pop()] #delete the highest key
    
    return sort_the_result(recomment_friend, N)
 
 
def sort_the_result( recomment_friend , N ): #sort the recomment friend
    
    if len(recomment_friend) < N:
        recomment_friend_sorted =sorted(recomment_friend.items(), key=lambda x : x[1], reverse = True)
        recomment_friend_sorted = dict(recomment_friend_sorted)
        return recomment_friend_sorted
    
    else:
        recomment_friend_sorted = sorted(recomment_friend.items(), reverse = False)
        recomment_friend_sorted = dict(recomment_friend_sorted)
        return recomment_friend_sorted
  
def result( U , user_friend_list, N):
    output = open('output.txt','w')
    
    if U not in user_friend_list and U < 50000: # if id not exist
        str_U = str(U)
        output.write(str(U))
        
    elif U >= 50000:
        output.write("Don't have a id? Do you want to create an account?")
        
    else: 
        recomment_friend = find_recomment_friend(user_friend_list, U, N) 
        str_U = str(U) + '\t'
        output.write(str_U)
        
        rcmtFriendList = [str(interger) for interger in recomment_friend.keys()]
        string_rcmtFriendList = ", ".join(rcmtFriendList)
        output.write(string_rcmtFriendList)


file_input = open('data.txt', 'r')

lines = file_input.readlines()
user_friend_list = read_input(lines)
   
file_input.close()

U = int(input())
N = int(input())

result(U, user_friend_list, N)

    


