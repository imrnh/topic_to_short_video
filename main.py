import time, os
from tqdm.auto import tqdm
from kb import make_knowledge_base


def main(video_title, keywords):
    master_knowledge_base = []
    master_knowledge_string = ""

    for kyw in keywords.split(", ")[:1]: # Taking top 3 for now.
        kb = make_knowledge_base(search_query=kyw, video_title=video_title)
        master_knowledge_base.append(kb)

        time.sleep(10) # to prevent google's IP ban due to frequent searching.

    for kb_list in master_knowledge_base:
        for item in kb_list:
            master_knowledge_string += item + " \n\n "

    master_knowledge_string = master_knowledge_string.encode("UTF-8")

    with open("knowledge_base.text", "a", encoding="utf-8") as kb:
        kb.write(item)



if __name__ == "__main__":
    video_title = "The Impact of Caffeine on Mental Health"
    keywords = "Caffeine and anxiety, Caffeine consumption, Caffeine and mental health, Caffeine dependence, Caffeine and depression, Neurotransmitters and caffeine, Caffeine addiction, Caffeine and sleep disorders, Caffeine withdrawal symptoms, Safe caffeine intake"
    
    main(video_title, keywords)