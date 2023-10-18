# def solution(A,F,M):
#     def find_combinations_helper(target_sum, F, current_combination, start):
#             if F == 0 and target_sum == 0:
#                 combinations.append(list(current_combination))
#                 return
            
#             for i in range(start, 7):
#                 if i > target_sum:
#                     break  
#                 current_combination.append(i)
#                 find_combinations_helper(target_sum - i, F - 1, current_combination, i)
#                 current_combination.pop()

#     target_sum = ((len(A) + F)*M) - sum(A)
    
#     if target_sum > (6*F) or target_sum <= 0:
#         print([0])
#     else:
#         combinations = []
#         find_combinations_helper(target_sum, F, [], 1)
        
#         print(combinations)
               
                
def solution(A,F,M):
    target_sum = ((len(A) + F)*M) - sum(A)
    states = [(0, [], 1)]

    if target_sum > (6*F) or target_sum <= 0:
        print([0])
    else:
        while states:
            current_sum, current_combination, start = states.pop()
            
            if current_sum == target_sum and len(current_combination) == F:
                print(current_combination)
            
            elif len(current_combination) < F:
                for i in range(start, 7):
                    if current_sum + i <= target_sum:
                        new_combination = current_combination + [i]
                        states.append((current_sum + i, new_combination, i))

solution([1,5,6], 4, 3)
solution([3,2,4,3], 2, 4)
solution([1,2,3,4], 4, 6)
solution([6,1], 1, 1)
solution([6], 10, 4)




    









