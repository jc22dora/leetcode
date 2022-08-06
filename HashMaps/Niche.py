class Solution:
    global globalWords
    
    def index(self, allReviews) -> int:
        globalWords = {}
        for school in allReviews:
            name = school[0]
            reviews = school[1]
            reviewId = 0
            for review in reviews:
                reviewId += 1
                review = review.lower()
                review = review.split()
                
                words = {}
                for word in review:
                    if(words.get(word)):
                        words[word] += 1
                    else:
                        words[word] = 1
                    if(globalWords.get(word)):
                        if(globalWords[word].get(name)):
                            if(globalWords[word][name].get(reviewId)):
                                # we've already seen this word in this review
                                pass
                            else:
                                globalWords[word][name][reviewId] = 1
                                if(globalWords[word][name]["reviewCount"]):
                                    globalWords[word][name]["reviewCount"] += 1
                                else:
                                    globalWords[word][name]["reviewCount"] = 1
                        else: globalWords[word][name] ={reviewId:1, "reviewCount": 1}
                    else:
                        globalWords[word] = {name:{reviewId:1, "reviewCount": 1}}

        return globalWords

    def getNumOfReviews(self, keywords, reviews):
        for key in keywords:
            print("for keywords: "+key)
            if(dict[key]):
                for doc in reviews:
                    name = doc[0]
                    try:
                        print("In "+str(dict[key][name]["reviewCount"])+" reviews for "+name)
                    except:
                        pass


if __name__ == "__main__":
    clark = ["Clark College", ["""Thanks to the ease of scheduling and flexibility offered in times and days classes are offered, i have had the great oppurtunity of actually attending college on campus versus the online school I was attending. I can do this while still having the ability to take care of my 3 year old son as a single mommy while continuing to hold down my 11-7 job 4 days a week. Thanks Clark for making my eduation possible! :) Clark College is very academically flexible. They are a two year college that deals with transfer students and running start students all of the time so they know how to deal with the different academic situations.
All clark students have access to the on-campus library, employment office, peer mentors, and tutors. Everyone gets the tools they need to be successful at Clark.
Clark is a great place to learn, especially considering the price level of the school. The teachers that i've had thus far have been animated and motivated in their areas of expertise and it helps to keep your attention when your instructors actually seem to care. I'm not a fan of the Running Start program, as the average Highschool student is not prepared to act in the manner appropriate for college learning. All in all i'm happy with Clark and would make the decision again.
This is mainly my fault because I wasn't responsible enough to register for classes on time..but I've heard that other students that didn't procrastinate have had a tough time registering for classes because they fill up so quick. I guess that's sort of a good thing because it shows that our school is growing, but that also means that we need to hire more staff. My opinion..
There is no need to interact with fellow students, so you can go about your day unbothered.
The mechanical engineering program is very good, but the workload is practically impossible if you want to get through the curriculum in the 'ideal' two years. In addition, it would have been nice if there were more hands-on projects involved in the classes to reinforce the teachings. Also, some of the engineering professors are somewhat unapproachable, and tend to assume that just because you're in engineering, any shortcuts or methods that they use to solve practice problems are inherently obvious to anyone with a few brain cells. However, the majority are friendly and easy to talk to, with a genuine interest in your success as a student.
Sometimes the wireless was easy to get on. Other times, you couldn't get on for half an hour or more. It got very frustrating when you had a limited amount of time between classes and such to do whatever you needed online to spend the majority of it attempting to connect.
I would say that I'm really satisfied with this school. Everyone from the staff to students are all really nice. I like the atmosphere of the college, and I always feel motivated to learn. The professors are all amazing, and you can learn so much from them. They are all dedicated and want to make every student learn. It's only a community college, so I'm only there for 2 years, but it's been really fun so far!
The main reason I chose this school was because of how flexible the class schedules are. I am able to work around my personal schedule, which is great.""", "greek", "greek"]]
    iowa = ["Iowa Western Community College", ["""The professors are really good, they are always trying to make sure everyone understood the material that is discussed in class, they always give their information to where they can be contacted outside of class and their office hours, also they are really good on replying back via e-mails. The class registration is good  you can do it with the help of your adviser or if you already know the classes that you are taking you are able to register by yourself which sometimes is helpful time wise.
I am studying Human Services and I love all my classesd that relate to my field we get hands on training by going out to different agencies to rate them
the financial aid im getting from iwcc is great. It came thru in a timely manner and was available as soon as it was posted to my account.The first couple of weeks were stressful not knowing when my aid would come through. When it did it helped out alot with the cost i had accumatelated. I would say when it comes down to it get it done for your future recieve all the help you can get because its out there with a little wait. Be upfront and get what you need when you needed it.
There is a lot of money one can receive.
IWCC's student body has a diverse range of traditional, international, non- traditional, and cultures. But as &quot;Reivers&quot; we all are like one family, of course every family has their disagreement, when push comes to shove, &quot;Reivers&quot; stand together
The computer network seems average. There has been a few days it has been completely down, but nothing too major. Speed is good. Wireless is available. You can check out netbooks from the library for a period of time.
I've had a pretty good experience flexibility wise. When I couldn't come to class and missed a test, the teacher stayed late to let me finish it. I know that most of my teachers would do whatever they can to help me succeed.
You will see many different students and diverse backgrounds on this campus. We have students who attend here that are still in high school.  Others come because tuition is cheaper here than schools in their own states.  There are many athletic programs available that many would not get into if they were going to a larger school.  Overall, it is a great place to go to find out if you are ready to go onto a 4-year school.
Though the technology in the classroom is top notch, in the dorms it is less than caveman have. The internet goes down almost every week. When I asked the Cox Cable guy about it he said that the dorms were not priority. I think that where the students are doing most of their homework should be where the internet is.
I have seen all kinds of people from all walks of life at iowa western. I belive they have a international student exchange. everyone seems to get along and usually everyone is understanding of eachother. I enjoy haveing to diverse student body."""]]
    ri = ["Rhode Island College", ["""It is pretty chilly... Fortunately, most my classes are in 1 building, so I don't have to walk through snow constantly.
Many of the Greek students host events but most students on campus aren't involved in it. Most of the sorotities have off campus housing while few of them live on campus. Many non-Greek students get along with the Greek students.
The computers at school are not that up to date. We have two main computer labs but they are usually very busy so I bring my own laptop everyday.  There are people working at these labs but sometimes they get confused and are mostly there to do homework. The computers work at a decent speed and are free which is always a plus. The wireless access on campus is getting better !
Academic Programs and its recognition in education and psychology
Freshman can have cars on campus, plus there is public transportation available on campus to anywhere in the state.  They also have two ZipCars available at a low cost to students for short trips.  Take a bus to downtown and you can get the T to Boston or the Providence airport, or Amtrak to anywhere.  Very easy to get around.
I hate it here. There is no campus community and it's nearly impossible to meet anyone. Everyone is either a commuter or goes home every weekend. Even the people who live on campus already have their group of friends because they are all from RI.
In dorms the RAs are overbearing but its a nice open campus. The campus police patrol and frown upon certain spots on campus. All in all, its fun and distracting.
The area is suburban. There are lots of people walking about. It is absolutely beautiful and provides the luxury of options with easy access to resources and benefits within the surrounding area. A CVS and a Stop and Shop are down the street with the added bonus of a campus book store and convenience store.
the library is great there is always someone who can help you. They have different sections and my favorite is the silent study level in the library, comes in handy when studying for exams. If your like me I need absolute silence and no distractions and that is what this floor of the library provides for me.
Rhode Island party sense is not the best Clubs close at 1 or 2 in the morning, and you need to car pool with someone who has a car. I been told Rhode Island College parties are horrible, people sit around and drink all night. If your looking for a decent party hit up a Johnston and Whales party."""]]
    reviews = [clark, iowa, ri]
    solution = Solution()
    dict = solution.index(reviews)
    solution.getNumOfReviews(["greek", "a", "students"], reviews)
    # Enter a search keyword:
    # a
    # In 7 reviews for Clark College
    # In 7 reviews for Iowa Western Community College
    # In 6 reviews for Rhode Island College
    