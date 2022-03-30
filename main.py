from data import Data
import argparse
import logging


def createLogger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    fileHandler = logging.FileHandler("finalproject.log", mode="w")
    fileHandler.setLevel(logging.DEBUG)
    logger.addHandler(fileHandler)
    logging.getLogger('matplotlib.font_manager').disabled = True
createLogger()

def main():
    data = Data()
    data.renameCols()
    data.mergeData()
    data.cleanData()
    data.buildModel()
    parser = argparse.ArgumentParser()
    logging.debug("Setting up parser")
    # allows user to select which plot to view
    parser.add_argument('-p', '--plot', dest='plot',
                        help='show this message and exit',
                        metavar='<plot option>',
                        choices=["data", 'regression', 'happinessbycountry',
                                 'disordersbycountry',
                                 'happinessbyyear', 'disordersbyyear'], type=str.lower)
    # allows user to select mean to view
    parser.add_argument('-m', '--mean', dest='mean',
                        help='show this message and exit',
                        metavar='<mean option>',
                        choices=['happinessbyyear', 'disorderbyyear',
                                 'happinessbycountry',
                                 'disorderbycountry'], type=str.lower)
    parser.add_argument("-s", "--sort", dest="sort",
                        # allow users to sort by happiness score and MH disorder prevalence
                        help="show this message and exit",
                        metavar="<sort option>",
                        choices=["happiness", "mhdisorders"], type=str.lower)
    args = parser.parse_args()
    if args.plot == "data":
        data.displayData()
    elif args.plot == 'regression':
        data.displayModel()
    elif args.plot == 'happinessbycountry':
        data.happinessByCountry()
    elif args.plot == 'disordersbycountry':
        data.mhdisorderByCountry()
    elif args.plot == 'happinessbyyear':
        data.happinessByYear()
    elif args.plot == 'disordersbyyear':
        data.mhdisorderByYear()

    if args.mean == 'happinessbyyear':
        data.avgHappinessYear()
    elif args.mean == 'disorderbyyear':
        data.avgDisorderYear()
    elif args.mean == 'happinessbycountry':
        data.avgHappinessCountry()
    elif args.mean == 'disorderbycountry':
        data.avgDisorderCountry()

    if args.sort == "happiness":
        data.sortHappiness()
    elif args.sort == "mhdisorders":
        data.sortDisorder()


if __name__ == "__main__":
    main()