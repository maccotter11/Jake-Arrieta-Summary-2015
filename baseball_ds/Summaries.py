import pandas as pd

CSV = "/Users/mason_cotter/Desktop/python_projects/baseball_ds/Jake_Arrieta_CyYoung.csv"

class PitchSummary:
    """
    Creates a pitcher summary from a downloaded Baseball Savant csv.

    Pitch name, count, pitch_freq, avg_relsease velo, avg_effective_speed, avg_release_spin.
    """
    

    @classmethod
    def pitch_L(self, x, df):
        """
        Calculates the number of a particular pitch trown to left handed batters.
        """
        my_dict = {}
        count = 0
        for item in x:
            item = str(item)
            for i in range(len(df["pitch_name"])):
                if df["pitch_name"][i] == item and df["stand"][i] == "L":
                    count += 1
            my_dict[item] = count
        return my_dict

    @classmethod
    def pitch_R(self, x, df):
        """
        Calculates the number of a particulat pitch trown to right handed batters.
        """
        my_dict = {}
        count = 0
        for item in x:
            item = str(item)
            for i in range(len(df["pitch_name"])):
                if df["pitch_name"][i] == item and df["stand"][i] == "R":
                    count += 1
            my_dict[item] = count
        return my_dict
        
        
        x = str(x)
        count = 0
        for i in range(len(df["pitch_name"])):
            if df["pitch_name"][i] == x and df["stand"][i] == "R":
                count += 1
        return count

    def __init__(self, CSV):
        self.CSV = CSV

        df = pd.read_csv(CSV)

        # Creates the dataframe pitch_data
        self.pitch_data = df.groupby("pitch_name")["release_speed"].mean().reset_index()

        # creates a dataframe called pitch_usage which tells each pitches usage frequency
        self.pitch_usage = df["pitch_name"].value_counts(normalize=True).reset_index()

        # renames columns of pitch_usage
        self.pitch_usage.columns = ["pitch_name", "pitch_frequency"]

        # merges pitch_data and pitch_usage
        self.pitch_data = pd.merge(self.pitch_data, self.pitch_usage)

        self.RIGHT = self.pitch_R(
            [
                "4-Seam Fastball", 
                "Changeup",
                "Curveball",
                "Intentional Ball",
                "Sinker",
                "Slider",
            
            ], 
            df
        )
        self.LEFT = self.pitch_L(
            [
                "4-Seam Fastball",
                "Changeup",
                "Curveball",
                "Intentional Ball",
                "Sinker",
                "Slider",
            ],
            df,
        )
    
    pitcher_summary = PitchSummary(CSV)

    pitch_LR = {
        "VS L": [
            pitcher_summary.LEFT["4-Seam Fastball"],
            pitcher_summary.LEFT["Changeup"],
            pitcher_summary.LEFT["Curveball"],
            pitcher_summary.LEFT["Intentional Ball"],
            pitcher_summary.LEFT["Sinker"],
            pitcher_summary.LEFT["Slider"],
        ],
        "VS R": [
            pitcher_summary.RIGHT["4-Seam Fastball"]
            pitcher_summary.RIGHT["Changeup"]
            pitcher_summary.RIGHT["Curveball"]
            pitcher_summary.RIGHT["Intentional Ball"]
            pitcher_summary.RIGHT["Sinker"]
            pitcher_summary.RIGHT["Slider"]
        ],
    }

    pitch_LR_1 = pd.DataFrame(pitch_LR)

    pitch_data = pd.merge(
        pitcher_summary.pitch_data,
        pitch_LR_1,
        left_index=True,
        right_index=True,
        suffixes=("", "_dup"),
    )

print(pitch_data)


