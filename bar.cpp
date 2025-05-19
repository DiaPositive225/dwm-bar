#include <cstddef>
#include <cstdio>
#include <iostream>
#include <ostream>
#define PATH_BATT_CHARGE_NOW "/sys/class/power_supply/BAT0/subsystem/BAT0/charge_now"
#define PATH_BATT_CHARGE_FULL "/sys/class/power_supply/BAT0/subsystem/BAT0/charge_full"

int get_battery_state() {
	int charged_percent = 0;
	FILE *battery_charge_current;
	FILE *battery_charge_full;
	long unsigned int max_mAh = 0;
	long unsigned int remaining_mAh = 0;

	if (NULL == (battery_charge_current = fopen(PATH_BATT_CHARGE_NOW, "r"))) {
		fclose(battery_charge_current);
		return -1;
	}
	if (NULL == (battery_charge_full = fopen(PATH_BATT_CHARGE_FULL, "r"))) {
		fclose(battery_charge_current);
		fclose(battery_charge_full);
		return -1;
	}

	fscanf((FILE *)battery_charge_full, "%lu", &max_mAh);
	fscanf((FILE *)battery_charge_current, "%lu", &remaining_mAh);

	charged_percent = 100.00 * ((float) remaining_mAh / (float) max_mAh);
	return charged_percent;
}

int main() {
	int balls = get_battery_state();
	if (balls != -1) {
		std::cout << balls << std::endl;
	} else {
		std::cout << "Error" << std::endl;
	}
}
