from abc import ABC, abstractmethod
# Інтерфейс стратегії
class DeliveryStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, weight: float) -> float:
        pass
# Конкретна стратегія: Наземна доставка
class GroundDelivery(DeliveryStrategy):
    def calculate_cost(self, weight: float) -> float:
        return weight * 5.5
# Конкретна стратегія: Авіадоставка
class AirDelivery(DeliveryStrategy):
    def calculate_cost(self, weight: float) -> float:
        return weight * 20.0
# Контекст, який використовує стратегію
class Order:
    def __init__(self, weight: float, delivery_strategy: DeliveryStrategy):
        self.weight = weight
        self.delivery_strategy = delivery_strategy

    def set_strategy(self, delivery_strategy: DeliveryStrategy):
        self.delivery_strategy = delivery_strategy

    def calculate_total(self) -> float:
        return self.delivery_strategy.calculate_cost(self.weight)
# Використання коду
if __name__ == "__main__":
    package_weight = 10.5
    # Створення замовлення з наземною доставкою
    order = Order(package_weight, GroundDelivery())
    print(f"Вартість наземної доставки: {order.calculate_total()} грн")
    # Зміна стратегії на авіадоставку під час виконання
    order.set_strategy(AirDelivery())
    print(f"Вартість авіадоставки: {order.calculate_total()} грн")

