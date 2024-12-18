import webbrowser, os, sys
import time

#asci art text Command to search
print('   ******                                                           **')
time.sleep(0.1)
print(' **////**                                                         /**')
time.sleep(0.1)
print(' **    //   ******  **********  **********   ******   *******      /**')
time.sleep(0.1)
print('/**        **////**//**//**//**//**//**//** //////** //**///**  ******')
time.sleep(0.1)
print('/**       /**   /** /** /** /** /** /** /**  *******  /**  /** **///**')
time.sleep(0.1)
print('//**    **/**   /** /** /** /** /** /** /** **////**  /**  /**/**  /**')
time.sleep(0.1)
print(' //****** //******  *** /** /** *** /** /**//******** ***  /**//******')
time.sleep(0.1)
print('  //////   //////  ///  //  // ///  //  //  //////// ///   //  ////// ')
time.sleep(0.1)
print("")
print("")
print(' ******  ******          ')
time.sleep(0.1)
print('///**/  **////**           ')
time.sleep(0.1)
print('  /**  /**   /**             ')
time.sleep(0.1)
print('  /**  /**   /**                       ')
time.sleep(0.1)
print('  //** //******                            ')
time.sleep(0.1)
print('   //   //////                  ')
time.sleep(0.1)
print("")
print("")
print('********                                  **              ')
time.sleep(0.1)
print(' **//////                                  /**           ')
time.sleep(0.1)
print('/**         *****   ******   ******  ***** /**          ')
time.sleep(0.1)
print('/********* **///** //////** //**//* **///**/******     ')
time.sleep(0.1)
print('////////**/*******  *******  /** / /**  // /**///**   ')
time.sleep(0.1)
print('       /**/**////  **////**  /**   /**   **/**  /**  ')
time.sleep(0.1)
print(' ******** //******//********/***   //***** /**  /** ')
time.sleep(0.1)
print('////////   //////  //////// ///     /////  //   // ')
time.sleep(0.1)

urlOrNo = input('Url or Search:') #get the user input for if they want to do a search or go to a domain

urlOrNoCap = urlOrNo.upper() #set urlOrNo to be all capitalized

if urlOrNoCap == 'URL':
    search = input('URL:') #get the user input for a url
    url = 'https://{}'.format(search) #set url equal to the search variable
if urlOrNoCap == 'SEARCH':
    search = input("Google Search:") #get the user input for a google search
    url = "https://www.google.com/search?q={}".format(search) #format the url for a normal google search


webbrowser.open(url) #Open the default browser with the url
