#Python MemeCreationBot: creates a meme based on user input and imgflip.com internet connection
import discord
import random
from discord.ext import commands
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#list of lists for each meme; each list's elements are as follows: ["link to meme",number of inputs for meme,"name of meme"] 
drake = ["https://imgflip.com/memegenerator/Drake-Hotline-Bling",2,"Drake-Hotline-Bling"]
distract = ["https://imgflip.com/memegenerator/Distracted-Boyfriend",3,"Distracted-Boyfriend"]
twobut = ["https://imgflip.com/memegenerator/Two-Buttons",2,"Two-Buttons"]
change = ["https://imgflip.com/memegenerator/Change-My-Mind",2,"Change-My-Mind"]
ball = ["https://imgflip.com/memegenerator/Running-Away-Balloon",5,"Running-Away-Balloon"]
leftex = ["https://imgflip.com/memegenerator/Left-Exit-12-Off-Ramp",3,"Left-Exit-12-Off-Ramp"]
uno = ["https://imgflip.com/memegenerator/UNO-Draw-25-Cards",2,"UNO-Draw-25-Cards"]
sponge = ["https://imgflip.com/memegenerator/Mocking-Spongebob",2,"Mocking-Spongebob"]
bat = ["https://imgflip.com/memegenerator/Batman-Slapping-Robin",2]
doge = ["https://imgflip.com/memegenerator/Buff-Doge-vs-Cheems",4]
brain = ["https://imgflip.com/memegenerator/Expanding-Brain",4]
cat = ["https://imgflip.com/memegenerator/Woman-Yelling-At-Cat",2]
gru = ["https://imgflip.com/memegenerator/Grus-Plan",4]
monke = ["https://imgflip.com/memegenerator/Monkey-Puppet",2]
always = ["https://imgflip.com/memegenerator/Always-Has-Been",2]
board = ["https://imgflip.com/memegenerator/Boardroom-Meeting-Suggestion",4]
nut = ["https://imgflip.com/memegenerator/Blank-Nut-Button",2]
skel = ["https://imgflip.com/memegenerator/Waiting-Skeleton",2]
panik = ["https://imgflip.com/memegenerator/Panik-Kalm-Panik",3]
handshake = ["https://imgflip.com/memegenerator/Epic-Handshake",3]
disaster = ["https://imgflip.com/memegenerator/Disaster-Girl",2]
bernie = ["https://imgflip.com/memegenerator/Bernie-I-Am-Once-Again-Asking-For-Your-Support",2]
leo = ["https://imgflip.com/memegenerator/Laughing-Leo",2]
pablo = ["https://imgflip.com/memegenerator/Sad-Pablo-Escobar",3]
memelist = []
memelist.append(drake)
memelist.append(distract)
memelist.append(twobut)
memelist.append(change)
memelist.append(ball)
memelist.append(leftex)
memelist.append(uno)
memelist.append(sponge)
memelist.append(bat)
memelist.append(doge)
memelist.append(brain)
memelist.append(cat)
memelist.append(gru)
memelist.append(monke)
memelist.append(always)
memelist.append(board)
memelist.append(nut)
memelist.append(skel)
memelist.append(panik)
memelist.append(handshake)
memelist.append(disaster)
memelist.append(bernie)
memelist.append(leo)
memelist.append(pablo)
memenames = ""
for i in range(len(memelist)):
    memenames += ("#" + str(i + 1) + ": " + memelist[i][0][34:] + "\n")


client = commands.Bot(command_prefix = '/')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def makememe(ctx):
    def check(m):
        return m.author.id == ctx.author.id
    await ctx.send("Would you like to randomize your meme?")
    check1 = False
    randomcheck = False
    while check1 == False:
        ans = await client.wait_for('message', check = check)
        ans = ans.content
        if(ans.lower() == "yes" or ans.lower() == "y"):
            await ctx.send("Ok, randomizing meme.")
            check1 = True
            randomcheck = True
        elif(ans.lower() == "no" or ans.lower() == "n"):
            await ctx.send("Ok, here's the list of memes that are available to pick from:")
            await ctx.send(memenames)
            check1 = True
            randomcheck = False
        else:
            await ctx.send("Answer the question, please!")
    memi = -1
    if randomcheck == True:
        memi = random.randint(0,len(memelist) - 1)
    else:
        check2 = False
        while check2 == False:
                await ctx.send("Please pick a number that corresponds to a meme.")
                memi = await client.wait_for('message', check = check)
                try:
                    memi = int(memi.content) - 1
                    if memi >= 0 and memi < len(memelist):
                        check2 = True
                    else:
                        await ctx.send("That number doesn't correspond to a meme, please pick one that does!")
                except:
                    await ctx.send("This is not a number! Please pick a number for your meme selection.")
    link = memelist[memi][0]
    numinp = memelist[memi][1]
    listinp = []
    await ctx.send("This meme has " + str(numinp) + " inputs.")
    for i in range(numinp):
        await ctx.send("What would you like input #" + str(i + 1) + " to be?")
        inp = await client.wait_for('message', check = check)
        listinp.append(inp.content)
    driver = webdriver.Chrome('pathtochromedriver/chromedriver.exe')  # replace "pathtochromedriver" with path to wherever chromedriver is installed on your computer
    driver.get(link);
    if memi == 17 or memi == 20 or memi == 22:
        Xpath = "//textarea[@placeholder='Top Text']"
        inputElement = driver.find_element_by_xpath(Xpath)
        inputElement.send_keys(listinp[0])
        Xpath = "//textarea[@placeholder='Bottom Text']"
        inputElement = driver.find_element_by_xpath(Xpath)
        inputElement.send_keys(listinp[1])
    else:
        for i in range(numinp):
            xpath1 = "//textarea[@placeholder='Text #"
            Xpath = xpath1 + str(i + 1) + "']"
            inputElement = driver.find_element_by_xpath(Xpath)
            inputElement.send_keys(listinp[i])
    time.sleep(1)
    generateButton = driver.find_element_by_class_name("mm-generate.b.but")
    generateButton.click()
    time.sleep(2)
    pic = driver.find_element_by_class_name("img-code.link")
    piclink = pic.get_attribute('value')
    await ctx.send(piclink)
    driver.close()
    driver.quit()

client.run('put Discord bot Token here') #replace 'put Discord bot Token here' with your discord bot's token
