from leaderboard import leaderboard
user_score = leaderboard()

def get_leaderboard():
    st = "Топ игроков:\n"
    sh = [user_score.get(i) for i in user_score.raw_data()]
    sk = list(user_score.keys())
    for i in range(len(sk)-1):
        for j in range(len(sk)-i-1):
            if sh[j] < sh[j+1]:
                sh[j],sh[j+1] = sh[j+1],sh[j]
                sk[j],sk[j+1] = sk[j+1],sk[j]
    for i in range(len(sh)):
        st += "@id"+ str(sk[i]) + " : " + str(sh[i]) + "\n"
    return st

def score_pLus(id):
    user_score.set(id)

def new_player(id):
    user_score.add(id,0)

def get(id):
    return user_score.get(id)
