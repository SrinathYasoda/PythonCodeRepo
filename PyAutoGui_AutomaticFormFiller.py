import pyautogui,time
nameField=(648,319)
submitButton=(651,817)
submitButtonColor=(75,141,249)
submitAnotherLink=(760,224)

formData=[{'name':'Alice','fear':'eavesdroppers','source':'wand','robocop':4,'comments':'Tell Bob I said hi.'},
{'name':'Bob','fear':'bees','source':'amulet','robocop':4,'comments':'n/a'},
{'name':'Carol','fear':'puppets','source':'crystal ball','robocop':1,'comments':'Please take the puppets out of the break room.'},
{'name':'Alex Murphy','fear':'ED-209','source':'money','robocop':5,'comments':'Protect the innocent. Uphold the law.'}]

pyautogui.PAUSE=0.5

for person in formData:
    print('>5 seconds to load the data')
    time.sleep(5)
    #wait to load the page
    #while not pyautogui.pixelMatchesColor(submitButtonColor[0],submitButtonColor[1],submitButtonColor):
     #   time.sleep(0.5)

    print('Entering name %s info' %(person['name']))
    pyautogui.click(nameField[0],nameField[1])

    pyautogui.typewrite(person['name']+'\t')
    pyautogui.typewrite(person['fear']+'\t')

    if person['source'] == 'wand':
        pyautogui.typewrite(['down','\t'])
    elif person['source'] == 'amulet':
        pyautogui.typewrite(['down','down','\t'])
    elif person['source'] == 'crystal ball':
        pyautogui.typewrite(['down','down','down','\t'])
    elif person['source'] == 'money':
        pyautogui.typewrite(['down','down','down','down','\t'])


    if person['robocop'] == '1':
        pyautogui.typewrite([' ','\t'])
    elif person['robocop'] == '2':
        pyautogui.typewrite(['right','\t'])
    elif person['robocop'] == '3':
        pyautogui.typewrite(['right','right','\t'])
    elif person['robocop'] == '4':
        pyautogui.typewrite(['right','right','right','\t'])
    elif person['robocop'] == '5':
        pyautogui.typewrite(['right','right','right','right','\t'])

    #Entering comments
    pyautogui.typewrite(person['comments'],'\t')
    #Clicking on Submit button
    pyautogui.press('enter')

    #Wait until the page has loaded
    print ('Clicked Submit.')
    time.sleep(5)

    pyautogui.click(submitAnotherLink[0],submitAnotherLink[1])



