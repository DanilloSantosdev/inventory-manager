class StorageControl:
    """
    Classe para controlar tudo o que ocorre na gestão do estoque.
    """
    def __init__(self):
        self.enter = []

    def add(self, product) -> None:
        self.enter.append(product)

    def delete(self, product) -> None:
        self.enter.remove(product)   
    
    def find(self, item: str):
        for product in self.enter:
            if product.description == item:
                print(product)
                return 
        print(f"{item} not found")

    def product_alert(self) -> list:
        alert = [product for product in self.enter if product.storage < product.limite]
        return alert

    def list_description(self) -> list:
        return "\n".join(product.description for product in self.enter)

    def total_new(self) -> float:
        return sum(product.price * product.storage for product in self.enter)

    def __str__(self) -> str:
        return "\n".join(str(enter) for enter in self.enter)