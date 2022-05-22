from colorama import init
from termcolor import colored


class TextLabel:
    init()  # colorama init
    inputCoin = colored("Input coin: ", "red")
    inputAmount = colored("Input amount of coins to buy: ", "red")
    inputPercent = colored("Input percent for hedging orders: ", "red")
    notice_1 = f"""NOTICE:\nThe trigger price of hedging short/long orders
will be higher/lower by percent% than
the entry price of the last open position."""

    inputLabel = colored(">>>Input: ", "yellow")
    aboutDivider = colored(">>>>>>>>>>>>>>>>>> ABOUT <<<<<<<<<<<<<<<<<<", "red")
    noticeDivider = colored(">>>>>>>>>>>>>>>>> NOTICE <<<<<<<<<<<<<<<<<", "red")
    menuDivider = colored(">>>>>>>>>>>>>>>>>>> MENU <<<<<<<<<<<<<<<<<<<", "magenta")
    finishDivider = colored("\n>>>>>>>>>>>>>>>>>> FINISH <<<<<<<<<<<<<<<<<<\n", "magenta")
    gameOverDivider = (colored("\n>>>>>>>>>>>>>>>>>> GAME OVER <<<<<<<<<<<<<<<<<<\n", "magenta"))
    angleDivider = colored(">>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<", "red")
    starDivider = "*********************************"
    longDashDivider = "\n---------------------------------------------------"
    shortDashDivider = "-------------"
    about = (aboutDivider
             + """\nThe main idea of this program is
            to open positions in the futures market
            and almost immediately hedges with
            opposite orders, placed with a trigger
            price, which is lower/higher by percent
            than the entry price of the position.
            Also, you could quickly change direction 
            of the open position and close and cancel
            all hedging orders.\n"""
             + aboutDivider)

    menu = (menuDivider
            + longDashDivider
            + colored("\n--- (s) - open short position", "red")
            + colored("\n--- (l) - open long position", "green")
            + colored("\n--- (cs) - close short position", "red")
            + colored("\n--- (cl) - close long position", "green")
            + colored("\n--- (sh) - ", "red")
            + colored("both: ", "yellow")
            + colored("short position + ", "red")
            + colored(f"hedging long order", "green")
            # + f"\nNotice: Trigger price of the hedging long order\nwill be higher by percent% than the entry price\nof the open position."
            + colored("\n--- (lh) - ", "green")
            + colored("both: ", "yellow")
            + colored("long position + ", "green")
            + colored(f"hedging short order", "red")
            # + f"\nNotice: Trigger price of the hedging short order\nwill be lower by percent% than the entry price\nof the open position."
            + colored(f"\n--- (hgs) - hedging short order by market price", "red")
            # + f"\nNotice: Trigger price of the short order\nwill be lower by percent% than\nthe current market price."
            + colored(f"\n--- (hgl) - hedging long order by market price", "green")
            # + "\nNotice: Trigger price of the long order\nwill be higher by percent% than\nthe current market price."
            + colored("\n--- (co) - cancel all open orders ", "magenta")
            + colored("\n--- (ns) - re-new short + hedging long", "blue")
            + colored("\n--- (nl) - re-new long + hedging short", "blue")
            + colored("\n--- (f) - finish", "magenta")
            + longDashDivider)

    shortPosition = (colored(" SHORT", "red") + " position")
    longPosition = (colored(" LONG", "green") + " position")
    shortHedge = (colored(" SHORT + hedge LONG", "red") + " position")
    longHedge = (colored(" LONG + hedge SHORT", "green") + " position")
    shortPositionClosed = (colored("***** SHORT position closed *****", "blue"))
    longPositionClosed = (colored("***** LONG position closed *****", "blue"))
    hedgeLongOrder = (colored("***** hedge LONG order placed *****", "blue"))
    hedgeShortOrder = (colored("***** hedge SHORT order placed *****", "blue"))
    ordersCanceled = (colored("***** all ORDERS canceled *****", "blue"))
    renewShortLong = (colored("***** re-new SHORT + hedge LONG position *****", "blue"))
    renewLongShort = (colored("***** re-new LONG + hedge SHORT position *****", "blue"))

    continueText = (colored("\nContinue: ", "yellow")
                    + colored("(y)-yes", "red")
                    + colored(" or ", "yellow")
                    + colored("(n)-no...?", "red"))

    def printTextAbout(self):
        print(self.about)

    def printInfoText(self, text):
        print(self.starDivider)
        print(text)
        print(self.starDivider)