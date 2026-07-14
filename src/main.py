from store import Products, StorageControl

produtos_data = [
    ("Notebook Acer", -4.800, 20, 8),
    ("Samsung Galaxy S26", 3.000, 12, 10),
    ("Smart TV LG 65 polegadas", 6.500, 4, 6),
]

resume = StorageControl()

for dados in produtos_data:
    try:
        produto = Products(*dados)
        resume.add(produto)
    except ValueError as e:
        print(f"Erro ao cadastrar '{dados[0]}': {e}")

print(resume.list_description())
print(resume.product_alert())
print(f"Valor total: R$ {resume.total_new():.3f}")