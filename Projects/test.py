import file_access as fa
data = fa.load_data()
degree = data["MYC/5434/10"]["degrees"]
print(degree)