from django.apps import AppConfig


class RentalConfig(AppConfig):
    name = 'rental'

    def ready(self) -> None:
        import rental.signals
