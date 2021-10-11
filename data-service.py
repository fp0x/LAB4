from dataclasses import dataclass

@dataclass
class TypeOfMainAssets:
    code: int
    name: str

@dataclass
class MoveOfMainAssets:
    name: str
    data: float
    code: int
    remainder: float
    received: float
    output: float

type_array = []
type_array.append(TypeOfMainAssets(100, "Бесарабський ринок"))
type_array.append(TypeOfMainAssets(200, "Житній ринок"))
type_array.append(TypeOfMainAssets(300, "Володимирський ринок"))
move_array = []
move_array.append(MoveOfMainAssets("Бесарабський ринок", "02.11.2016", 100, 45.00, 50.00, 70.00))
move_array.append(MoveOfMainAssets("Житній ринок", "02.11.2016", 200, 35.00, 30.00, 50.00))
move_array.append(MoveOfMainAssets("Володимирський ринок", "02.11.2016", 300, 35.00, 30.00, 45.00))
move_array.append(MoveOfMainAssets("Бесарабський ринок", "14.11.2016", 100, 45.00, 45.00, 60.00))
move_array.append(MoveOfMainAssets("Житній ринок", "14.11.2016", 200, 40.00, 40.00, 50.00))
move_array.append(MoveOfMainAssets("Володимирський ринок", "14.11.2016", 300, 35.00, 35.00, 45.00))
move_array.append(MoveOfMainAssets("Бесарабський ринок", "22.11.2016", 100, 40.00, 40.00, 60.00))
move_array.append(MoveOfMainAssets("Житній ринок", "22.11.2016", 200, 40.00, 40.00, 50.00))
move_array.append(MoveOfMainAssets("Володимирський ринок", "22.11.2016", 300, 40.00, 40.00, 60.00))

def printMoveOfMainAssets(moveOfMainAssets):
    '''printMoveOfMainAssets function prints
    "Статистичні дані про ринкові ціни"
    with names and values'''

    print ("Код: {code}, Найменування ринку: {name}, Дата: {data}, Картопля,грн.: {remainder}, Капуста,грн.: {received} Цибуля, грн: {output}"
          .format(name=moveOfMainAssets.name, code=moveOfMainAssets.code, remainder=moveOfMainAssets.remainder,
                  received=moveOfMainAssets.received, output=moveOfMainAssets.output, data=moveOfMainAssets.data)) 
for data in move_array:
    printMoveOfMainAssets(data)

def printTypeOfMainAssets(typeOfMainAssets):
    '''printTypeOfMainAssets function prints
    "Довідник ринків"
    with names and values'''

    print("Код: {code}, Найменування ринку: {name}"
        .format(code=typeOfMainAssets.code, name=typeOfMainAssets.name))

for data in type_array:
    printTypeOfMainAssets(data)