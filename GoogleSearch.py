import webbrowser, os, sys
import time

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

urlOrNo = input('Url or Search:')

urlOrNoCap = urlOrNo.upper()

if urlOrNoCap == 'URL':
    search = input('URL:')
    url = 'https://{}'.format(search)

    
if urlOrNoCap == 'SEARCH':
    search = input("Google Search:")
    url = "https://www.google.com/search?q={}".format(search)


#print("To use this tool simply type what you want to search below")

#search = input("Google Search:")


#url = "https://www.google.com/search?q={}".format(search)

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

#chrome_path = '/usr/lib/chromium-browser/chromium-browser'
webbrowser.get(chrome_path).open(url)