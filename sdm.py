# parts taken from https://github.com/nmakel/sdm_modbus

class SDM():
    model = "Generic"
    registers = {}

    stopbits = 1
    parity = "N"
    baud = 38400

class SDM72V2(SDM):

    def __init__(self, *args, **kwargs):
        self.model = "SDM72V2"
        self.baud = 9600

        self.registers = {
            "l1_voltage": (0x0000, 2, "L1 Voltage", "V", 1, 1, ""),
            "l2_voltage": (0x0002, 2, "L2 Voltage", "V", 1, 1, ""),
            "l3_voltage": (0x0004, 2, "L3 Voltage", "V", 1, 1, ""),
            "l1_current": (0x0006, 2, "L1 Current", "A", 1, 1, ""),
            "l2_current": (0x0008, 2, "L2 Current", "A", 1, 1, ""),
            "l3_current": (0x000a, 2, "L3 Current", "A", 1, 1, ""),
            "l1_power_active": (0x000c, 2, "L1 Power (Active)", "W", 1, 1, ""),
            "l2_power_active": (0x000e, 2, "L2 Power (Active)", "W", 1, 1, ""),
            "l3_power_active": (0x0010, 2, "L3 Power (Active)", "W", 1, 1, ""),
            "voltage_ln": (0x002a, 2, "L-N Voltage", "V", 1, 1, ""),
            "current_ln": (0x002e, 2, "L-N Current", "A", 1, 1, ""),
            "total_line_current": (0x0030, 2, "Total Line Current", "A", 1, 1, ""),
            "total_power": (0x0034, 2, "Total Power", "W", 1, 1, ""),
            "import_energy_active": (0x0048, 2, "Imported Energy (Active)", "kWh", 1, 1, "total_power"),
            "export_energy_active": (0x004a, 2, "Exported Energy (Active)", "kWh", 1, 1, "total_power"),
        }


class SDM72(SDM):

    def __init__(self, *args, **kwargs):
        self.model = "SDM72"
        self.baud = 9600

        self.registers = {
            "l1_voltage": (0x0000, 2, "L1 Voltage", "V", 1, 1, ""),
            "l2_voltage": (0x0002, 2, "L2 Voltage", "V", 1, 1, ""),
            "l3_voltage": (0x0004, 2, "L3 Voltage", "V", 1, 1, ""),
            "l1_current": (0x0006, 2, "L1 Current", "A", 1, 1, ""),
            "l2_current": (0x0008, 2, "L2 Current", "A", 1, 1, ""),
            "l3_current": (0x000a, 2, "L3 Current", "A", 1, 1, ""),
            "l1_power_active": (0x000c, 2, "L1 Power (Active)", "W", 1, 1, ""),
            "l2_power_active": (0x000e, 2, "L2 Power (Active)", "W", 1, 1, ""),
            "l3_power_active": (0x0010, 2, "L3 Power (Active)", "W", 1, 1, ""),
            "voltage_ln": (0x002a, 2, "L-N Voltage", "V", 1, 1, ""),
            "current_ln": (0x002e, 2, "L-N Current", "A", 1, 1, ""),
            "total_line_current": (0x0030, 2, "Total Line Current", "A", 1, 1, ""),
            "total_power": (0x0034, 2, "Total Power", "W", 1, 1, ""),
            "import_energy_active": (0x0048, 2, "Imported Energy (Active)", "kWh", 1, 1, "total_power"),
            "export_energy_active": (0x004a, 2, "Exported Energy (Active)", "kWh", 1, 1, "total_power"),
        }


class SDM120(SDM):

    def __init__(self, *args, **kwargs):
        self.model = "SDM120"
        self.baud = 2400

        self.registers = {
            "V": (0x0000, 2, "V", "V", 1, 1, ""),
            "current": (0x0006, 2, "Current", "A", 1, 1, ""),
            "power_active": (0x000c, 2, "Power (Active)", "W", 1, 1, ""),
            "import_energy_active": (0x0048, 2, "Imported Energy (Active)", "kWh", 1, 1, "power_active"),
            "export_energy_active": (0x004a, 2, "Exported Energy (Active)", "kWh", 1, 1, "power_active"),
            "total_demand_power_active": (0x0054, 2, "Total Demand Power (Active)", "W", 2, 1, ""),
            "import_demand_power_active": (0x0058, 2, "Import Demand Power (Active)", "W", 2, 1, ""),
            "export_demand_power_active": (0x005c, 2, "Export Demand Power (Active)", "W", 2, 1, ""),
            "total_demand_current": (0x0102, 2, "Total Demand Current", "A", 3, 1, ""),
            "total_energy_active": (0x0156, 2, "Total Energy (Active)", "kWh", 4, 1, "total_demand_power_active"),
        }


class SDM230(SDM):

    def __init__(self, *args, **kwargs):
        self.model = "SDM230"
        self.baud = 9600

        self.registers = {
            "V": (0x0000, 2, "V", "V", 1, 1, ""),
            "current": (0x0006, 2, "Current", "A", 1, 1, ""),
            "power_active": (0x000c, 2, "Power (Active)", "W", 1, 1, ""),
            "total_demand_power_active": (0x0054, 2, "Total Demand Power (Active)", "W", 2, 1, ""),
            "import_demand_power_active": (0x0058, 2, "Import Demand Power (Active)", "W", 2, 1, ""),
            "export_demand_power_active": (0x005c, 2, "Export Demand Power (Active)", "W", 2, 1, ""),
            "total_demand_current": (0x0102, 2, "Total Demand Current", "A", 3, 1, ""),
            "total_energy_active": (0x0156, 2, "Total Energy (Active)", "kWh", 4, 1, "total_demand_power_active"),
            "import_energy_active": (0x0048, 2, "Imported Energy (Active)", "kWh", 1, 1, "import_demand_power_active"),
            "export_energy_active": (0x004a, 2, "Exported Energy (Active)", "kWh", 1, 1, "export_demand_power_active"),
        }


class SDM630(SDM):

    def __init__(self, *args, **kwargs):
        self.model = "SDM630"
        self.baud = 9600

        self.registers = {
            "l1_voltage": (0x0000, 2, "L1 Voltage", "V", 1, 1, ""),
            "l2_voltage": (0x0002, 2, "L2 Voltage", "V", 1, 1, ""),
            "l3_voltage": (0x0004, 2, "L3 Voltage", "V", 1, 1, ""),
            "l1_current": (0x0006, 2, "L1 Current", "A", 1, 1, ""),
            "l2_current": (0x0008, 2, "L2 Current", "A", 1, 1, ""),
            "l3_current": (0x000a, 2, "L3 Current", "A", 1, 1, ""),
            "l1_power_active": (0x000c, 2, "L1 Power (Active)", "W", 1, 1, ""),
            "l2_power_active": (0x000e, 2, "L2 Power (Active)", "W", 1, 1, ""),
            "l3_power_active": (0x0010, 2, "L3 Power (Active)", "W", 1, 1, ""),
            "voltage_ln": (0x002a, 2, "L-N Voltage", "V", 1, 1, ""),
            "current_ln": (0x002e, 2, "L-N Current", "A", 1, 1, ""),
            "total_line_current": (0x0030, 2, "Total Line Current", "A", 1, 1, ""),
            "total_power_active": (0x0034, 2, "Total Power (Active)", "W", 1, 1, ""),
            "import_energy_active": (0x0048, 2, "Imported Energy (Active)", "kWh", 1, 1, "total_power_active"),
            "export_energy_active": (0x004a, 2, "Exported Energy (Active)", "kWh", 1, 1, "total_power_active"),
            "total_current": (0x0052, 2, "Total Current", "A", 2, 1, ""),
            "l1_import_energy_active": (0x015a, 2, "L1 Import Energy (Active)", "kWh", 4, 1, "l1_power_active"),
            "l2_import_energy_active": (0x015c, 2, "L2 Import Energy (Active)", "kWh", 4, 1, "l2_power_active"),
            "l3_import_energy_active": (0x015e, 2, "L3 Import Energy (Active)", "kWh", 4, 1, "l3_power_active"),
            "l1_export_energy_active": (0x0160, 2, "L1 Export Energy (Active)", "kWh", 4, 1, "l1_power_active"),
            "l2_export_energy_active": (0x0162, 2, "L2 Export Energy (Active)", "kWh", 4, 1, "l2_power_active"),
            "l3_export_energy_active": (0x0164, 2, "L3 Export Energy (Active)", "kWh", 4, 1, "l3_power_active"),
            "l1_energy_active": (0x0166, 2, "L1 Total Energy (Active)", "kWh", 4, 1, "total_power_active"),
            "l2_energy_active": (0x0168, 2, "L2 Total Energy (Active)", "kWh", 4, 1, "total_power_active"),
            "l3_energy_active": (0x016a, 2, "L3 Total Energy (Active)", "kWh", 4, 1, "total_power_active"),
        }
