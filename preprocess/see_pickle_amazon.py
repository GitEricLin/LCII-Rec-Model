import os
import pickle

def load_pickle(pickle_file):
    return pickle.load(open(pickle_file, 'rb'))

dataset = 'amazon'
home = (os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir)))+"./datasets"
DATASET_DIR = home + "/" + dataset
DATASET_FILE_1 = DATASET_DIR + '/Clothing_Shoes_and_Jewelry_Result_2018.csv'
user_sessions = DATASET_DIR + '/2_user_sessions.pickle' 
user_sessions_filter = DATASET_DIR + '/3_user_sessions_filter.pickle' 
pickle_train_test_split = DATASET_DIR + '/4_train_test_split.pickle' 
pickle_train_test_split_sample = DATASET_DIR + '/4_train_test_split_sample.pickle' 
user_sessions = load_pickle(user_sessions)
user_sessions_filter = load_pickle(user_sessions_filter)
pickle_train_test_split = load_pickle(pickle_train_test_split)
pickle_train_test_split_sample = load_pickle(pickle_train_test_split_sample)

with open(DATASET_FILE_1, 'rt', buffering=10000, encoding='utf8') as dataset:
    count = 0
    for i in dataset:
        print(i)
        count += 1
        if count == 3: break
count = 0
for i in user_sessions:
    print(i)
    count += 1
    if count == 3: break

## user_sessions_filter (dict)
type(user_sessions_filter)
u_count = 0
i_count = 0
for k, v in user_sessions_filter.items():
    u_count +=1
    i_count = i_count + len(v)
print("user : %.2f" %u_count)
print("items: %.2f" %i_count)
count = 0
for i in user_sessions_filter.items():
    print(i)
    count += 1
    if count == 3: break
print("查閱: 輸入資料情況")
count_action_to_user = []
count_sess_to_user = []
count_act_to_sess = []
for user, session in user_sessions_filter.items():
    count_sess_to_user.append(len(session))
    temp_c = 0
    for action in session:
        temp_c += len(action)
        count_act_to_sess.append(len(action))
    count_action_to_user.append(temp_c)
    
print("平均每個用戶分配多少action的資料長度(應要與用戶數一致):",len(count_action_to_user))
print("平均每個用戶分配多少session的資料長度(應要與用戶數一致):",len(count_sess_to_user))
print("平均每個session分配多少action的資料長度(應要與session數一致):",len(count_act_to_sess))
print("\n查閱: 四分位距")
count_action_to_user = sorted(count_action_to_user, reverse = False)
Q1 = int(len(count_action_to_user)/4*1)
Q2 = int(len(count_action_to_user)/4*2)
Q3 = int(len(count_action_to_user)/4*3)
print("平均每個用戶分配多少action | Q1:",count_action_to_user[Q1],"Q2:",count_action_to_user[Q2],"Q3:",count_action_to_user[Q3])
count_sess_to_user = sorted(count_sess_to_user, reverse = False)
Q1 = int(len(count_sess_to_user)/4*1)
Q2 = int(len(count_sess_to_user)/4*2)
Q3 = int(len(count_sess_to_user)/4*3)
print("平均每個用戶分配多少session | Q1:",count_sess_to_user[Q1],"Q2:",count_sess_to_user[Q2],"Q3:",count_sess_to_user[Q3])
count_act_to_sess = sorted(count_act_to_sess, reverse = False)
Q1 = int(len(count_act_to_sess)/4*1)
Q2 = int(len(count_act_to_sess)/4*2)
Q3 = int(len(count_act_to_sess)/4*3)
print("平均每個session分配多少action | Q1:",count_act_to_sess[Q1],"Q2:",count_act_to_sess[Q2],"Q3:",count_act_to_sess[Q3])

## Fully data
trainset = pickle_train_test_split['trainset']
testset = pickle_train_test_split['testset']
train_session_lengths = pickle_train_test_split['train_session_lengths']
test_session_lengths = pickle_train_test_split['test_session_lengths']
user_count = 0
item_type = {}
items_in_sess = 0
session_nums_train = 0
session_nums_test = 0
pading_count = 0
User = {}
Session = {}
for user, user_sess in trainset.items():
    if user not in User:
        User[user] = 0
        user_count +=1
    User[user] += 1
    count_sess_len = len(user_sess)  
    if count_sess_len not in Session: Session[count_sess_len] = 0
    Session[count_sess_len] += 1
    session_nums_train = session_nums_train + len(user_sess)
    for each_session in user_sess:
        items_in_sess = items_in_sess + len(each_session)
        for i in each_session:
            if i[1] not in item_type: item_type[i[1]] = True
            if i == [0, 0]: pading_count += 1

for user, user_sess in testset.items():
    if user not in User:
        User[user] = 0
        user_count +=1
    User[user] += 1
    count_sess_len = len(user_sess)  
    if count_sess_len not in Session: Session[count_sess_len] = 0
    Session[count_sess_len] += 1
    session_nums_test = session_nums_test + len(user_sess)
    for each_session in user_sess:
        items_in_sess = items_in_sess + len(each_session)
        for i in each_session:
            if i[1] not in item_type: item_type[i[1]] = True
            if i == [0, 0]: pading_count += 1
  
session_nums = session_nums_train+session_nums_test
pading_proportion = pading_count/items_in_sess*100
pading_proportion = "%.2f" %pading_proportion
print(" --  以下數據包含 amazon: train + test 統計")
print(" --  資料集中的session長短分佈 [sess長短: 以及其數量]:  "+str(Session))
print(" --  ---------------------------------------------------------------------------------------------------------------- ")
print(" --  總計User | "+str(user_count))
print(" --  session train | "+str(session_nums_train))
print(" --  session test | "+str(session_nums_test))
print(" --  總計session | "+str(session_nums))
print(" --  總計互動種類 | "+str(len(item_type)))
print(" --  總計互動紀錄 | "+str(items_in_sess))
print(" --  總計互動紀錄(扣除缺值) | "+str(items_in_sess-pading_count))
print(" --  平均每個 User 分配 item | "+str(round(items_in_sess/user_count,2)))
print(" --  平均每個 User 分配 item(扣除缺值) | "+str(round((items_in_sess-pading_count)/user_count,2)))
print(" --  平均每個 User 分配 session | "+str(round((session_nums/user_count),2)))
print(" --  平均每個 Session 分配 item | "+str(round((items_in_sess-pading_count)/session_nums,2)))
print(" --  每個session中有幾個互動 | "+str(items_in_sess/session_nums))
print(" --  總計缺值[0,0] | "+str(pading_count))
print(" --  缺值佔整體item多少比例 | "+ str(pading_proportion) +"%")

## Sample
trainset = pickle_train_test_split_sample['trainset']
testset = pickle_train_test_split_sample['testset']
train_session_lengths = pickle_train_test_split_sample['train_session_lengths']
test_session_lengths = pickle_train_test_split_sample['test_session_lengths']
user_count = 0
item_type = {}
items_in_sess = 0
session_nums_train = 0
session_nums_test = 0
pading_count = 0
User = {}
Session = {}
for user, user_sess in trainset.items():
    if user not in User:
        User[user] = 0
        user_count +=1
    User[user] += 1
    count_sess_len = len(user_sess)  
    if count_sess_len not in Session: Session[count_sess_len] = 0
    Session[count_sess_len] += 1
    session_nums_train = session_nums_train + len(user_sess)
    for each_session in user_sess:
        items_in_sess = items_in_sess + len(each_session)
        for i in each_session:
            if i[1] not in item_type: item_type[i[1]] = True
            if i == [0, 0]: pading_count += 1
for user, user_sess in testset.items():
    if user not in User:
        User[user] = 0
        user_count +=1
    User[user] += 1
    count_sess_len = len(user_sess)  
    if count_sess_len not in Session: Session[count_sess_len] = 0
    Session[count_sess_len] += 1
    session_nums_test = session_nums_test + len(user_sess)
    for each_session in user_sess:
        items_in_sess = items_in_sess + len(each_session)
        for i in each_session:
            if i[1] not in item_type: item_type[i[1]] = True
            if i == [0, 0]: pading_count += 1
  
session_nums = session_nums_train+session_nums_test
pading_proportion = pading_count/items_in_sess*100
pading_proportion = "%.2f" %pading_proportion
print(" --  以下數據包含 amazon_sample: train + test 統計")
print(" --  資料集中的session長短分佈 [sess長短: 以及其數量]:  "+str(Session))
print(" --  ---------------------------------------------------------------------------------------------------------------- ")
print(" --  總計User | "+str(user_count))
print(" --  session train | "+str(session_nums_train))
print(" --  session test | "+str(session_nums_test))
print(" --  總計session | "+str(session_nums))
print(" --  總計互動種類 | "+str(len(item_type)))
print(" --  總計互動紀錄 | "+str(items_in_sess))
print(" --  總計互動紀錄(扣除缺值) | "+str(items_in_sess-pading_count))
print(" --  平均每個 User 分配 item | "+str(round(items_in_sess/user_count,2)))
print(" --  平均每個 User 分配 item(扣除缺值) | "+str(round((items_in_sess-pading_count)/user_count,2)))
print(" --  平均每個 User 分配 session | "+str(round((session_nums/user_count),2)))
print(" --  平均每個 Session 分配 item | "+str(round((items_in_sess-pading_count)/session_nums,2)))
print(" --  每個session中有幾個互動 | "+str(items_in_sess/session_nums))
print(" --  總計缺值[0,0] | "+str(pading_count))
print(" --  缺值佔整體item多少比例 | "+ str(pading_proportion) +"%")