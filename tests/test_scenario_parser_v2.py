__author__ = "Cameron Summers"

from tidepool_data_science_simulator.makedata.scenario_parser_v2 import ScenarioParserV2
from tidepool_data_science_simulator.visualization.sim_viz import plot_sim_results
from tidepool_data_science_metrics.glucose.glucose import blood_glucose_risk_index


def test_is_scenario_parser_smoking(test_config_v2_path):

    parser = ScenarioParserV2(test_config_v2_path)
    sims = parser.get_sims()

    results = {}
    for sim in sims:
        sim.run()
        results_df = sim.get_results_df()
        results[sim.name] = results_df

        results_df["bg"][results_df["bg"] < 0] = 1.0
        lbgi, hbgi, brgi = blood_glucose_risk_index(results_df["bg"])
        print(sim.name, "LBGI:", lbgi, "HBGI:", hbgi, "BRGI:", brgi)

    plot_sim_results(results)


if __name__ == "__main__":

    test_path = "../scenario_configurations/tidepool_risk/risks/TLR-684/Simulation-Configuration-TLR-684_Resistant_Profile.json"
    test_is_scenario_parser_smoking(test_path)
