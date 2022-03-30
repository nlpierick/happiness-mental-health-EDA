import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import matplotlib.pyplot as plt
import logging

def createLogger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    fileHandler = logging.FileHandler("finalproject.log", mode="w")
    fileHandler.setLevel(logging.DEBUG)
    logger.addHandler(fileHandler)
    logging.getLogger('matplotlib.font_manager').disabled = True
createLogger()

class Data():
    def __init__(self):
    # create dataframe for World Happiness Report dataset and include relevant columns
        self.WHR_Data = pd.read_csv("DataPanelWHR2021C2.csv",
                        usecols=["Country name", "year",
                                "Life Ladder"])
    # create dataframe for Our World in Data mental health dataset and include relevant columns
        self.MH_Data = pd.read_csv(
                        "share-with-mental-and-substance-disorders.csv",
                        usecols=["Entity", "Year",
                        "Prevalence - Mental disorders - Sex: Both - Age: Age-standardized (Percent)"])
        self.avgHappinessByYear = None
        self.avgHappinessByCountry = None
        self.avgDisorderByYear = None
        self.avgDisorderByCountry = None
        logging.debug("Creating dataframes for datasets")
    def renameCols(self):
    # rename columns of data
        self.WHR_Data.rename(columns={"Country name": "Country", "year": "Year",
                                    "Life Ladder": "Happiness Score"},
                                    inplace=True)
        self.MH_Data.rename(columns={"Entity": "Country",
                            "Prevalence - Mental disorders - Sex: Both - Age: Age-standardized (Percent)":
                            "MH Disorder Prevalence"},
                            inplace=True)
        logging.debug("Renaming columns")
    def mergeData(self):
    # merge dataframes
        self.mergedData = pd.merge(self.WHR_Data, self.MH_Data,
                        on=["Country", "Year"], how="left")
        logging.debug("Merging WHR_Data and MH_Data dataframes")
    def cleanData(self):
    # remove rows with NaN
        self.data = self.mergedData.dropna()
    # output clean data to CSV
        self.data.to_csv("World_Happiness_Mental_Health_Data.csv", index=False)
        logging.debug("Cleaning data and outputting to CSV")
    def buildModel(self):
    # build model
        X = np.array(self.data[["Happiness Score"]]).reshape(-1, 1)
        Y = np.array(self.data[["MH Disorder Prevalence"]]).reshape(-1, 1)
        X_train, self.X_test, Y_train, self.Y_test = train_test_split(X, Y,
        test_size=0.20,
        random_state=0)
        self.model = LinearRegression()
        self.model.fit(X_train, Y_train)
        predictions = self.model.predict(self.X_test)
        print("Model Evaluation Metrics:")
        # r squared, coefficient of determination
        coeffDetermination = self.model.score(self.X_test, self.Y_test)
        print("Coefficient of Determination: " + str(
        round(coeffDetermination, 3)))
        # mean squared error
        meanSquaredError = metrics.mean_squared_error(self.Y_test, predictions)
        print("Mean Squared Error: " + str(round(meanSquaredError, 3)))
        #mean absolute error
        meanAbsError = metrics.mean_absolute_error(self.Y_test, predictions)
        print("Mean Absolute Error: " + str(round(meanAbsError, 3)))
        #mean root error
        rootSqError = np.sqrt(metrics.mean_squared_error(self.Y_test, predictions))
        print("Root Mean Squared Error: " + str(round(rootSqError, 3)))
        logging.debug(
        "Building linear regression model and calculating metrics")
    def displayData(self):
    # display original data
        plt.scatter(self.data["Happiness Score"],
        self.data["MH Disorder Prevalence"], color="purple")
        plt.title("Data: Happiness Score vs. Mental Health Disorder Prevalence")
        plt.xlabel("Happiness Score")
        plt.ylabel("MH Disorder Prevalence")
        plt.show()
        logging.debug("Creating plot")
    def displayModel(self):
    # display model data
        Y_pred = self.model.predict(self.X_test)
        plt.scatter(self.X_test, self.Y_test, color="purple")
        plt.plot(self.X_test, Y_pred, color="grey", linewidth=2)
        plt.title(
        "Model: Happiness Score vs. Mental Health Disorder Prevalence")
        plt.xlabel('Happiness Score')
        plt.ylabel('MH Disorder Prevalence')
        plt.show()
        logging.debug("Creating plot")
    def happinessByCountry(self):
    # produces a graph of happiness scores vs country
        WHR_array = np.array(self.WHR_Data)
        countries_array = WHR_array[:, 0]
        happiness_array = WHR_array[:, 2]
        plt.scatter(countries_array, happiness_array, color="purple")
        plt.title("Happiness Score by Country")
        plt.axis([0, 24, 0, 50])
        plt.ylabel('Happiness Score')
        plt.xlabel('Countries')
        plt.xticks(rotation=90)
        plt.ylim([0, 10])
        plt.tight_layout()
        plt.show()
        logging.debug("Creating plot")
    def mhdisorderByCountry(self):
    # produces a graph of mh discords vs country
        MH_array = np.array(self.MH_Data)
        countries_array2 = MH_array[:, 0]
        mhdisorder_array = MH_array[:, 2]
        plt.scatter(countries_array2, mhdisorder_array, color="purple")
        plt.title("MH Disorder Prevalence by Country")
        plt.axis([0, 24, 0, 50])
        plt.ylabel('MH Disorder')
        plt.xlabel('Countries')
        plt.xticks(rotation=90)
        plt.ylim([0, 25])
        plt.tight_layout()
        plt.show()
        logging.debug("Creating plot")
    def happinessByYear(self):
    # produces a graph of happiness scores vs year
        WHR_byyear = np.array(self.WHR_Data)
        year_array = WHR_byyear[:, 1]
        float_year = year_array.astype(np.float64)
        happiness_array = WHR_byyear[:, 2]
        plt.scatter(year_array, happiness_array, color="purple")
        plt.title("Happiness Score by Year")
        plt.ylabel('Happiness Score')
        plt.xlabel('Year')
        plt.xticks(rotation=75)
        plt.xticks(float_year)
        plt.show()
        logging.debug("Creating plot")
    def mhdisorderByYear(self):
    # produces a graph of mh disorders vs year
        MH_byyear = np.array(self.MH_Data)
        year_array2 = MH_byyear[:, 1]
        float_year2 = year_array2.astype(np.float64)
        mhdisorder_array = MH_byyear[:, 2]
        plt.scatter(year_array2, mhdisorder_array, color="purple")
        plt.title("MH Disorder Prevalence by Year")
        plt.ylabel('MH Disorder Prevalence')
        plt.xlabel('Year')
        plt.xticks(rotation=75)
        plt.xticks(float_year2)
        plt.show()
        logging.debug("Creating plot")
    def avgHappinessYear(self):
    # average happiness by year
    #output to CSV
        self.avgHappinessByYear = (
        self.data.groupby("Year", as_index=False, sort=True)
                    ["Happiness Score"].mean())
        self.avgHappinessByYear.to_csv("Happiness_By_Year.csv", index= False)
        logging.debug("Calculating average happiness score by year")
    def avgHappinessCountry(self):
    # average happiness by country
    # output to CSV
        self.avgHappinessByCountry = (
        self.data.groupby("Country", as_index=False, sort=True)
                    ["Happiness Score"].mean())
        self.avgHappinessByCountry.to_csv("Happiness_By_Country.csv", index=False)
        logging.debug("Calculating average happiness score by country")
    def avgDisorderYear(self):
    # average MH disorder prevalence by year
    # output to CSV
        self.avgDisorderByYear = (
        self.data.groupby("Year", as_index=False, sort=True)
                    ["MH Disorder Prevalence"].mean())
        self.avgDisorderByYear.to_csv("MH_Disorder_By_Year.csv", index=False)
        logging.debug("Calculating average MH disorder prevalence by year")
    def avgDisorderCountry(self):
        # average MH disorder prevalence by country
        # output to CSV
        self.avgDisorderByCountry = (
            self.data.groupby("Country", as_index=False, sort=True)
            ["MH Disorder Prevalence"].mean())
        self.avgDisorderByCountry.to_csv("MH_Disorder_By_Country.csv", index=False)
        logging.debug("Calculating average MH disorder prevalence by country")
    def sortHappiness(self):
        # sort by happiness score
        # output to CSV
        self.sortedHappiness = self.data.sort_values(by=["Happiness Score"], ascending=False)
        self.sortedHappiness.to_csv("Sorted_By_Happiness.csv", index=False)
        logging.debug("Sorting by happiness score")
    def sortDisorder(self):
        # sort by MH disorder prevalence
        # output to CSV
        self.sortedDisorder = self.data.sort_values(by=["MH Disorder Prevalence"], ascending=False)
        self.sortedDisorder.to_csv("Sorted_By_MH_Disorder.csv", index=False)
        logging.debug("Sorting by MH disorder prevalence")