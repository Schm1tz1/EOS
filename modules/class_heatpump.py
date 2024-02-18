import json
from datetime import datetime, timedelta, timezone
import numpy as np
from pprint import pprint

# Lade die .npz-Datei beim Start der Anwendung
class Waermepumpe:
    def __init__(self, max_heizleistung):
        self.max_heizleistung = max_heizleistung

    def cop_berechnen(self, aussentemperatur):
        cop = 3.0 + (aussentemperatur-0) * 0.1
        return max(cop, 1)


    def heizleistung_berechnen(self, aussentemperatur):
        #235.092 kWh + Temperatur * -11.645
        heizleistung = (((235.0) + aussentemperatur*(-11.645))*1000)/24.0
        heizleistung = min(self.max_heizleistung,heizleistung)
        return heizleistung

    def elektrische_leistung_berechnen(self, aussentemperatur):
        heizleistung = self.heizleistung_berechnen(aussentemperatur)
        cop = self.cop_berechnen(aussentemperatur)
        return heizleistung / cop

    def simulate_24h(self, temperaturen):
        leistungsdaten = []
        for temp in temperaturen:
            elektrische_leistung = self.elektrische_leistung_berechnen(temp)
            leistungsdaten.append(elektrische_leistung)
        return leistungsdaten







# Beispiel für die Verwendung der Klasse
if __name__ == '__main__':
        max_heizleistung = 5000  # 5 kW Heizleistung
        start_innentemperatur = 15
        isolationseffizienz = 0.8
        gewuenschte_innentemperatur = 20
        wp = Waermepumpe(max_heizleistung)
        
        print(wp.cop_berechnen(-10)," ",wp.cop_berechnen(0), " ", wp.cop_berechnen(10))
        # 24 Stunden Außentemperaturen (Beispielwerte)
        temperaturen = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -5, -2, 5]

        # Berechnung der 24-Stunden-Leistungsdaten
        leistungsdaten = wp.simulate_24h(temperaturen)

        print(leistungsdaten)
