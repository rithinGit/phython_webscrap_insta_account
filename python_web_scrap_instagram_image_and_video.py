import time
from selenium import webdriver 
from bs4 import BeautifulSoup as bs 
import urllib.request 
import os


####
username = 'the_new_girl_in_city' ##destination accout where download files from this account
####

# Create target Directory if don't exist
directory_name_to_save_image = username+'_instagram_saved_on'+time.strftime("%Y%m%d-%H%M%S")
#
if not os.path.exists(directory_name_to_save_image):
    #
    os.mkdir(directory_name_to_save_image)
    #

#Username
user = 'your insta username'
#Password
pwd = 'your insta password'


driverpath = 'chromedriver.exe' 
driver = webdriver.Chrome(driverpath) 



driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')

time.sleep(2)

elem = driver.find_element_by_name("username")
elem.send_keys(user)

time.sleep(2)

elem = driver.find_element_by_name("password")
elem.send_keys(pwd)


time.sleep(2)

#driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]/button").click() 
driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]/button").click()


time.sleep(2)

#https://www.instagram.com/the_new_girl_in_city/


#driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[2]").click()


time.sleep(2)

#driver.find_element_by_xpath("//*[@id='react-root']/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[3]/button/div[1]").click()

driver.get('https://www.instagram.com/'+username)



time.sleep(2)

##

####
accessable_link_array_of_data = []
# #sleep time is required. If you don't use this Instagram may interrupt the script and doesn't scroll through pages
SCROLL_PAUSE_TIME  = 2
##Max_scroll_exicute = 2 
##Current_scroll_cnt = 0
# # Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
##
while True:
     #Scroll down to bottom
     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
     #######
     Current_scroll_cnt = Current_scroll_cnt + 1 
     #######
     source = driver.page_source 
     data   = bs(source, 'html.parser') 
     data_b = data.findAll("div", {"class": "v1Nh3"}) 
     for current_single_div in data_b:
        link_from_this_array = current_single_div.findAll('a' , href=True) 
        for link_from_this_array_above in link_from_this_array: 
            accessable_link_array_of_data.append(link_from_this_array_above['href']) 
     #######
#    # Wait to load page
     time.sleep(SCROLL_PAUSE_TIME)
#     # Calculate new scroll height and compare with last scroll height
     new_height = driver.execute_script("return document.body.scrollHeight")
     #################
     ##if Current_scroll_cnt >= Max_scroll_exicute: to limit max scrolls
        ##break
     #################
     if new_height == last_height:
         break
     last_height = new_height
##
####Unique Links######
accessable_link_array_of_data = set(accessable_link_array_of_data) 
####Unique Links######/p/BPlXkoRAIGp/
time.sleep(4)
##################
for repeat_unique_links in accessable_link_array_of_data:
    ####
    if len(repeat_unique_links) > 4:
        ##
        driver.get('https://www.instagram.com'+repeat_unique_links)
        ##
        source = driver.page_source
        data   = bs(source, 'html.parser')
        ##
        data_image_item = data.findAll("div", {"class": "KL4Bh"})
        ##
        data_video_item = data.findAll("div", {"class": "_5wCQW"})
        ####
        try:
            if len(data_image_item) > 0: 
                ##
                index_for_image = 0
                for data_image_item_repeat in data_image_item:
                    ##
                    image_from_this_array = data_image_item_repeat.findAll('img', attrs = {'srcset' : True})
                    ##
                    try:
                        if len(image_from_this_array) > 0:
                            for image_src_list in image_from_this_array:  
                                ##
                                #print(image_src_list['srcset'])
                                data_link_splitted = image_src_list['srcset'].split(",")
                                ##
                                for data_link_splitted_items in data_link_splitted:
                                    #
                                    index_for_image += 1
                                    #
                                    file_name_unique_for_download = directory_name_to_save_image+'/'+'instagram_image_on_'+time.strftime("%Y%m%d-%H%M%S")+'_'+str(index_for_image)+'.jpg'
                                    ##print(file_name_unique_for_download)
                                    print(data_link_splitted_items)  
                                    print('---------')
                                    try:
                                        ####
                                        space_after_separate = " ";
                                        ####
                                        data_link_splitted_items = data_link_splitted_items.split(space_after_separate, 1)[0]
                                        ####data_link_splitted_items = data_link_splitted_items.replace(" ", "%")
                                        urllib.request.urlretrieve(data_link_splitted_items, file_name_unique_for_download)
                                    except Exception as e:
                                        print(str(e))
                                ##    
                    except:
                        print("Repeat firt open call image collection") 
                    ##    
                ####
        except:
            print("Repeat firt open call")
        ####
        try:
            ####
            if len(data_video_item) > 0:
                ##
                index_for_video = 0 
                for data_video_item_repeat in data_video_item:
                    ##
                    video_from_this_array = data_video_item_repeat.findAll('video')
                    ##
                    try:
                        ####
                        if len(video_from_this_array) > 0:
                            ##
                            for video_loop_from_above in video_from_this_array: 
                                 if len(video_loop_from_above['src']) > 4:
                                    index_for_video += 1
                                    file_name_unique_for_download = directory_name_to_save_image+'/'+'instagram_video_on_'+time.strftime("%Y%m%d-%H%M%S")+'_'+str(index_for_video)+'.mp4'  
                                    urllib.request.urlretrieve(video_loop_from_above['src'], file_name_unique_for_download)
                            ## 
                        ####
                    except Exception as e:
                        print("Repeat firt open call video collection") 
            ####
        except:
            print("Repeat firt open call") 
        ####
        time.sleep(4)
        ##
    ####
##################