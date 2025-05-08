from barCodeScanner import BarCodeScanner
from databaseProxy import DatabaseProxy

scanner = BarCodeScanner()
db_proxy = DatabaseProxy()


try:
    barcode = scanner.read_barcode()
    part_info = db_proxy.read_part_information(barcode)

    print(f"Part Information: {part_info}")
    print(f"Part Information: {part_info.weight}")
except ValueError as e:
    print(f"Error: {e}")