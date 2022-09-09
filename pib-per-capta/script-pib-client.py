from factory.calculate_pib_per_capta_factory import calculatePibPerCaptaFactory

def main():
    calculate = calculatePibPerCaptaFactory.create_instance()
    
    print(calculate)

    calculate.load_file()
    calculate.load_uf_by_region()
    calculate.print_all_content()

main()