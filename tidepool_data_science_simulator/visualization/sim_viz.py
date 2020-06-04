__author__ = "Cameron Summers"

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.style as style

style.use("seaborn-poster")  # sets the size of the charts
style.use("ggplot")


def plot_sim_results(all_results):

    # ==== TMP ====
    # TODO - This is a placeholder for dev. Replace with viz tools module.
    fig, ax = plt.subplots(3, 1, figsize=(16, 20))
    for sim_id, ctrl_result_df in all_results.items():

        ax[0].plot(ctrl_result_df["bg"], label="{} {}".format("bg", sim_id))
        ax[0].set_title("BG Over Time")
        ax[0].set_xlabel("Time (5min)")
        ax[0].set_ylabel("BG (mg/dL)")
        ax[0].set_ylim((0, 400))
        median = ctrl_result_df["bg"].median()
        std = round(ctrl_result_df["bg"].std())
        # ax[0].axhline(median, label="BG Median {}".format(median), color="green")
        # ax[0].axhline(median + std, label="BG Std {}".format(std), color="green")
        # ax[0].axhline(median - std, label="BG Std {}".format(std), color="green")
        ax[0].legend()

        ax[1].plot(ctrl_result_df["sbr"], label="{} {}".format("sbr", sim_id))
        ax[1].set_title("Schedule Basal Rate Over Time")
        ax[1].set_ylabel("Insulin (U)")
        ax[1].set_xlabel("Time (5 mins)")
        ax[1].plot(ctrl_result_df["temp_basal"], label="{} {}".format("tmp_br", sim_id))
        ax[1].set_title("Temp Basal Rate")
        ax[1].plot(ctrl_result_df["bolus"], label="{} {}".format("bolus", sim_id))
        ax[1].set_ylim((0, 3))
        ax[1].legend()

        ax[2].plot(ctrl_result_df["carb"], label="{} {}".format("carb", sim_id))
        ax[2].set_title("Carb Events")
        ax[2].set_ylabel("Carbs (g)")
        ax[2].set_xlabel("Time (5 mins)")
        ax[2].set_ylim((0, 40))
        ax[2].legend()

        print(
            "Patient Bg min {} max {}".format(
                ctrl_result_df["bg"].min(), ctrl_result_df["bg"].max()
            )
        )

        log_bg = np.log(ctrl_result_df["bg"])
        geo_mean = np.mean(log_bg)
        geo_var = np.var(log_bg)

        # counts, bins, patches = ax[2].hist(log_bg, bins=50, label="{} {} {}".format("bg", vp_name, ctr_name), alpha=0.1)
        # # ax[2].set_xscale("log")
        # ax[2].set_xticklabels(np.exp(bins).astype(int))
        # ax[2].axvline(geo_mean, label="{} {} {}".format("Geo Mean", vp_name, ctr_name))
        # ax[2].set_xlabel("BG (mg/dL)")
        # ax[2].legend()
        #
        # counts, bins, patches = ax[3].hist(ctrl_result_df['bg'], bins=50, label="{} {}".format("bg", sim_id), alpha=0.1)
        # ax[3].set_xscale("log")
        # ax[3].set_title("BG Distribution")
        # ax[3].set_xlabel("BG (mg/dL)")
        # ax[3].legend()

    plt.show()
