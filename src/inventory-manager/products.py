class Products:
    """
    Classe para controlar os produtos de forma organizada
    """
    def __init__(self, description: str, price: float, storage: int, limite: int):
        self.description = description
        self.price = price
        self.storage = storage
        self.limite = limite

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Não é permitido valor negativo")
        self._price = value

    def entrada(self, quantidade: int) -> None:
        self.storage = quantidade #funcionando

    def saida(self, quantidade: int) -> None:
        if quantidade > self.storage:
            print("Estoque insuficiente")
            return
        self.storage -= quantidade #funcionando

    def __repr__(self) -> str:
        return f"Produto('{self.description}', R${self._price:.2f}, estoque={self.storage})"

    def alert(self) -> None:
        if self.storage < self.limite: 
            print(f"ALERTA!!! Produto {self.description}: Estoque baixo")
    

    def __str__(self) -> str:
        """ Exibir infos do produto ao cliente """
        return f"Produto: {self.description} - Valor: R$ {self._price:.3f} | Quantidade: {self.storage}"