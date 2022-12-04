S={12001:{'CA1':'S','CA2':'S','CA3':'A','CA4':'E','CA5':'C'},
      12002 : {'CA1':'B','CA2':'F','CA3':'C','CA4':'D','CA5':'E'}}

G=['S','A','B','C','D','E','F','X']


def sub_basedon_grade(gr):
    d={}
    for roll,res in S.items():
        d[roll]=""
        s=[]
        for subj,grade in res.items():
            if grade==gr:
                s.append(subj)
        if s!=[]:
            d[roll]=s
        else:
            d[roll]='None'
    print(d)
        

sub_basedon_grade('A')


def Highest_grade_Subjects():
    d={}
    for roll,res in S.items():
        d[roll]=""
        for g in G:
            s=[]
            for subj,grade in res.items():
                if grade==g:
                    s.append((subj,grade))
            d[roll]=s
            if s!=[]:
                break
    print(d)
    
Highest_grade_Subjects()







