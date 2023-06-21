def solution(answers):
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    student_tot = [student1, student2, student3]

    ans_tot = [[], [], []]
    correct = []
    max_correct = []

    for i in range(3):
        
        sti = student_tot[i]

        ans_tot[i] = [answers[i] - sti[i % len(sti)] for i in range(len(answers))]
        correct_cnt = ans_tot[i].count(0)
        correct.append(correct_cnt)

        max_correct = [idx + 1 for idx, v in enumerate(correct) if v == max(correct)]

    return max_correct

#-------------------------------------------------------------X
# 시간초과 실패

# def solution(answers):
#     student1 = [1, 2, 3, 4, 5]
#     student2 = [2, 1, 2, 3, 2, 4, 2, 5]
#     student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
#     student_tot = [student1, student2, student3]

#     ans1 = []
#     ans2 = []
#     ans3 = []
#     ans_tot = [ans1, ans2, ans3]
#     correct = []
#     max_correct = []

#     for i in range(3):
#         sti = student_tot[i]

#         x = len(answers) // len(sti)
#         y = len(answers) % len(sti)
#         sti = sti * x + sti[:y]

#         ans_tot[i] = [s - a for idx_s, s in enumerate(sti) for idx_a, a in enumerate(answers) if idx_s == idx_a]
#         correct_cnt = ans_tot[i].count(0)
#         correct.append(correct_cnt)

#         max_correct = [idx + 1 for idx, v in enumerate(correct) if v == max(correct)]

#     return max_correct