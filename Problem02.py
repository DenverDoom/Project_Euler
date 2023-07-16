def even_fibo_series(limit):
    first_term = 1
    second_term = 1
    result_term = 0
    even_fibo_list = list()
    while(result_term <= limit):
        result_term = first_term + second_term
        if (result_term <= limit):
            if(result_term % 2 == 0):
                even_fibo_list.append(result_term)
        first_term = second_term
        second_term = result_term
    return even_fibo_list

limit = 4000000
even_fibo_list = even_fibo_series(limit)

print(sum(even_fibo_list))