from bs4 import BeautifulSoup
from selenium import webdriver
import urllib  ## url 인코딩
import pymysql
# 크롬 headless 모드 실행
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('lang=ko_KR')

driver = webdriver.Chrome('chromedriver_win32/chromedriver.exe', chrome_options=chrome_options)
driver.implicitly_wait(3)  # implicity_wait은 뜻 그대로 브라우저에서 사용되는 엔진 자체에서 파싱되는 시간을 기다려 주는

search = "java"

search = urllib.parse.quote(search)

driver.get('http://www.jobkorea.co.kr/Search/?stext=' + search + '&tabType=recruit&Page_No=1')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
temp = soup.select("#content > div > div > div.cnt-list-wrap > div > div.recruit-info >"
                   " div.list-filter-wrap > p > strong")[0].get_text()

print(temp)
# driver.quit()
result2=[]
child_num =1
while 1:
    driver.implicitly_wait(1)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    if child_num==1:
    #     name =       soup.select("#content > div > div > div.cnt-list-wrap > div >"
    #                        " div.recruit-info > div.lists >"
    #                        " div > div.list-default > ul > li.list-post.active "
    #                        "> div > div.post-list-info > a")[0].get_text()
    #
    #     career=       soup.select("#content > div > div > div.cnt-list-wrap.topLine > "
    #                         "div > div.recruit-info > div.lists > div > div.list-default >"
    #                         " ul > li.list-post.active > div > div.post-list-info "
    #                         "> p.option > span.exp")[0].get_text()
    #
    #     Education =      soup.select("#content > div > div > div.cnt-list-wrap.topLine > div > div.recruit-info >"
    #                            " div.lists > div > div.list-default > ul > li.list-post.active "
    #                            "> div > div.post-list-info > p.option > span.edu")[0].get_text
    #     time =         soup.select("#content > div > div > div.cnt-list-wrap.topLine > div > div.recruit-info > "
    #                        "div.lists > div > div.list-default > ul > li.list-post.active > div >"
    #                        " div.post-list-info > p.option > span:nth-child(3)")[0].get_text
    #
    #     area =        soup.select("#content > div > div > div.cnt-list-wrap.topLine > div > div.recruit-info > "
    #                        "div.lists > div > div.list-default > ul > li.list-post.active > div "
    #                        "> div.post-list-info > p.option > span.loc.short")[0].get_text
    #     dday =      soup.select("#content > div > div > div.cnt-list-wrap.topLine > div > div.recruit-info >"
    #                        " div.lists > div > div.list-default > ul > li.list-post.active > div"
    #                        " > div.post-list-info > p.option > span.date")[0].get_text
    #
    # dic = {"name":name ,"career":career, "Education":Education , "time":time, "area":area, 'dday':dday}
    # result2.append(dic)
       # print(soup.select(".option")[1].get_text)
       #  my_list = soup.select("#content > div > div > div.cnt-list-wrap >"
       #                        " div > div.recruit-info > div.lists > "
       #                        "div > div.list-default > ul > li.list-post.active")

    # content > div > div > div.cnt-list-wrap > div > div.recruit-info > div.lists > div > div.list-default > ul > li.list-post.active > div > div.post-list-corp > a
        print(soup.select(".list-post.active")[0].select("a")[0].get("title"))
        list_first = soup.select(".list-post.active")[0]
        option = list_first.select(".option")[0]
        list_op=[]
        for op in option.get_text().split("\n"):
            list_op.append(op)


    name =  list_first.select("a")[0].get("title")
    #
    contents=  list_first.select("a")[1].get("title")
    #
    # career = option.select(".exp")[0].get_text()
    #
    # Education = option.select(".edu")[0].get_text()
    #
    # time = option.select("span:nth-child(3)")[0].get_text()
    #
    # area = option.select(".loc.short")[0].get_text()
    #
    # date = option.select(".date")[0].get_text()

    dic = {"name": name, "career": list_op[1], 'education': list_op[2] ,'time' : list_op[3], 'area': list_op[4],
           'date': list_op[4] ,'contents' : contents}

    result2.append(dic)
    print(result2)
    # for title in my_list:
        #     print(title.get())
    #print(result2)



    try:
        break
        #print(soup.select(".option")[child_num].get_text)
        #child_num += 1
    except:
        print("페이지 끝남")
        break
driver.quit()
# print(result2)
# fw =open(search+'.txt','w', -1, "utf-8")
# for i in result2:
#     fw.write(i)
# fw.close()
# my sql install https://m.blog.naver.com/bjh7007/221829548634
# mysql 워크 빈치 쓸때   ''''''' 따옴표 이게 아니라 ``````````이거임