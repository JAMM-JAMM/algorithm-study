# 상호 평가

def solution(scores):
    
    new_scores = list(map(list, zip(*scores)))
    
    averages = []
    
    answer = ''
    
    for idx, score in enumerate(new_scores):
        if (score.count(score[idx]) == 1) and (score[idx] == max(score) or score[idx] == min(score)):
            score.remove(score[idx])
            averages.append(sum(score)/len(score))
        else:
            averages.append(sum(score)/len(score))
    
    for average in averages:
        if average >= 90:
            answer += 'A'
        elif 80 <= average < 90:
            answer += 'B'
        elif 70 <= average < 80:
            answer += 'C'
        elif 50 <= average < 70:
            answer += 'D'
        else:
            answer += 'F'
    
    return answer