from singleton.calculate_pib_per_capta_singleton import CalculatePibPerCaptaSingleton


class calculatePibPerCaptaFactory:
    @classmethod
    def create_instance(self):
        return CalculatePibPerCaptaSingleton.get_instance()
