message = '''曲: 周杰倫
Qu: Zhou Jie Lun
Lyrics: Jay Chou'''

print("The full message is:\n",message)
print("\nThe number of characters in the string is ", len(message)) #Number of characters in string.
print("The number of lines is ", message.count("\n") + 1) #Good for prioritizing which Mandarin karaoke characters to memorize for karaoke.

index1 = message.find("\n", 1)
index2 = message.find("\n", index1 + 1) #Last arg in find method is the what character positiion to begin the search.
index3 = message.find("\n", index2 + 1)
print("Index of 1st newline char (counting any invisible space characters at end of line) is at char ", message.find("\n")) #Maybe can use this to find where Chinese characters stop and pinyin starts.
print("index2 = ", index2)
print("index3 = ", index3)
line1 = message[:index1]
line2 = message[index1+1:index2]
line3 = message[index2+1:]
print("line1 = ", line1)
print("line2 = ", line2)
print("line3 = ", line3)

# Start with this value.
location = -1
while True:
    location = message.find("\n", location + 1) # Find next occurrence by starting search at character +1 after previous occurrence.
    if location == -1: break # Break if not found.
    print(location)

print("\nCharacters 4 thru 11 going past the newline characters are:\n", message[4:12])
print("Number of characters 4 thru 11 including newline characters is: ", len(message[4:12]))
print("Changing the message to lowercase gives:\n", message[4:12].lower())
temp = message.replace("曲", "杰")
print("After replacing 曲 with 杰, the full message becomes:\n",temp)

combined = message.replace("\n", "") #Substitute love words with RE words to create RE versions of love songs.
print("Removing newlines characters combines the lines into ", combined)
print("The number of characters in the new string without newline characters is ", len(combined))


greeting = 'Hello'
name = 'Michael'
message = "{} .... {}!!  You da man!".format(greeting, name) #Need to use to format for python2.
print(message)
message = f"Really {greeting} .... {name}!!  You da man!" #Good for RE form letters to multiple people.  Or cover letters to multiple employers.
print(message)
message = f"{greeting.upper()} .... {name.upper()}!!  You da man!" #Good for bolding/highlighting key words.
print(message)

print(dir(message))
#print(help(str))
#print(help(str.lower))

message = '''曲: 周杰倫
Qu: Zhou Jie Lun
Lyrics: Jay Chou

久未放晴的天空 依舊留著你的笑容
jiu wei fang qing de tian kong / yi jiu liu zhe ni de xiao rong
The sky which has long not been sunny still keeps your smile as before

哭過 卻無法掩埋歉疚
ku guo / que wu fa yan mai qian jiu
Have cried, but been unable to bury [my] guilt

風箏在陰天擱淺 想念還在等待救援
Feng zheng zai yin tian ge qian / xiang nian hai zai deng dai jiu yuan
The kite stranded in the gloomy sky, [my] longing is still awaiting to be rescued

我拉著線 複習你給的溫柔
wo la zhe xian / fu xi ni gei de wen rou
I'm pulling the kite string and reviewing the tenderness you gave


曝晒在一旁的寂寞
pu shai zai yi pang de ji mo 
The loneliness that has been isolated on the side

笑我給不起承諾
xiao wo gei bu qi cheng nuo
Laughing at the promises that I can't afford to give

怎麼會怎麼會 你竟原諒了我
zen me hui zen me hui ni jing yuan liang le wo
How come, how come, you've actually forgiven me


我只能永遠讀著對白 讀著我給你的傷害
wo zhi neng yong yuan du zhe dui bai / du zhe wo gei ni de shang hai
I can only forever read the dialogue, reading the pain that I've given you

我原諒不了我 就請你當作我已不在
wo yuan liang bu liao wo / jiu qing ni dang zuo wo yi bu zai
I cannot forgive myself, so please treat as if I'm not here anymore

我睜開雙眼看著空白 忘記你對我的期待
wo zheng kai shuang yan kan zhe kong bai / wang ji ni dui wo de qi dai
I looked on blankly with eyes wide open, [trying] to forget the expectations you had of me

讀完了依賴 我很快就離開
du wan le yi lai / wo hen kuai jiu li kai
After finish reading [my] dependence [on you], I'll leave very soon '''


print("\nThe number of characters in the string is ", len(message)) #Number of characters in string.
print("The number of lines is ", message.count("\n") + 1) #Good for prioritizing which Mandarin karaoke characters to memorize for karaoke.

index1 = message.find("\n", 1)
index2 = message.find("\n", index1 + 1) #Last arg in find method is the what character positiion to begin the search.
index3 = message.find("\n", index2 + 1)
index4 = message.find("\n", index3 + 1)
index5 = message.find("\n", index4 + 1)
index6 = message.find("\n", index5 + 1)
index7 = message.find("\n", index6 + 1)
print("Index of 1st newline char (counting any invisible space characters at end of line) is at char ", message.find("\n")) #Maybe can use this to find where Chinese characters stop and pinyin starts.
print("index2 = ", index2)
print("index3 = ", index3)
print("index4 = ", index4)
print("index5 = ", index5)
print("index6 = ", index6)
print("index7 = ", index7)
line1 = message[:index1]
line2 = message[index1+1:index2]
line3 = message[index2+1:index3]
line4 = message[index3+1:index4]
line5 = message[index4+1:index5]
line6 = message[index5+1:index6]
line7 = message[index6+1:]
print("line1 = ", line1)
print("line2 = ", line2)
print("line3 = ", line3)
print("line4 = ", line4)
print("line5 = ", line5)
print("line6 = ", line6)
print("line7 = ", line7)

#print(message)
print(len(message))
print(message.count("我"))
print(message.find("我"))
new_message = message.replace("我", "Wo")
#print(new_message)

print(message[3:9])
print(len(message[3:9]))

print(message[0:9])
print(len(message[0:9]))
print(message[0:9].lower())

message = message.replace("我", "Wo baby baby")
#print(message)

greeting = '你好'
name = '哥哥'
message = "{} .... {}!!  You da man!".format(greeting, name)
print(message)
message = f"Really {greeting} .... {name}!!  You da man!"
print(message)
message = f"{greeting.upper()} .... {name.upper()}!!  You da man!"
print(message)