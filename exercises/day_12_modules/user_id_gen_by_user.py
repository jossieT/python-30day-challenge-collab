import random_id_generator as rid_gen
def user_id_gen_by_user():
    num1 = int(input("How random id's do you want to generate:"))
    num2 = int(input("What is length of your random id:"))
    print("#Output:")
    i = 0
    while i <= num1:
        print(f'#{rid_gen.random_user_id(num2)}')
        i += 1




user_id_gen_by_user()