import enum


class UserStatus(enum.Enum):
    Student = "student"
    Worker = "worker"
class User: ## конструктор класса
    name: str ## свойство
    age: int
    status: UserStatus
    items: list[str]

    ##функция создает новый экземпляр определенного класса
    def __init__(self, name, age, status, items):
        ## self - указывает на саму себя, в ней будет экземпляр текущего класса (не всех экземпляров класса)
        ## иницииализруем класс
        self.name = name
        self.age = int(age)
        self.status = UserStatus(status)
        self.items = items

    def is_adult(self) -> bool: ## проверка свойства пользователя
        return self.age >= 18

    @classmethod
    def from_csv(cls, user_dict):
        return cls(name=user_dict["name"],
                   age=user_dict["age"],
                   status=user_dict["status"],
                   items=user_dict["items"])


class Worker(User):
    pass


if __name__ == '__main__':
    oleg = User(name="Oleg", age=18, status="student", items=[])
    olga = User(name="Olga", age=20, status="student", items=[])
    ##assert oleg.age == 18
    assert oleg.is_adult() is True
    print()